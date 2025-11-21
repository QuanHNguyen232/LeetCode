class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        [1,2,5,4,3,3]
        replace_idx1 = 1 (num=2)
        replace_idx2 = 5 (num=3)
        swap: [1,3,5,4,3,2]
        reverse: [1,3,2,3,4,5]

        [1,3,2,3,4,5].next = [1,3,2,3,5,4]
        [1,3,2,3,5,4].next = [1,3,2,4,3,5]
        """
        n = len(nums)
        replace_idx1 = None
        for i in range(n-2, -1, -1):
            if nums[i] < nums[i+1]:
                replace_idx1 = i
                break

        def reverse_in_place(nums, start):
            l, r = start, len(nums)-1
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l+=1
                r-=1

        if replace_idx1 is None:
            # the arr is non-increasing --> reverse
            reverse_in_place(nums, 0)
        else:
            # find replace_idx2, the next number that larger than replace_idx1
            replace_idx2 = n - 1
            while nums[replace_idx2] <= nums[replace_idx1]:
                replace_idx2 -= 1
            # swap
            nums[replace_idx1], nums[replace_idx2] = nums[replace_idx2], nums[replace_idx1]
            # after swap, it remains reversed --> reverse
            reverse_in_place(nums, replace_idx1+1)
