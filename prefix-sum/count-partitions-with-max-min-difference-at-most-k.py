class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        """
        [9,4,1,3,7]
        [9]: 1
        [9, 4]: 1
        [9, 4, 1]: 2 ([9]: 1 + [4,1]: 2)
        [9, 4, 1, 3]: 4 ([9]: 1 + [4,1,3]:3)
        [9, 4, 1, 3, 7]: 6 ([9]: 1 + [4,1,3]:3 + [3,7]: 2)

        dp[i]: num of ways for items 0...i (inclusive)
        dp[i] = (
            . if nums[i] make max-min<=k -> dp[i-1] + 1
            . if nums[i] make invalid -> dp[i-1]
            with max, min are monotonic stacks
        )
        """
        n = len(nums)
        MOD = 10**9 + 7
        dp = [0] * (n + 1)
        prefix = [0] * (n + 1)
        min_q = deque()
        max_q = deque()

        dp[0] = 1
        prefix[0] = 1
        j = 0


        for i in range(n):
            # maintain the maximum value queue
            while max_q and nums[max_q[-1]] <= nums[i]:
                max_q.pop()
            max_q.append(i)

            # maintain the minimum value queue
            while min_q and nums[min_q[-1]] >= nums[i]:
                min_q.pop()
            min_q.append(i)

            # adjust window: increase left until max-min <= k
            while max_q and min_q and nums[max_q[0]] - nums[min_q[0]] > k:
                if max_q[0] == j:
                    max_q.popleft()
                if min_q[0] == j:
                    min_q.popleft()
                j += 1

            if j > 0:
                dp[i + 1] = (prefix[i] - prefix[j - 1]) % MOD
            else:
                dp[i + 1] = prefix[i] % MOD
            
            prefix[i + 1] = (prefix[i] + dp[i + 1]) % MOD

        return dp[n]