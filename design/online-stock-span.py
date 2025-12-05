class StockSpanner:

    def __init__(self):
        # store value and index in Monotonic stack
        self.max_stack = []

    def next(self, price: int) -> int:
        ans = 1
        while self.max_stack and self.max_stack[-1][0] <= price:
            ans += self.max_stack.pop()[1]

        self.max_stack.append([price, ans]) # price span of price
        return ans


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)