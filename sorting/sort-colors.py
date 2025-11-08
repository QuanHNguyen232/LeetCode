class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # return self.count_sort(nums)
        return self.quick_sort(nums)
    
    def quick_sort(self, nums: List[int]) -> None:
        # soln 1: based on quicksort
        n = len(nums)
        
        # move all 0 to left
        left = 0
        for i in range(n):
            if nums[i] < 1:
                nums[left], nums[i] = nums[i], nums[left]
                left += 1
        
        # move all 2 to right
        right = n-1
        for i in range(n-1, left-1, -1):
            if nums[i] > 1:
                nums[right], nums[i] = nums[i], nums[right]
                right -= 1
        # time: O(n)
        # space: O(1)
    
    def count_sort(self, nums: List[int]) -> None:
        # soln 2: counting sort

        # step 1: count
        count = [0]*3
        for num in nums:
            count[num] += 1

        # step 2: get index by cummulate count
        idxes = [count[0]]
        for val in count[1:]:
            idxes.append(idxes[-1] + val)

        # step 3:
        for val in range(len(count)):
            for _ in range(count[val]):
                idx = idxes[val] - 1
                nums[idx] = val

                idxes[val] -= 1
        # time: O(m+n) where m: maxVal, n: len of nums
        # space: O(m) for idxes
