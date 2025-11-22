class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        '''
        valid triangle must have sum of 2 sides > another side
        a + b > c,
        b + c > a,
        a + c > b

        Let c be the largest number in triplet
        then:
            c >= a
            c >= b
            a + b > c
        note that:
            b + c >= b + a > a
        '''
        n = len(nums)
        nums.sort()
        ans = 0
        def binary_search(nums, l, r, target):
            # lower bound
            while l <= r:
                m = l + (r-l) // 2
                if target <= nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            return l

        for i in range(n-2):
            # k = i+2
            for j in range(i+1, n-1):
                k = j+1
                target = nums[i] + nums[j]
                k = binary_search(nums, k, n-1, target) # k: the element just > target
                ans += (k-1)-j # since requires target>k --> k-1 to be what we need

        return ans