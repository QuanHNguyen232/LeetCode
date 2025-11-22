class Solution:
    def missingNumber(self, nums):
        # return self.bit(nums)
        return self.bsearch1(nums)

    def bsearch1(self, nums):
        """
        [0,1,2,3] (index)
        [0,1,2,3]
         l m   r
             l r
               lr -> out of loop
        """
        def condition(mid):
            return nums[mid]-nums[0] != mid

        nums.sort()
        if nums[0] != 0:
            return 0
        left = 0
        right = len(nums)-1
        
        while left < right:
            mid = left + (right - left) // 2 # lower bound
            if condition(mid):
                right = mid
            else:
                left = mid + 1 # otherwise causes infinite loop
        
        if left == nums[left]: # for [0,1] -> add 2
            return left+1
        return left


    def bit(self, nums):
        """
        missing
            =4 ∧ (0∧0) ∧ (1∧1) ∧ (2∧3) ∧ (3∧4)
            =(4∧4) ∧ (0∧0) ∧ (1∧1) ∧ (3∧3) ∧ 2
            =0 ∧ 0 ∧ 0 ∧ 0 ∧ 2
            =2
        """
        missing = len(nums)
        for i, num in enumerate(nums):
            missing ^= i ^ num
        
        return missing