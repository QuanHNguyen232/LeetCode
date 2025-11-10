class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        """
        dp[i]: len of longest subseq has diff=difference unitl i-th number
        dp[i]: (
            for j from 0->i
            max( dp[j] if nums[i]-nums[j]==diff )
        )
        """
        n = len(arr)
        dp = [1]*n

        for i in range(n):
            for j in range(i):
                if arr[i]-arr[j] == difference:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)