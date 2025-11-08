class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        '''
        sort by starting time

        [0,30],[5,10],[10, 14],[15,20]
        [5,10],[10, 14]: can merge (same room)

        [0, 5], [0, 2]: may want to short by end time if same start time --> use hashmap
        [0, 2], [0, 5], [3, 5]

        [(0, 1), (30, -1), (5, 1), (10, -1), (15, 1), (20, -1)]
        [(0, 1), (5, 1), (10, -1), (15, 1), (20, -1), (30, -1)] (sorted) --> cannot handle [1,13], [13,15]

        [1,13], [13,15]
        [(1, 1), (13, -1)] want to add  (13, 1)
        [(1, 1), (13, -1), (13, 1), (15, -1)]
        '''
        # return self.sln1(intervals)
        return self.sln2(intervals)

    def sln2(self, intervals):
        ans = 0
        count = 0
        START = 1
        END = -1 # [[0,5],[5,10]] -> 1 room, so END goes before START
        arr = []
        for interval in intervals:
            start_time, end_time = interval
            arr.append((start_time, START))
            arr.append((end_time, END))
        arr.sort()
        # print(arr)
        
        for item in arr:
            if item[1] == START:
                count += 1
            else:
                count -= 1
            ans = max(ans, count)
        return ans

    def sln1(self, intervals):
        ans = 0
        
        arr = []
        for (start, end) in intervals:
            arr.append((start, 1))
            arr.append((end, -1))
        
        #arr = sorted(arr, cmp=lambda x, y: )

        # arr.sort(key= lambda x: x[0])x ** 3 - y ** 3
        # arr.sort(key = lambda x: (x[0], x[1]))
        # arr.sort(cmp = lambda x, y: x[1] - y[1] if x[0] == y[0] else x[0] - y[0] )
        arr.sort(key = functools.cmp_to_key(lambda x, y: x[1] - y[1] if x[0] == y[0] else x[0] - y[0]))
        print(arr)
        
        count = 0
        for (_, i) in arr:
            count += i
            ans = max(ans, count)

        return ans