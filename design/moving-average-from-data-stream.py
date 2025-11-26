class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.total = deque()
        self.past = 0

    def next(self, val: int) -> float:
        prev = self.total[-1] if self.total else 0
        self.total.append(val + prev)
        if len(self.total) > self.size:
            self.past = self.total.popleft()
        return (self.total[-1] - self.past) / len(self.total)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)