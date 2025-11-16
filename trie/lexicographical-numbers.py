class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        trie = Trie()
        for i in range(1, n+1):
            trie.insert(str(i))

        return trie.get_lexical_order()

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False
class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.lexical_order = []
    
    def insert(self, num_str: str) -> None:
        curr = self.root
        for c in num_str:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.isEndOfWord = True

    
    def search(self, num_str: str) -> bool:
        curr = self.root
        for c in num_str:
            if c not in curr.children: return False
            curr = curr.children[c]
        return curr.isEndOfWord
    
    def get_lexical_order(self) -> List[int]:
        # get strs (similar to get path from root->all leaves => backtrack) and add to ans
        self.lexical_order = []
        self.dfs_backtrack(self.root, 0)
        return self.lexical_order

    def dfs_backtrack(self, curr: TrieNode, currVal: int) -> List[int]:
        if curr.isEndOfWord:
            self.lexical_order.append(currVal)
        
        for v, child in curr.children.items():
            newVal = currVal*10 + int(v)
            self.dfs_backtrack(child, newVal)


