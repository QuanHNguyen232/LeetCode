class TrieNode:
    def __init__(self):
        self.child = {}
        self.sentences = defaultdict(int)

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word, freq):
        curr = self.root
        for c in word:
            if c not in curr.child:
                curr.child[c] = TrieNode()
            curr = curr.child[c]
            curr.sentences[word] += freq

    def search(self, keyword: Union[List[str], str]) -> List[Tuple[str, int]]:
        curr = self.root
        for c in keyword:
            if c not in curr.child:
                return []
            curr = curr.child[c]
        
        ans = list(curr.sentences.items())
        # self.dfs(curr)
        # self.backtrack(ans, curr, path=[])

        return ans
    
    def backtrack(self, ans, curr: TrieNode, path: List[str]):
        # base
        if curr.countEnd:
            ans.append((curr.countEnd, ''.join(path)))
        # recursion
        for next_char in curr.child:
            self.backtrack(ans, curr.child[next_char], path+[next_char])

    # def dfs(self, curr)-> List[str]:
    #     ans = []
    #     # backtrack
    #     def backtrack(ans, curr, path: List[str]):
    #         # base
    #         if curr.countEnd:
    #             ans.append((curr.countEnd, ''.join(path)))
    #         # recursion
    #         for next_char in curr.child:
    #             backtrack(ans, curr.child[next_char], path+[next_char])
    #     backtrack(curr, [])
    #     return ans
    
    def __str__(self):
        ans = self.search("")
        return '\n'.join(f"cnt:{cnt}, s={s}" for s, cnt in ans)

class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.LIMIT = 3
        self.curr_search = []
        self.trie = Trie()
        for sent, freq in zip(sentences, times):
            self.trie.insert(sent, freq)

        # print(self.trie)

    def input(self, c: str) -> List[str]:
        if c == "#":
            curr_sentence = "".join(self.curr_search)
            self.trie.insert(curr_sentence, 1)
            self.curr_search = []
            return []
        
        self.curr_search.append(c)
        keyword = "".join(self.curr_search)
        matches = self.trie.search(keyword)
        matches.sort(key=lambda x: [-x[1], x[0]])
        # print(f"curr_search={self.curr_search}, {matches}")
        ans = matches[:self.LIMIT]
        return [sent for sent, cnt in ans]


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)