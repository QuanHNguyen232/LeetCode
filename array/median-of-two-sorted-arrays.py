class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        return self.sln_mergeSort(nums1, nums2)
    
    def sln_mergeSort(self, nums1: List[int], nums2: List[int]) -> float:
        def merge(nums1, nums2):
            m, n = len(nums1), len(nums2)
            ans = []
            p1 = p2 = 0
            while p1 < m and p2 < n:
                if nums1[p1] <= nums2[p2]:
                    ans.append(nums1[p1])
                    p1 += 1
                else:
                    ans.append(nums2[p2])
                    p2 += 1
            if p1 < m:
                p2 = p1
                n = m
                nums2 = nums1
            while p2 < n:
                ans.append(nums2[p2])
                p2 += 1
            return ans
        arr = merge(nums1, nums2)
        
        n = len(arr)
        if n % 2 != 0:
            return arr[n // 2]
        return (arr[(n // 2) - 1] + arr[n // 2]) / 2.0