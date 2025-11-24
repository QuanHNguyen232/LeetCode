class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        ans = []
        DIVISOR = 5
        curr_num = 0
        for i in range(len(nums)):
            curr_num = (curr_num << 1) | nums[i]
            ans.append(curr_num % DIVISOR == 0)
        return ans