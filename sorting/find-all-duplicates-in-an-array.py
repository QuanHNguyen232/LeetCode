class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans =[]
        # only work for positive numbers (1 <= nums[i] <= n and 1 <= n <= 10^5)
        for x in nums:
            x = abs(x)

            # x was visited before as index=x-1 is marked as negative for visietd
            # --> x is duplicated
            if nums[x-1] < 0:
                ans.append(x)
            
            # mark index x-1 as visited x value
            nums[x-1] *= -1
        
        return ans