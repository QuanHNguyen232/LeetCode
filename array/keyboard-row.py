class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        char2row = {} # O(1) -> at most 26 characters
        char2row.update({
            char: 0 for char in list("qwertyuiop")
        })
        char2row.update({
            char: 1 for char in list("asdfghjkl")
        })
        char2row.update({
            char: 2 for char in list("zxcvbnm")
        })
        

        ans = []
        for word in words:
            word_tmp = word.lower()
            rowIdx = char2row[word_tmp[0]]
            if all([rowIdx == char2row[c] for c in word_tmp]):
                ans.append(word)

        return ans