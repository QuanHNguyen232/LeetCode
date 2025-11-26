class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        len1 = len(nums1)
        len2 = len(nums2)

        if len2 > len1: return self.intersect(nums2, nums1)
        cnter2 = Counter(nums2)
        ans = []
        for num in nums1:
            if num in cnter2:
                ans.append(num)
                cnter2[num] -= 1
                if cnter2[num] == 0: del cnter2[num]
        
        return ans