class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        ans = []

        for (curr_code, category, status) in zip(code, businessLine, isActive):
            if (
                curr_code and curr_code.replace("_", "").isalnum()
                and status
                and category in ["electronics", "grocery", "pharmacy", "restaurant"]
            ):
                ans.append(curr_code)

        return sorted(ans)