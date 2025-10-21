class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        
        ans = False
        sub_arr_idx = set()
        cnt_incr = 1
        for i in range(1, n):
            if nums[i-1] < nums[i]:
                cnt_incr += 1
                if cnt_incr >= k:
                    sub_arr_idx.add(i)
                    if i-k in sub_arr_idx:
                        return True
            else:
                cnt_incr = 1

        return ans