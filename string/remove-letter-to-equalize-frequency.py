class Solution:
    def equalFrequency(self, word: str) -> bool:
        cnter = Counter(word)
        freq_cnter = Counter(cnter.values())
        keys = list(freq_cnter.keys())
        vals = list(freq_cnter.values())
        
        if (len(freq_cnter) == 1):
            """
            "abcde" {1: v} -> True (-> {1:v-1})
            "aaaaa" {k: 1} -> True (-> {k-1:1})
            "aabb" {k:v} -> False (-> {v-1:1, k:v-1})
            """
            return keys[0] == 1 or vals[0] == 1
        if (len(freq_cnter) == 2):
            """
            "abbcc" {1: 1, 2: 2} -> True (rm key=1 (smaller, must be key=1))
            "abbcc" {2: 1, 3: 2} -> True (rm key=1 (smaller, if smaller key=2 -> {1:1, 3:2}))

            "aaabbcc" {3: 1, 2: 2} -> True (rm key=3 (larger) -> {2:3})
            """
            f1, f2 = min(keys), max(keys)
            return (f1 == 1 and freq_cnter[f1] == 1) or (f2-f1==1 and freq_cnter[f2] == 1)

        return False

