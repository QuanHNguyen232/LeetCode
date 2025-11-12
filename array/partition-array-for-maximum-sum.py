class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        """
        [1,15,7,9,2,5,10], k=3, len_arr=7
        
        # From solution
        for each start from 6->0
        for start=4 (compute dp[4])
        case i=4: [1,15,7,9,[2],5,10] -> currMax=2, currSum = 2*1 + dp[5]
        for start=3
        case i=3: [1,15,7,[9],2,5,10] -> currMax=9, currSum = currMax*1 + dp[4]
        case i=4: [1,15,7,[9,2],5,10] -> currMax=9, currSum = currMax*2 + dp[5] (dp of the rest [5,10])
        case i=5: [1,15,7,[9,2,5],10] -> currMax=9, currSum = currMax*3 + dp[6] (dp of the rest [10])
        --> dp[i] = max(
            currMax*(j-i+1) for each j from [i->len_arr-1]
        )

        # My solution
        for each start from 0->6
        dp = [0] * (len_arr+1) --> return dp[len_arr-1] (using this, dp[-1] = 0)
        if start=0 (compute dp[0])
        dp[0] = arr[0]
        if start=1 (compute dp[1])
        case i=1: [1,[15],7,9,2,5,10] -> currMax = 15, currSum = 15*1 + dp[0]
        case i=0: [[1,15],7,9,2,5,10] -> currMax = 15, currSum = 15*2 + dp[i-1] (if i < 0 --> 0)
        if start=2 (compute dp[2] = max(all currSum for i from start->start-k) )
        case i=2: [1,15,[7],9,2,5,10] -> currMax = 7, currSum = 7*1 + dp[1] (currMax*(start-i+1) + dp[i-1])
        case i=1: [1,[15,7],9,2,5,10] -> currMax = 15, currSum = 15*2 + dp[0]
        case i=0: [[1,15,7],9,2,5,10] -> currMax = 15, currSum = 15*3 + dp[-1]
        if start=3 (compute dp[3])
        case i=3: [1,15,7,[9],2,5,10] -> currMax = 9, currSum = 9*1 + dp[2]
        case i=2: [1,15,[7,9],2,5,10] -> currMax = 9 (compare last currMax w/ current arr[i]), currSum = 9*2 + dp[1]
        case i=1: [1,[15,7,9],2,5,10] -> currMax = 15, currSum = 15*3 + dp[0]

        dp[i]: largest sum of the given array after partitioning for array arr[0] -> arr[i-1]
        dp[i] = max(
            max(arr[j:i+1])*len_subarr + dp[j-1]
        )
        """
        n = len(arr)
        dp = [0]*(n+1)
        dp[0] = arr[0]

        for start in range(1, n):
            currMax = -math.inf
            end = max(start-k, -1)
            for i in range(start, end, -1):
                currMax = max(currMax, arr[i])
                currSum = currMax*(start-i+1) + dp[i-1]
                dp[start] = max(dp[start], currSum)
            
        return dp[n-1]