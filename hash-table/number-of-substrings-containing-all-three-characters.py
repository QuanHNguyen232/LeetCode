class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        res = 0
        n = len(s)
        l = 0
        dictionary = defaultdict(int)
        for r in range(n):
            dictionary[s[r]] += 1
            while len(dictionary) >= 3:
                res += n - r
                dictionary[s[l]] -= 1
                if dictionary[s[l]] == 0:
                    del dictionary[s[l]]
                l += 1
        return res
