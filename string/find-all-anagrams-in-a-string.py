class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans = []
        p_dict = Counter(p)
        s_dict = defaultdict(int)
        l = 0
        n = len(s)
        m = len(p)
        for r, c in enumerate(s):
            s_dict[c] += 1
            while s_dict[c] > p_dict[c]:
                s_dict[s[l]] -= 1
                l += 1
            if r-l+1 == m:
                ans.append(l)


        return ans