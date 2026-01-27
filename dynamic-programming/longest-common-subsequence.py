class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)

        def print_help():
            # backtrack to print result:
            path = []
            i, j = m, n
            while i > 0 and j > 0:
                if text1[i-1] == text2[j-1]:
                    path.append(text1[i-1])
                    i -= 1
                    j -= 1
                elif dp[i][j] == dp[i-1][j]:
                    i -= 1
                else:
                    j -= 1
            print(path[::-1])

        dp = [[0]*(n+1) for _ in range(m+1)]
        for i in range(m):
            for j in range(n):
                if text1[i] == text2[j]:
                    dp[i+1][j+1] = dp[i][j] + 1
                else:
                    # consider the subproblem that removes the first letter off the first word,
                    # and then the subproblem that removes the first letter off the second word.
                    dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
        
        return dp[m][n]
        # time: O(n^2)
        # space: O(n^2)

        # APPROACH 2
        # n = len(text1)
        # m = len(text2)

        # @lru_cache(maxsize=None)
        # def dp(idx1, idx2):
        #     '''
        #     '''
        #     # base case
        #     if idx1 == n or idx2 == m:
        #         return 0

        #     # recursion
        #     # either consider character at text1[idx1] or skip it
        #     option1 = dp(idx1 + 1, idx2)

        #     matchIdx = text2.find(text1[idx1], idx2)
        #     if matchIdx != -1:
        #         option2 = 1 + dp(idx1 + 1, matchIdx + 1)
        #     else:
        #         option2 = 0
            
        #     return max(option1, option2)
        
        # ans = dp(0, 0)
        
        # return ans