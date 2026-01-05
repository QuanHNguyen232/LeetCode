class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        preSum = 0
        minPreSum = math.inf
        for num in nums:
            preSum += num
            minPreSum = min(minPreSum, preSum)

        if minPreSum <= 0:
            return abs(minPreSum) + 1
        else:
            return 1 # Minimum start value should be positive -> choose 1