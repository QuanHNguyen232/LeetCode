class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        return self.sln2(nums)
        
    def sln2(self, nums: List[int]) -> int:
        n = len(nums)
        left_sum = 0
        right_sum = sum(nums)

        for index in range(n):
            right_sum -= nums[index]
            if index > 0:
                left_sum += nums[index - 1]

            if left_sum == right_sum:
                return index

        return -1

    def sln1(self, nums: List[int]) -> int:
        preSum = [nums[0]]
        for num in nums[1:]:
            preSum.append(preSum[-1] + num)

        if preSum[-1] - nums[0] == 0:
            return 0
        
        for pivot_idx in range(1, len(preSum) - 1):
            leftSum = preSum[pivot_idx - 1]
            rightSum = preSum[-1] - preSum[pivot_idx]
            if leftSum == rightSum:
                return pivot_idx
        
        if len(preSum)>1 and preSum[-2] == 0:
            return len(preSum) - 1
        
        return -1
        # time: O(n)
        # space: O(n)