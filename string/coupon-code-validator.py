class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        cate_order = {
            key: idx
            for idx, key in enumerate(["electronics", "grocery", "pharmacy", "restaurant"])
        }
        grps = [[] for _ in range(len(cate_order))]

        for (curr_code, category, status) in zip(code, businessLine, isActive):
            if (
                len(curr_code) > 0 and curr_code.replace("_", "").isalnum()
                and status
                and category in cate_order
            ):
                grps[cate_order[category]].append(curr_code)

        grps = [sorted(grp) for grp in grps]
        ans = []
        for grp in grps:
            ans.extend(sorted(grp))
        return ans