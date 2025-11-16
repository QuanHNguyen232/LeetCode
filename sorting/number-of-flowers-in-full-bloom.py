class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        START = 1
        END = 2
        flower_time = []
        for flower_s, flower_e in flowers:
            flower_time.append((flower_s, START))
            flower_time.append((flower_e+1, END))

        flower_time.sort()
        time_stamp = [item[0] for item in flower_time]
        cate = [item[1] for item in flower_time]
        preSum = [1 if flower_time[0][-1]==START else -1]

        for i in range(1, len(time_stamp)):
            curr_val = 1 if cate[i] == START else -1
            preSum.append(preSum[-1] + curr_val)

        ans = []
        for visit_time in people:
            idx = bisect.bisect_right(time_stamp, visit_time) - 1
            ans.append(preSum[idx])

        return ans