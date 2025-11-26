class Solution:
    def convertToBase7(self, num: int) -> str:
        BASE = 7
        ans = []
        sign = num // abs(num)
        num = abs(num)
        while num != 0:
            ans.append(str(num % BASE))
            num //= BASE
        
        if sign < 0:
            ans.append("-")
            
        return ''.join(ans[::-1])