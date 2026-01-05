class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        return self.sln2(nums)

    def sln2(self, nums: List[int]) -> List[int]:
        ans = []

        # left_product: left -> right (except itself)
        currProduct = 1
        for i in range(len(nums)):
            ans.append(currProduct)
            currProduct *= nums[i]

        # right_product: right -> left (except itself)
        currProduct = 1
        for i in range(len(nums)-1, -1, -1):
            ans[i] *= currProduct
            currProduct *= nums[i]

        return ans
        # time: O(n): takes O(2n) to compute prefix and suffix
        # space: O(1): does not include ans

    def sln1(self, nums: List[int]) -> List[int]:
        # Similar to Prefix sum, we compute prefix product and suffix product
        leftProd = [nums[0]]
        for num in nums[1:]:
            leftProd.append(leftProd[-1] * num)
        # print(leftProd)

        rev_nums = nums[::-1] # [4,3,2,1]
        rightProd = [0] * len(nums)
        rightProd[0] = rev_nums[0] # [4,0,0,0]
        for i, num in enumerate(rev_nums[1:]):
            rightProd[i+1] = rightProd[i] * num
        rightProd = rightProd[::-1]
        # print(rightProd)

        ans = [rightProd[0+1]]
        
        for i in range(1, len(nums) - 1):
            val = leftProd[i - 1] * rightProd[i + 1]
            ans.append(val)
        
        ans.append(leftProd[-1 - 1])

        return ans
        # time: O(n): takes O(n) to compute prefix and suffix, and O(n) to compute each index in ans
        # space: O(n): space for prefix, suffix --> O(2n)