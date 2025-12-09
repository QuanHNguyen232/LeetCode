class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        cnter = Counter(s)
        cnt_odd = 0
        for k, v in cnter.items():
            if v % 2 != 0:
                cnt_odd += 1

        return cnt_odd <= 1

