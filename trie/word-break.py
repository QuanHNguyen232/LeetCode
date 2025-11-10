class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        dp[i]: is string s until index i-th segmented (include s[i])
        dp[i] = s[0:j+1] segmentable/dp[j] and s[j+1:i+1] in dictionary
        ==> dp[i] = dp[j] and s[j+1 : i+1] in wordDict
        """
        n = len(s)
        dp = [False] * n
        for i in range(n):
            for word in wordDict:
                if i < len(word) - 1:
                    # len(word) - 1: index of char at end of word
                    # i does not enough to contain that word
                    continue

                if i == len(word) - 1 or dp[i - len(word)]:
                    # i == len(word) - 1: s starts with word
                    # dp[i - len(word)] OR dp[j] aka s[0:j+1] segmentable
                    if s[i - len(word) + 1 : i+1] == word:
                        dp[i] = True
                        break

        return dp[-1]

    def sln_1(self, s, wordDict):
        # cat sand og
        # cats and og

        # dp(i) is return true if s[i..n) (a.k.a: s[i:n]) can be segmented into a space-separated sequence of one or more dictionary words.
        # 

        # dp(n) is the empty string -> return true
        n = len(s)
        wordSet = set(wordDict)

        @cache
        def dp(i):
            if i == n:
                return True

            for j in range(i, n):
                word = s[i:j+1]
                if word in wordSet and dp(j+1):
                    return True

            return False

        ans = dp(0)
        return ans