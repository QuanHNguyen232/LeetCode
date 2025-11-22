"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        tree = {}
        for employee in employees:
            tree[employee.id] = {
                "importance": employee.importance,
                "subordinates": employee.subordinates
            }

        def dfs(idx: int) -> int:
            ans = 0
            ans += tree[idx]['importance']
            for sub_id in tree[idx]["subordinates"]:
                ans += dfs(sub_id)
            return ans

        return dfs(id)
