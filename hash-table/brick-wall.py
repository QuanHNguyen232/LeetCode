class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        cnter = Counter()
        n = len(wall)
        for i, row in enumerate(wall):
            cnter.update(list(itertools.accumulate(row))[:-1])

        ans = len(wall)
        for key, val in cnter.items():
            ans = min(ans, n-val)
        return ans