class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        """num1 = 3, num2 = 2
        times = 3//2 = 1
        ans += times
        num1 = 3-(2*times) = 1
        num1 = 2, num2 = 1

        times = 2//1 = 2
        ans += times
        num1 = 2-(1*times) = 0
        num1 = 1, num2 = 0
        """

        if num1 == 0 or num2 == 0:
            return 0
        
        ans = 0
        if num2 > num1: # always keep num1 bigger
            num1, num2 = num2, num1
        
        while not (num1==0 or num2==0):
            times = num1 // num2
            ans += times
            num1 -= num2*times

            if num2 > num1:
                num1, num2 = num2, num1

        return ans