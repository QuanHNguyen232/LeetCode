class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        merged = []
        for i in range(len(nums)):
            for num in nums[i]:
                merged.append((num, i))
        merged.sort()

        freq = defaultdict(int)
        left = 0
        range_start, range_end = 0, math.inf
        for right in range(len(merged)):
            right_num, right_idx = merged[right]
            freq[right_idx] += 1

            while len(freq) >= len(nums):
                left_num, left_idx = merged[left]

                if right_num - left_num < range_end - range_start:
                    range_start = left_num
                    range_end = right_num

                freq[left_idx] -= 1
                if freq[left_idx] == 0:
                    del freq[left_idx]

                left += 1
           
        return [range_start, range_end]