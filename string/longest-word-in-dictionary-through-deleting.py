class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        def is_subword(word1, word2) -> bool:
            """
            word2 is subword to word1
            """
            i = j = 0
            while i < len(word1) and j < len(word2):
                if word1[i] == word2[j]:
                    i+=1
                    j+=1
                else:
                    i += 1
            return j == len(word2)

        ans = ""
        for word in dictionary:
            if is_subword(s, word):
                if (
                    len(ans) < len(word) # if longer -> update
                    or (len(ans) == len(word) and word < ans) # if equal length and word smaller (lexicographical) -> update
                ):
                    ans = word
        return ans