class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        """
        [5,4,2,4]
        Consider:
        [5] -> good
        [5,4] -> good
        [5,4,2] -> bad (max(5)-min(2)=3 > 2) -> [4,2] -> good
        [4,2,4] -> good
        """
        # Map to maintain sorted frequency map of current window
        freq = defaultdict(int)
        left = right = 0
        count = 0  # Total count of valid subarrays

        for right in range(len(nums)):
            # Add current element to frequency map
            freq[nums[right]] += 1

            # While window violates the condition |nums[i] - nums[j]| ≤ 2
            # Shrink window from left
            while max(freq) - min(freq) > 2:
                # Remove leftmost element from frequency map
                freq[nums[left]] -= 1
                if freq[nums[left]] == 0:
                    del freq[nums[left]]
                left += 1

            # Add count of all valid subarrays ending at right
            count += right - left + 1

        return count