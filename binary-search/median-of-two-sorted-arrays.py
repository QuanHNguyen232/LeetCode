class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # return self.sln_mergeSort(nums1, nums2)
        return self.sln_twoPtr(nums1, nums2)
    
    def sln_twoPtr(self, nums1: List[int], nums2: List[int]) -> float:
        verbose = 0

        m, n = len(nums1), len(nums2)
        total_len = m + n
        if total_len % 2 == 1:
            med_idx1 = med_idx2 = (total_len + 1) // 2
        else:
            med_idx1 = total_len // 2
            med_idx2 = med_idx1 + 1

        print(f"med_idx1={med_idx1}, med_idx2={med_idx2}")
        ptr1 = ptr2 = 0
        curr_med = 0
        med1, med2 = None, None
        while ptr1 < m and ptr2 < n:
            if verbose: print(f"curr_med: ptr1:{ptr1}, ptr2:{ptr2}; med1:{med1}, med2:{med2}")
            if nums1[ptr1] <= nums2[ptr2]:
                curr_med += 1
                if curr_med == med_idx1:
                    if verbose: print(f"\tfound curr_med == med_idx1 ({curr_med}),  med1={nums1[ptr1]}")
                    med1 = nums1[ptr1]
                elif curr_med == med_idx2:
                    if verbose: print(f"\tfound curr_med == med_idx2 ({curr_med}),  med2={nums1[ptr1]}")
                    med2 = nums1[ptr1]
                ptr1 += 1
            else:
                curr_med += 1
                if curr_med == med_idx1:
                    if verbose: print(f"\tfound curr_med == med_idx1 ({curr_med}),  med1={nums2[ptr2]}")
                    med1 = nums2[ptr2]
                elif curr_med == med_idx2:
                    if verbose: print(f"\tfound curr_med == med_idx2 ({curr_med}),  med2={nums2[ptr2]}")
                    med2 = nums2[ptr2]
                ptr2 += 1
        
        if ptr1 < m:
            if verbose: print(f"continue ptr=ptr1={ptr1}")
            ptr, lim, nums = ptr1, m, nums1
        else:
            if verbose: print(f"continue ptr=ptr2={ptr2}")
            ptr, lim, nums = ptr2, n, nums2
        while (med1 is None or med2 is None) and ptr < lim:
            curr_med += 1
            if curr_med == med_idx1:
                med1 = nums[ptr]
            elif curr_med == med_idx2:
                med2 = nums[ptr]
            ptr += 1
        if verbose: print(f"\tmed1={med1}, med2={med2}")
        return med1 if total_len % 2 == 1 else (med1 + med2) / 2

        
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