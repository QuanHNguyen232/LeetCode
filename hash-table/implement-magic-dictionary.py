class MagicDictionary:

    def __init__(self):
        self.word_set = set()
        self.counter = Counter()

    def generate_masked_word(self, word: str) -> List[str]:
        masks = [word[:i] + "#" + word[i+1:] for i in range(len(word))]
        return masks

    def buildDict(self, dictionary: List[str]) -> None:
        self.word_set = self.word_set.union(set(dictionary))
        self.counter.update(Counter(nei for word in dictionary for nei in self.generate_masked_word(word)))
        
    def search(self, searchWord: str) -> bool:
        """
        e.g. 
        if count[h#llo]=2 (from "hallo" and "hello")
        --> searchWord="hello" -> True as it can be generated from "hallo"
        
        if count[h#llo]=1 (from "hello" only)
        --> searchWord="hello" (in word_set) -> False as it can not be itself
        --> searchWord="hallo" (not in word_set) -> True
        """
        for nei in self.generate_masked_word(searchWord):
            if (
                (self.counter[nei] > 1)
                or (self.counter[nei] == 1 and searchWord not in self.word_set)
            ):
                return True

        return False


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)