class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # n = len(nums)
        # nums.sort() # O(nlogn)
        
        # def getBit(x, k):
        #     return (x >> k) & 1

        # ans = []
        # seen = set()
        # for x in range(1 << n): # O(2^n)
        #     subset = []
        #     s = ''
        #     for i in range(n): # O(n)
        #         if getBit(x, i) == 1:
        #             subset.append(nums[i])
        #             s = s + str(nums[i])
        #     if s not in seen:
        #         ans.append(subset)
        #         seen.add(s)

        # return ans
        # time: O(2^n * n)
        # space: O(2^n * n) where O(2^n) is for seen and each subset string is O(n)

        nums.sort()
        res = []

        def backtrack(idx, curr: list):
            """
                          []
                    /     |         \
                [1]       [2]        [2]  <= This branch should be skipped
                          |
                          [2,2]
            """
            # base
            # if idx == len(nums):
            #     return

            # do sth
            res.append(curr[:])

            # recursion
            for i in range(idx, len(nums)):
                if i > idx and nums[i] == nums[i-1]:
                    # Skip duplicates on the same tree level
                    continue
                curr.append(nums[i])
                backtrack(i + 1, curr)
                curr.pop()

        backtrack(0, [])

        return res
        
        # n = len(nums)
        # curr_soln = []
        # ans = []

        # def choose(i):
        #     # base case
        #     if i == n:
        #         ans.append(curr_soln[:])
        #         return

        #     # recursion
        #     curr_soln.append(nums[i])
        #     choose(i+1)
        #     curr_soln.pop()

        #     # choose(i+1)
        
        # nums.sort()
        # choose(0)
        # return ans