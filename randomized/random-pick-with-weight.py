class Solution:
    def __init__(self, w: List[int]):
        """
        :type w: List[int]
        """
        self.prefix_sums = []
        prefix_sum = 0
        for weight in w:
            prefix_sum += weight
            self.prefix_sums.append(prefix_sum)
        self.total_sum = prefix_sum

    def pickIndex(self) -> int:
        """
        :rtype: int
        """
        def binary_search_left(target):
            # run a binary search to find the target zone
            low, high = 0, len(self.prefix_sums)
            while low <= high:
                mid = low + (high - low) // 2
                if self.prefix_sums[mid] >= target:
                    high = mid - 1
                else:
                    low = mid + 1
            return low

        target = self.total_sum * random.random()
        return binary_search_left(target)

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()