class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        ans = 0
        str_len = len(strs[0])

        def is_col_sorted(col):
            curr = strs[0][col]
            for row in strs[1:]:
                if curr > row[col]:
                    return False
            return True

        for col in range(str_len):
            if not is_col_sorted(col):
                ans += 1
        
        return ans