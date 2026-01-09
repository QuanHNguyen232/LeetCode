class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # return self.sln_mergeSort(nums1, nums2)
        return self.sln_twoPtr(nums1, nums2)
    
    def sln_twoPtr(self, nums1: List[int], nums2: List[int]) -> float:
        """
        time: O(m+n)
        space: O(1)
        """
        m, n = len(nums1), len(nums2)
        total_len = m + n
        if total_len % 2 == 1:
            med_idx1 = med_idx2 = (total_len + 1) // 2
        else:
            med_idx1 = total_len // 2
            med_idx2 = med_idx1 + 1

        ptr1 = ptr2 = 0
        curr_med = 0
        med1, med2 = None, None
        while ptr1 < m and ptr2 < n:
            curr_med += 1
            if nums1[ptr1] <= nums2[ptr2]:
                if curr_med == med_idx1:
                    med1 = nums1[ptr1]
                elif curr_med == med_idx2:
                    med2 = nums1[ptr1]
                ptr1 += 1
            else:
                if curr_med == med_idx1:
                    med1 = nums2[ptr2]
                elif curr_med == med_idx2:
                    med2 = nums2[ptr2]
                ptr2 += 1
        
        ptr = ptr1 if ptr1 < m else ptr2
        lim = m if ptr1 < m else n
        nums = nums1 if ptr1 < m else nums2
        while (med1 is None or med2 is None) and ptr < lim:
            curr_med += 1
            if curr_med == med_idx1:
                med1 = nums[ptr]
            elif curr_med == med_idx2:
                med2 = nums[ptr]
            ptr += 1
        return med1 if total_len % 2 == 1 else (med1 + med2) / 2

        
    def sln_mergeSort(self, nums1: List[int], nums2: List[int]) -> float:
        """
        time: O(m+n)
        space: O(m+n)
        """
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