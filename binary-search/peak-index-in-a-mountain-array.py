class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        """
        [0, 1, 2, 3, 4, 5]
        [0, 5, 6, 9, 2, 1]
         l     m        r
                  l  m  r
                  lrm
                  r  l --> l-1

        [0, 1, 2, 3, 4, 5]
        [0, 9, 6, 5, 2, 1]
         l     m        r
         lm r
            lrm
            r  l
        
        [1, 2, 3, 4, 5]
        [3, 5, 3, 2, 0]
         l  m        r
        """
        l = 1
        r = len(arr) - 1
        while l <= r:
            mid = l + (r-l)//2
            if arr[mid-1] < arr[mid]:
                l = mid + 1
            else:
                r = mid - 1

        return l-1