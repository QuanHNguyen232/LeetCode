class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """monotonic stack/queue: keep a list of number from largest->smallest
        [1,3,-1,-3,5,3,6,7]
        subarr=[1] --> dq = [1]
        subarr=[1,3] --> dq = [3] # pop all smallest < 3
        subarr=[1,3,-1] --> dq = [3,-1]
        subarr=[1,3,-1,-3] --> dq = [3,-1,-3]
        subarr=[1,3,-1,-3,5] --> dq = [5]
        """
        dq = deque()
        res = []
        
        # init window size k
        for i in range(k):
            curr_val = nums[i]
            while dq and curr_val >= dq[-1][0]:
                dq.pop()
            dq.append((curr_val, i))

        res.append(dq[0][0])

        for i in range(k, len(nums)):
            curr_val = nums[i]
            if dq and dq[0][1] == i - k:
                dq.popleft()
            while dq and curr_val >= dq[-1][0]:
                dq.pop()

            dq.append((curr_val, i))
            res.append(dq[0][0])

        return res