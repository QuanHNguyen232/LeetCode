class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        n = len(nums)
        preSum = 0
        res = n
        total = sum(nums)
        target = total % p
        hashmap = {0:-1} # new practice: at idx=0, set -1 so that get len i-hashmap == i+1 when preSum=0
        
        if target == 0: return 0

        for i in range(n):
            preSum = (preSum + nums[i]) % p

            remain = (preSum - target) % p
            if remain in hashmap:
                res = min(res, i - hashmap[remain])

            # always update for shortest subarray
            hashmap[preSum] = i

        return res if res != n else -1