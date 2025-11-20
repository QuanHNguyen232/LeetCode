class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        """
        startPos = 1, endPos = 2, k = 3

        dp[i]: num of ways to get i-th pos --> cannot track k --> use 2D
        dp[i][j]: num of ways to get i-th pos in j steps
        dp[i][j] = (
            dp[i-1][j-1] + dp[i+1][j-1]
        )
        startPos = 1 --> dp[1][0] = 1
        
        Since we need i+1 and i-1 ==> cannot use bottom up
        # dp = [[0]*(k+1) for _ in range(2*k)]
        # dp[startPos][0] = 1
        # dp[j][0]= 0 for j != startPos
        
        constrains:
        0 <= j <= k
        i-k <= i <= i+k
        """
        MOD = 1e9+7
        
        
        memo = {}
        @cache
        def dp(currPos, stepsUsed):
            key = (currPos, stepsUsed)
            if key in memo:
                return memo[key]
            """
            endPos = 2, k = 3
            
            currPos = 1 or currPos = 3, stepsLeft = 1
            """
            # base case
            if currPos==startPos and stepsUsed==k:
                memo[key] = 1
                return 1
            if stepsUsed==k:
                memo[key] = 0
                return 0
            
            # recursion
            memo[key] = dp(currPos+1, stepsUsed+1) + dp(currPos-1, stepsUsed+1)
            memo[key] = int(memo[key] % MOD)

            return memo[key]
        
        return dp(endPos, 0)