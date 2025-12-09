class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        # return self.sln1(nums)
        return self.sln2(nums)

    def sln1(self, nums: List[int]) -> List[str]:
        if not nums: return []
        curr_range = nums[0]
        ans = [str(curr_range)]
        
        for i, num in enumerate(nums[1:] + [math.inf]):
            if curr_range+1 != num:
                new_str = ans.pop()
                curr = str(curr_range)
                new_str = new_str + "->" + curr if new_str != curr else new_str
                ans.append(new_str)
                
                if num != math.inf:
                    ans.append(str(num))

            curr_range = num

        return ans
    
    def sln2(self, nums: List[int]) -> List[str]:
        ans = []
        i = 0
        n = len(nums)

        while i < n:
            start = nums[i]
            while i + 1 < n and nums[i] + 1 == nums[i + 1]:
                i += 1

            end = nums[i]
            append_str = f"{start}->{end}" if start != end else str(end)
            ans.append(append_str)

            i += 1

        return ans