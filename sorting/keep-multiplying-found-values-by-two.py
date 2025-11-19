class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        nums_set = set(nums)
        ans = original
        while ans in nums_set:
            ans *= 2
        return ans
