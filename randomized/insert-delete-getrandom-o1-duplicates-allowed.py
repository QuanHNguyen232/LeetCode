class RandomizedCollection:

    def __init__(self):
        self.lst = []
        self.idx = defaultdict(set)

    def insert(self, val: int) -> bool:
        self.idx[val].add(len(self.lst))
        self.lst.append(val)
        num_elements = len(self.idx[val])
        return num_elements == 1

    def remove(self, val: int) -> bool:
        if val not in self.idx or len(self.idx[val]) < 1: return False
        rm_idx = self.idx[val].pop()
        last_idx = len(self.lst)-1
        last_val = self.lst[last_idx]

        self.idx[last_val].add(rm_idx)
        self.idx[last_val].discard(last_idx)

        self.lst[rm_idx], self.lst[last_idx] = self.lst[last_idx], self.lst[rm_idx]
        self.lst.pop()
        return True

    def getRandom(self) -> int:
        randIdx = randint(0, len(self.lst)-1)
        return self.lst[randIdx]


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()