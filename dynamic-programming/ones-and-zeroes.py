class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        """0/1 Knapsack
        dp[i][m][n]: size of the largest subset, from 0->i (inclusive) with at most m zeroes and n ones
        dp[i][m][n] = (
            if not take: dp[i-1][m][n]
            if take: dp[i-1][m - 0s][n - 1s] + 1 if m-0s>=0 and n-1s>=0
                    (1s=Counter[1], 0s=Counter[0])
        )
        """
        limit_i = len(strs)
        M = m
        N = n
        dp = [[[0]*(N+1) for _ in range(M+1)] for _ in range(limit_i)]
        # base case
        for i in range(limit_i):
            cnter = Counter(strs[i])
            cnt_1 = cnter["1"]
            cnt_0 = cnter["0"]
            for m in range(M+1):
                for n in range(N+1):
                    not_take = dp[i-1][m][n]
                    take = dp[i-1][m - cnt_0][n - cnt_1] + 1 if (m-cnt_0>=0 and n-cnt_1>=0) else 0
                    dp[i][m][n] = max(not_take, take)
        
        for i in range(limit_i):
            for row in dp[i]: print(row)
            print()

        return dp[limit_i-1][M][N]