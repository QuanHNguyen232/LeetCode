class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s2t = {}
        t2s = {}
        for char_s, char_t in zip(s, t):
            if char_s not in s2t and char_t not in t2s:
                s2t[char_s] = char_t
                t2s[char_t] = char_s
            else:
                # case 1: a -> b and a -> c ==> False
                if char_s in s2t:
                    char_curr = s2t[char_s]
                    if char_curr != char_t:
                        return False
                # case 2: a -> c and b -> c ==> False
                else:
                    char_curr = t2s[char_t]
                    if char_curr != char_s:
                        return False
        return True