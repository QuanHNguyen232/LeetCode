class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        [-1,0,3,5,9,12]
        [ 0,1,2,3,4, 5]
        0,5 => 2 (val 2 < 9) -> move left
        3,5 => 4 (val 9 = 9) -> move right

        """
        left = 0
        right = len(nums) - 1

        while left < right: # Search Space is at least 2 ==> if Search Space == 1 -> need post-process
            mid = left + (right-left)//2
            if nums[mid] >= target: # mid works
                right = mid
            else:
                left = mid + 1
        
        # post-process (case search space = 1)
        # since we escape loop, left = right
        if nums[left] == target:
            return left
        return -1