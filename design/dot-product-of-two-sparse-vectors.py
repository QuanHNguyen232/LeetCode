class SparseVector:
    def __init__(self, nums: List[int]):
        # sln1: can use hashmap, but depending on implementation (and memory location)
        # --> using list of tuple or parallel list is preferred
        self.indices = []
        self.vals = []
        for i, num in enumerate(nums):
            if num != 0:
                self.indices.append(i)
                self.vals.append(num)
    
    def __len__(self) -> int:
        return len(self.indices)

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        res = 0
        i, j = 0, 0
        while i < len(self) and j < len(vec):
            if self.indices[i] == vec.indices[j]:
                res += self.vals[i] * vec.vals[j]
                i += 1
                j += 1
            elif self.indices[i] < vec.indices[j]:
                # Advance i using binary search (instead of i += 1)
                i = bisect.bisect_left(self.indices, vec.indices[j], lo=i+1)
            else:
			    # Advance j using binary search (instead of j += 1)
                j = bisect.bisect_left(vec.indices, self.indices[i], lo=j+1)
        return res


# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)