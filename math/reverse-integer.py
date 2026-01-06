class Solution:
    def reverse(self, x: int) -> int:
        sign = 1 if x > 0 else -1
        rev = 0
        x = abs(x)

        while x > 0:
            mod = x % 10
            x = x // 10
            rev = rev * 10 + mod
            if rev > 2**31 - 1:
                return 0

        return sign * rev