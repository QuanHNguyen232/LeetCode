class OrderedStream:

    def __init__(self, n: int):
        self.n = n
        self.currIdx = 1
        self.hashmap = {}

    def insert(self, idKey: int, value: str) -> List[str]:
        ans = []
        
        self.hashmap[idKey] = value
        # if idKey matches currIdx -> add to ans, incr currIdx
        while self.currIdx in self.hashmap:
            ans.append(self.hashmap[self.currIdx])
            del self.hashmap[self.currIdx]
            self.currIdx += 1

        return ans


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)