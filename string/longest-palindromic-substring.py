class Solution:
    def longestPalindrome(self, s: str) -> str:
        N = len(s)
        if N <= 1:
            return s
        
        ans = ""
        memo = [[False]*N for _ in range(N)]

        def inBound(idx):
            return 0 <= idx < N

        def dp(i, j): # O(N)
            nonlocal ans
            if memo[i][j]:
                # update ans
                ans = s[i:j+1] if j - i + 1 > len(ans) else ans
                # expand
                newI ,newJ = i-1, j+1
                if inBound(newI) and inBound(newJ) and s[newI] == s[newJ]:
                    memo[newI][newJ] = True
                    # recursion
                    dp(newI, newJ)

        # len(word) is odd
        for i in range(N): # O(N)
            memo[i][i] = True
            dp(i, i)

        # len(word) is even
        for i in range(N-1): # O(N)
            j = i+1
            memo[i][j] = s[i] == s[j]
            dp(i, j)

        return ans
        # O(N^2)