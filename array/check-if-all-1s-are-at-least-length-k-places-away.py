class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        last_one_idx = -math.inf
        for i in range(n):
            if nums[i] == 1:
                if i - last_one_idx - 1 < k:
                    return False
                last_one_idx = i
        
        return True