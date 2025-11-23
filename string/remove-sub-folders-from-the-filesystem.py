class TrieNode:
    def __init__(self):
        self.child = {}
        self.isEnd = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, s) -> None:
        curr = self.root
        for c in s:
            if c not in curr.child:
                curr.child[c] = TrieNode()
            curr = curr.child[c]
        curr.isEnd = True

    def is_subFolder(self, s) -> bool:
        curr = self.root
        for c in s:
            if curr.isEnd:
                return True
            if c not in curr.child:
                return False
            curr = curr.child[c]
        return curr.isEnd

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort() # ensure folder is added before subfolder
        ans = []
        trie = Trie()
        
        for f in folder:
            s = f.split("/")
            if len(s[0]) == 0:
                s = s[1:]

            if trie.is_subFolder(s):
                continue
            
            trie.insert(s)
            ans.append(f)
        
        return ans
