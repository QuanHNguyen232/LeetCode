class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        return self.sln_2(s, t)

    def sln_2(self, s: str, t: str) -> bool: # O(1) space complexity
        class StrIterator:
            def __init__(self, s: str):
                self.idx = len(s) - 1
                self.s = s
                self.hash_count = 0

            def next(self):
                while self.idx >= 0:
                    if self.s[self.idx] == "#":
                        # increase skip_quota
                        self.hash_count += 1
                        self.idx -= 1
                    elif self.hash_count > 0:
                        # skip
                        self.hash_count -= 1
                        self.idx -= 1
                    else:
                        res = self.s[self. idx]
                        self.idx -= 1
                        return res
                return None

        iter1 = StrIterator(s)
        iter2 = StrIterator(t)
        while True:
            s_char = iter1.next()
            t_char = iter2.next()
            
            if s_char != t_char:
                return False
            if s_char is None and t_char is None:
                return True

        def sln_1(self, s: str, t: str) -> bool:
            # use stack, O(n) space complexity
            pass