class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        memo = {1:0}

        def getPower(val):
            if val not in memo:
                if val % 2 == 0:
                    memo[val] = getPower(val //2) + 1
                else:
                    memo[val] = getPower(val*3 +1) + 1
            
            return memo[val]
        
        nums = [i for i in range(lo, hi+1)]
        nums.sort(key=lambda val: [getPower(val), val])

        return nums[k-1]