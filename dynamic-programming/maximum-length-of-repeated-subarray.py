class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        """
        i: subarr of nums1[:i+1]
        j: subarr of nums2[:j+1]
        dp[i][j]: max len of subarr of nums2 in nums1

        """
        # nums1 alway longer
        if len(nums1) < len(nums2):
            nums1, nums2 = nums2, nums1

        n = len(nums1)
        m = len(nums2)
        dp = [[0]*(m) for _ in range(n)]
        
        def isInBound(i1, i2):
            return (0<=i1<n) and (0<=i2<m)

        # init dp
        ans = 1
        for i1 in range(n):
            for i2 in range(m):
                if nums1[i1] == nums2[i2]:
                    dp[i1][i2] += 1
                    if isInBound(i1-1, i2-1) and nums1[i1-1] == nums2[i2-1]:
                        dp[i1][i2] = max(dp[i1][i2], dp[i1-1][i2-1]+1)
                        ans = max(ans, dp[i1][i2])



        # for row in dp: print(row)



        return ans