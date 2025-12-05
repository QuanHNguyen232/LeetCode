class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        preSum = list(itertools.accumulate(nums))

        for i in range(n-1):
            left_sum = preSum[i]
            right_sum = preSum[-1] - preSum[i]
            ans = ans+1 if (left_sum - right_sum) % 2 == 0 else ans

        return ans