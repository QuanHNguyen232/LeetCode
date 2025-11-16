class Solution:
    def numSub(self, s: str) -> int:
        return self.count1(s)

    def count1(self, s:str)->int:
        ans = 0
        MOD = 1e9+7
        for ones in s.split("0"):
            L = len(ones)
            ans += L*(L+1)//2
            ans %= MOD
        
        return int(ans)
    
    def count2(self, s:str)->int:
        pass