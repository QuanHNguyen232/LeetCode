class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        trie = Trie()
        for word in strs:
            trie.insert(word)
        return trie.lcs()

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        current = self.root
        for c in word:
            if c not in current.children:
                current.children[c] = TrieNode()
            current = current.children[c]
        current.isEndOfWord = True

    def lcs(self):
        ans = []
        current = self.root
        while current:
            if len(current.children) > 1 or current.isEndOfWord:
                break
            else:
                key = list(current.children.keys()) # there is only 1 child (len(key) = 1)
                ans.append(key[0])
                current = current.children.get(key[0])
        
        return ''.join(ans)