class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # return self.sln1(nums1, nums2)
        return self.sln2(nums1, nums2)
    
    def sln2(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()

        N = len(nums1)
        M = len(nums2)
        p1 = 0
        p2 = 0
        intersection = set()

        while p1 < N and p2 < M:
            if nums1[p1] == nums2[p2]:
                intersection.add(nums1[p1])
                p1 += 1
                p2 += 1
            elif nums1[p1] < nums2[p2]:
                p1 += 1
            else:
                p2 += 1

        return list(intersection)
    
    def sln1(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)
        return list(set2 & set1)