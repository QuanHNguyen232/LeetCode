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
        if n < 7: return False
        pre_sum = list(itertools.accumulate(nums))

        def can_split_half(pre_sum, start, end):
            """
            start, end: inclusive
            """
            left_sum = 0
            right_sum = (pre_sum[end] - pre_sum[start-1]) if start > 0 else pre_sum[end]
            print("\t", (start, end), (left_sum, right_sum))
            for i in range(start, end):
                right_sum -= nums[i]print("\t\t", i)
                

                upper = 0
                lower = 0
                if upper == lower: return True
            return False
        
        for j in range(n):
            if not (3 <= j <= n-4): continue
            print(f"j={j}")
            can_find_i = can_split_half(pre_sum, 0, j-1)
            # find if can find i that can split 0...j by half
                # smallest i = 1 (s.t. can get sum(0, i-1)) and i+1 < j ==> j >= 3
            
            can_find_k = can_split_half(pre_sum, j+1, n-1)
            # find if can find k that can split j...n by half
                # largest k = n-2 (s.t. can get sum(k+1, n-1)) and j + 1 < k < n - 1 ==> j <= n-4


        return False