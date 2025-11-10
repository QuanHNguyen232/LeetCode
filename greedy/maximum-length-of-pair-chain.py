class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        """
        similar to LIS (Longest Increasing Subsequence) https://leetcode.com/problems/longest-increasing-subsequence/
        dp[i]: max len at pair i-th
        dp[i] = max(
            dp[j] from j=0->i-1
            if sorted_pairs[j][1] < sorted_pairs[i][0]
        )
        """
        pairs.sort(key=lambda pair: (pair[0], pair[1]))
        n = len(pairs)
        dp = [1] * n
        
        for i in range(n):
            for j in range(i):
                if pairs[j][1] < pairs[i][0]:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        return max(dp)