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

        def can_split_half(pre_sum, start, end) -> set:
            """to find i and k. MUST: start < i,k < end
            start, end: inclusive
                for i: start = 0, end=j-1
                for k: start = j+1, end=n-1
            
            Note: must return all possible cases that can be splitted
            e.g: [1,2,-1,1,2,5,2,5,2], j = 5
            -> find 2 cases for i: i=2 (split_val=3) and i=3 (split_val=2)
            """
            ans = set()
            left_sum = 0
            if start > 0:
                right_sum = pre_sum[end] - pre_sum[start-1]
            else:
                right_sum = pre_sum[end]

            for i in range(start, end+1):
                right_sum -= nums[i]
                if i > start:
                    left_sum += nums[i - 1]

                if start < i < end and left_sum == right_sum:
                    ans.add(left_sum)
            return ans
        

        if n < 7: return False
        for j in range(n):
            # find if can find i that can split 0...j by half
            split_vals_i = can_split_half(pre_sum, 0, j-1)
            
            # find if can find k that can split j...n by half
            split_vals_k = can_split_half(pre_sum, j+1, n-1)
            
            if split_vals_i & split_vals_k:
                return True

        return False