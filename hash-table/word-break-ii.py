class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        return self.sln_backtrack(s, wordDict)
        
    def sln_backtrack(self, s: str, wordDict: List[str]) -> List[str]:
        """
        "catsanddog" (n=10)
        check:
        - i=0 (s[:i+1]="c") -> continue
        - i=1 ("ca") -> continue
        - i=2 ("cat") -> in wordSet -> path.append("cat")
            -> backtrack(start=i+1=3, path=["cat"])
                - i=3 (s[start:i+1]="s") -> continue
                - i=4 ("sa") -> continue
                - i=5 ("san") -> continue
                - i=6 ("sand") -> in wordSet -> path.append("sand")
                    -> backtrack(start=i+1=7, path=["cat","sand"])
                        - i=7 (s[start:i+1]="d") -> continue
                        - i=8 ("do") -> continue
                        - i=9 ("dog") -> in wordSet -> path.append("dog")
                            -> backtrack(start=i+1=10, path=["cat","sand","dog"])
                                - start=len(s) -> save path
                            - path.pop() -> path=["cat","sand"]
                    - path.pop() -> path=["cat"]
            - path.pop() -> path=[]
        - i=3 ("cats") -> in wordSet -> path.append("cats")
            -> backtrack(start=i+1=4, path=["cats"])
                - i=4 (s[start:i+1]="a") -> continue
        """
        n = len(s)
        wordSet = set(wordDict)
        ans = []

        def backtrack(start, curr_path: List[str]):
            # base case
            if start == len(s):
                # save
                ans.append(' '.join(curr_path.copy()))
                return

            for i in range(start, n):
                if s[start:i+1] in wordSet:
                    curr_path.append(s[start:i+1])
                    backtrack(i+1, curr_path)
                    curr_path.pop()

        backtrack(0, [])
        return ans