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
        verbose = False
        MOD = 1e9+7
        dp = [[[0]*k for _ in range(ncols)] for _ in range(nrows)]
        
        def debug():
            if not verbose: return
            for r in grid: print(r)
            for r in dp: print(r)
            print('-'*20)
        
        # init
        dp[0][0][grid[0][0] % k] = 1
        # by 0-row
        for j in range(1, ncols):
            currMod = grid[0][j] % k
            # grid[0][j] = (grid[0][j] + grid[0][j-1]) % k # for debug only
            for prevMod in range(k):
                prev_cnt = dp[0][j-1][prevMod]
                new_mod = (prevMod + currMod) % k
                dp[0][j][new_mod] = prev_cnt %MOD
                if verbose: print(f"col={j}, prevMod={prevMod}, prev_cnt={prev_cnt}, new_mod={new_mod}")
        debug()
        # by 0-col
        for i in range(1, nrows):
            currMod = grid[i][0] % k
            # grid[i][0] = (grid[i][0] + grid[i-1][0]) % k # for debug only
            for prevMod in range(k):
                prev_cnt = dp[i-1][0][prevMod]
                new_mod = (prevMod + currMod) % k
                dp[i][0][new_mod] = prev_cnt %MOD
                if verbose: print(f"row={i}, prevMod={prevMod}, prev_cnt={prev_cnt}, new_mod={new_mod}")
        debug()
        
        # compute dp
        for i in range(1, nrows):
            for j in range(1, ncols):
                currMod = grid[i][j] % k
                # grid[i][j] = (grid[i][j] + grid[i-1][j] + grid[i][j-1]) % k # for debug only
                if verbose: print(f"r={i}, c={j}, currMod={currMod}")
                # update dp
                for prevMod in range(k):
                    up_cnt = dp[i-1][j][prevMod]
                    left_cnt = dp[i][j-1][prevMod]
                    new_mod = (prevMod + currMod) % k
                    dp[i][j][new_mod] = (up_cnt + left_cnt) %MOD
                    if verbose: print(f"r={i}, c={j}, prevMod={prevMod}, up_cnt={up_cnt}, left_cnt={left_cnt}, prev_cnt={up_cnt + left_cnt}, new_mod={new_mod}")
        debug()
        
        return int(dp[-1][-1][0] % MOD)