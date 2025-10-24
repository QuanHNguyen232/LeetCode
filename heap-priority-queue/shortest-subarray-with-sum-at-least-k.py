class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        res = math.inf
        preSum = 0
        l = 0
        n = len(nums)

        for r in range(n):
            preSum += nums[r]

            while preSum >= k:
                res = min(res, r-l+1)
                preSum -= nums[l]
                l+=1

        return -1 if res==math.inf else res