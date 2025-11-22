class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda x : x[0]-x[1]) # sort by how much cost saved by go to A
        ans = 0
        n = len(costs)//2
        for i in range(n):
            ans += costs[i][0] + costs[i+n][1] # from i->n: go to A (cost[0]), n+1->2n: go to B (cost[1])
        return ans