class Solution:
    def minSteps(self, s: str, t: str) -> int:
        hashmap = defaultdict(int)
        n = len(s) # len(s)=len(t)
        for i in range(n):
            hashmap[s[i]] += 1
            hashmap[t[i]] -= 1
        
        ans = 0
        # find pairs of positives and negatives.
        # in simple term, since it always can convert to t --> only need to count values>0
        for k, val in hashmap.items():
            if val > 0:
                ans += val

        return ans