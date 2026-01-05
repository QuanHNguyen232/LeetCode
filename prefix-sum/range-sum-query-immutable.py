class NumArray:

    def __init__(self, nums: List[int]):
        self.preSum = list(itertools.accumulate(nums))

    def sumRange(self, left: int, right: int) -> int:
        upper = self.preSum[right]
        lower = self.preSum[left-1] if left > 0 else 0

        return upper - lower


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)