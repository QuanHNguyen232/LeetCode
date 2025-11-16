class Solution:
    def numSub(self, s: str) -> int:
        # return self.count1(s)
        return self.count2(s)

    def count1(self, s:str)->int:
        """Math-based
        """
        ans = 0
        MOD = 1e9+7

        for ones in s.split("0"):
            L = len(ones)
            ans = (ans + L*(L+1)//2) % MOD
        
        return int(ans)
    
    def count2(self, s:str)->int:
        """Count-based
        """
        ans = 0
        MOD = 1e9 + 7
        curr_cnt = curr_consecutive_ones = 0

        for i in range(len(s)):
            curr = s[i]
            if curr == "1":
                curr_consecutive_ones += 1
                curr_cnt += curr_consecutive_ones
            else: # if see "0"
                ans = (ans + curr_cnt) % MOD
                curr_cnt = curr_consecutive_ones = 0

        # if last curr="1" --> must add the rest to ans
        ans = (ans + curr_cnt) % MOD

        return int(ans)