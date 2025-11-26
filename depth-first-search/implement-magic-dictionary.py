class MagicDictionary:

    def __init__(self):
        self.original_dict = set()
        self.vocab_dict = defaultdict(set)

    def generate_masked_word(self, word: str) -> List[str]:
        masks = [word[:i] + "#" + word[i+1:] for i in range(len(word))]
        return masks
    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            self.original_dict.add(word)
            for masked_word in self.generate_masked_word(word):
                self.vocab_dict[len(masked_word)].add(masked_word)
        
        print(self.vocab_dict)

    def search(self, searchWord: str) -> bool:
        if searchWord in self.original_dict:
            return False
        masked_searchWords = self.generate_masked_word(searchWord)
        return any([masked_searchWord in self.vocab_dict[len(masked_searchWord)] for masked_searchWord in masked_searchWords])


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)