class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        idx1 = idx2 = -math.inf
        ans = math.inf
        for i, word in enumerate(wordsDict):
            if word == word1:
                idx1 = i
            if word == word2:
                idx2 = i
            ans = min(ans, abs(idx1 - idx2))
        
        return ans