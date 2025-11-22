class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        chars = list(''.join(s.split('-')).upper())
        
        ans = []
        cnt = 0
        curr = []
        for i in range(len(chars)-1, -1, -1):
            cnt += 1
            curr.append(chars[i])
            if cnt % k == 0:
                ans.append(''.join(curr[::-1]))
                curr = []
                cnt = 0

        if curr:
            ans.append(''.join(curr[::-1]))

        return "-".join(ans[::-1])