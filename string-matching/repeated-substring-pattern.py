class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        for i in range(1, n // 2 + 1):
            substr = s[:i]
            if n % len(substr) ==0:
                new_s = substr * (n // len(substr))
                if s==new_s:
                    return True

        return False