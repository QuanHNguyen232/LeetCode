class Solution:
    def search(self, nums: List[int], target: int) -> int:

        print(self.upper_bound([0, 1, 1, 2, 2, 3], 2))

        return self.lower_bound(nums, target)

    def lower_bound(self, nums: List[int], target: int) -> int:
        """
        [-1,0,3,5,9,12], 9
        [ 0,1,2,3,4, 5]
        0,5 => 2 (val 2 < 9) -> move left (=mid+1)
        3,5 => 4 (val 9 = 9) -> move right (=mid)
        """
        n = len(nums)
        left = 0
        right = n-1

        # Search Space is at least 2 ==> if Search Space == 1 -> need post-process
        while left < right:
            mid = left + (right-left)//2
            if target <= nums[mid]: # mid works
                right = mid
            else:
                left = mid + 1
        
        # post-process (case search space = 1)
        # since we escape loop, left = right
        if nums[left] == target:
            return left
        return -1

    def upper_bound(self, nums: List[int], target: int) -> int:
        """
        [0, 1, 1, 1, 2, 2, 2, 2, 3], 1
        [0, 1, 2, 3, 4, 5, 6, 7, 8]
        0,8 => 4 (val 2 > 1) -> move right (=mid-1)
        0,3 => 2 (val 1 = 1) -> move left (=mid)
        """
        n = len(nums)
        left = 0
        right = n-1

        # Search Space is at least 2 ==> if Search Space == 1 -> need post-process
        while left < right:
            mid = right - (right-left)//2
            if target < nums[mid]:
                right = mid - 1
            else:
                left = mid

        # post-process (case search space = 1)
        # since we escape loop, left = right
        if nums[left] == target:
            return left
        return -1