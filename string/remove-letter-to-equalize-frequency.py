class Solution:
    def equalFrequency(self, word: str) -> bool:
        cnter = Counter(word)

        freq_cnter = Counter([count for char, count in cnter.items()])
        keys = list(freq_cnter.keys())
        if len(keys) == 2 and abs(freq_cnter[keys[0]] - freq_cnter[keys[1]]) == 1:
            return True
        
        return False