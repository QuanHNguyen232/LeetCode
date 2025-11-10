class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # Solution 1: DP
        """
        nums=[10,9,2,5,3,7,101,18]
        dp  =[ 1,1,1,2,2,3,  4, 4] -> 4

        nums=[1,3,6,7,9,4,10,5,6]
        dp  =[1,2,3,4,5,3, 6,4,5] -> 6
        dp[i] = longest-increasing-subsequence until index i, including nums[i]
        dp[i] = max(
            nums[j] < nums[i] => max( [dp[j] for j in range(0,i)] ) + 1
        )
        """
        n = len(nums)
        dp = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
        # Time: O(N^2)
        # Space: O(N)

        # Solution 2: Binary Search
        # sub = []
        # for num in nums:
        #     if not sub or num > sub[-1]:
        #         sub.append(num)
        #     else:
        #         idx = bisect_left(sub, num)
        #         sub[idx] = num
        # return len(sub)