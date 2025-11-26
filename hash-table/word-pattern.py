class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words): return False

        pattern_map = {}
        s_map = {}
        for char, word in zip(pattern, words):
            if (
                char in pattern_map and word not in s_map
                or char not in pattern_map and word in s_map
            ):
                # either in map -> False
                return False
            elif char not in pattern_map and word not in s_map:
                # both not in map -> add
                pattern_map[char] = word
                s_map[word] = char
            else:
                # both in map -> check
                if pattern_map[char] != word or s_map[word] != char:
                    return False
        return True