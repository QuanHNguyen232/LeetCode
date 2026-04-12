class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        cnter = defaultdict(list)
        for i, num in enumerate(nums): # O(n)
            cnter[num].append(i)
        
        res = float("inf")
        for num, indices in cnter.items():
            if len(indices) < 3:
                continue
            for idx in range(2, len(indices)):
                i, j, k = indices[idx-2], indices[idx-1], indices[idx]
                distance = abs(i-j) + abs(j-k) + abs(k-i)
                res = min(res, distance)

        return -1 if res==float("inf") else res