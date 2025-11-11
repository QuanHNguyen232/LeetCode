class Solution:
    def totalMoney(self, n: int) -> int:
        """let total_one_week = $28/week (week: [1, 2, 3, 4, 5, 6, 7])
        n = 4
        week=0, day=4
        ans = (
            total_one_week + 7*0
            sum([1, 2, 3, 4]) = sum([1, 2, 3, 4]) + day*0
        )

        n = 10
        week=1, day=3
        ans = (
            total_one_week + 7*1
            + sum([2, 3, 4]) = sum([1, 2, 3]) + day*1
        )

        n = 20
        week=2, day=6
        ans = (
            total_one_week + 7*2
            + sum([3, 4, 5, 6, 7, 8]) = sum([1, 2, 3, 4, 5, 6]) + day*week
        )
        """
        DAYS_PER_WEEK = 7
        ans = 0
        one_week = list(range(1, 8))
        total_one_week = sum(one_week)

        num_weeks = n // DAYS_PER_WEEK
        num_remain_day = n % DAYS_PER_WEEK

        # add by weeks
        for week in range(num_weeks):
            ans += total_one_week + week*DAYS_PER_WEEK
        
        # add by remain days
        ans += sum(one_week[:num_remain_day]) + (num_remain_day*num_weeks)
        
        return ans