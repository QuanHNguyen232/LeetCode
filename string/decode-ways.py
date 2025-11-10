class Solution:
    def numDecodings(self, s: str) -> int:
        """
        s = 226

        dp[i]: number of ways to decode string s until i-th (exclusive) --> s[0:i]
        dp[i] = (
            dp[i-1] (case 1 digit)
            + dp[i-2] (case 2 digits)
        )
        """
        n = len(s)
        dp = [0] *(n+1)
        dp[0] = 1
        dp[1] = 0 if s[0] == "0" else 1
        
        for i in range(2, n+1):
            if s[i - 1] != "0":
                dp[i] += dp[i - 1]
            if "10" <= s[i - 2 : i] and s[i - 2 : i] <= "26":
                dp[i] += dp[i - 2]

        return dp[n]

    def sln_1(self, s: str) -> int:
        n = len(s)

        # dp(i) is the number of ways to decode s[i...n)
        @cache
        def dp(i):
            if i == n:
                return 1

            ans = 0
            # Case 1: single digit starting at i (1..9)
            if s[i] != '0':
                ans += dp(i+1)

            # Case 2: 2 digits starting at index i (10..26)
            if i+1 < n and (s[i] == '1' or s[i] == '2' and s[i+1] <= '6'):
                ans += dp(i+2)

            return ans

        return dp(0)

