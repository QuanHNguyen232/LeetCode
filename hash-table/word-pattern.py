class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words): return False

        pattern_map = {}
        for char, word in zip(pattern, words):
            if char not in pattern_map:
                pattern_map[char] = word
            if char in pattern_map and pattern_map[char] != word:
                return False
        return True