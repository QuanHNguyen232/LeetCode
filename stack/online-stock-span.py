class StockSpanner:

    def __init__(self):
        # store value and index
        self.idx = 0
        self.max_stack = []

    def next(self, price: int) -> int:
        self.idx += 1
        ans = 1
        # print(self.max_stack, (price, self.idx))
        while self.max_stack and self.max_stack[-1][0] <= price:
            prev_price, prev_idx = self.max_stack.pop()
        if self.max_stack:
            ans = max(ans, self.idx - self.max_stack[-1][1])
        self.max_stack.append([price, self.idx])
        # print(ans)
        return ans


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)