class Solution:
    def minMoves(self, nums: List[int]) -> int:
        target = max(nums)
        ans = 0
        for num in nums:
            ans += target - num

        return ans