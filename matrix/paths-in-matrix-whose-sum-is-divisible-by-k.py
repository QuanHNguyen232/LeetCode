class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        """DP
        dp[i][j][r] number of path to reach (i,j) with modulo of k=r (sum % k = r) with 0<=r<k

        return int(dp[-1][-1][0] % MOD)

        [5,2,4]           [2,2,1]
        [3,0,5] --> mod = [0,0,2] <=> given k=3
        [0,7,2]           [0,1,2]
        # init
        (0,0) -> dp[0][0][2]=1
        (0,1)
            -> update mod -> dp[]
            -> update count dp[0][1][ (prevMod+currMod)%k=(2+2)%3=1 ] = prev mod (dp[0][0][2])
        (0,2) -> dp[0][2][]
        """
        nrows = m = len(grid)
        ncols = n = len(grid[0])
        MOD = 1e9+7
        dp = [[[0]*k for _ in range(ncols)] for _ in range(nrows)]
        
        # base case
        dp[0][0][grid[0][0] % k] = 1
        
        # compute dp
        for i in range(nrows):
            for j in range(ncols):
                if i==0 and j==0: continue

                currMod = grid[i][j] % k

                # update dp
                for prevMod in range(k):
                    up_cnt = dp[i-1][j][prevMod] if i >= 1 else 0
                    left_cnt = dp[i][j-1][prevMod] if j >= 1 else 0
                    dp[i][j][(prevMod + currMod) % k] = (up_cnt + left_cnt) %MOD
        
        return int(dp[-1][-1][0])