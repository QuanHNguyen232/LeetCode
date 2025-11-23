class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        max_val = max(nums)
        min_val = min(nums)
        max_smallest_range = max_val-k
        min_largest_range = min_val+k
        if max_smallest_range<=min_largest_range:
            return 0
        return max_smallest_range - min_largest_range