class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        """
        [0, 1, 2, 3, 4, 5]
        [5, 9, 6, 3, 2, 0]
         l     m        r
         l  m  r
               lr

        [0, 1, 2, 3, 4, 5]
        [1, 2, 5, 6, 9, 2]
         l     m        r
                  l  m  r
                        lr

        [0, 1, 2, 3, 4, 5]
        [3, 4, 5, 2, 1, 0]
         l     m        r
                  l  m  r
                  lr
        """
        l = 1
        r = len(arr) - 1
        while l < r:
            mid = l + (r-l)//2
            if arr[mid-1] >= arr[mid]:
                r = mid
            else:
                l = mid + 1

        return l-1

        # while l <= r:
        #     mid = l + (r-l)//2
        #     if arr[mid-1] < arr[mid]:
        #         l = mid + 1
        #     else:
        #         r = mid - 1

        # return l-1