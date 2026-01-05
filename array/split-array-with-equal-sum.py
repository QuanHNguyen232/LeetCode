class Solution:
    def splitArray(self, nums: List[int]) -> bool:
        '''
        targetSum must be <= (total//3)

        index= [0,1,2,3,4,5, 6], n=7
        nums = [1,2,1,2,1,2, 1]
        preSum=[1,3,4,6,7,9,10]
                  i   j   k
        what we want:
        preSum[i-1] = preSum[j-1]-preSum[i] = preSum[k-1]-preSum[j] = preSum[n-1]-preSum[k]
        '''
        n = len(nums)
        total = sum(nums)
        pre_sum = list(itertools.accumulate(nums))

        def can_split_half(pre_sum, start, end):
            """
            start, end: inclusive
            """
            left_sum = 0
            right_sum = (pre_sum[end] - pre_sum[start-1]) if start > 0 else pre_sum[end]
            # print("\t", (start, end), (left_sum, right_sum))
            for i in range(start, end):
                right_sum -= nums[i]
                if i > start:
                    left_sum += nums[i - 1]
                # print(f"\t\ti={i}, left_sum={left_sum}, right_sum={right_sum}")
                if left_sum == right_sum:
                    return i, left_sum
            return -1, 0
        

        if n < 7: return False
        for j in range(n):
            if not (3 <= j <= n-4):
                # smallest i = 1 (s.t. can get sum(0, i-1)) and i+1 < j ==> j >= 3
                # largest k = n-2 (s.t. can get sum(k+1, n-1)) and j + 1 < k < n - 1 ==> j <= n-4
                continue

            # print(f"j={j}")

            # find if can find i that can split 0...j by half
            idx_i, split_val_i = can_split_half(pre_sum, 0, j-1)
            
            # find if can find k that can split j...n by half
            idx_k, split_val_k = can_split_half(pre_sum, j+1, n-1)
            
            # print(f"find i={(idx_i, split_val_i)}, k={(idx_k, split_val_k)}")

            if idx_i != -1 and idx_k != -1 and split_val_i == split_val_k:
                return True

        return False