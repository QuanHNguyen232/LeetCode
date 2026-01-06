class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visited = set()
        left = 0
        res = 0

        for right in range(len(s)):
            c = s[right]

            # step 2
            while c in visited and left < right:
                visited.remove(s[left])
                left += 1

            # step 3
            visited.add(s[right])
            res = max(res, right - left + 1)
        
        return res