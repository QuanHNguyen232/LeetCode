class RandomizedSet:

    def __init__(self):
        self.dict = {}
        self.list = []

    def insert(self, val: int) -> bool:
        if val not in self.dict:
            self.dict[val] = len(self.list)
            self.list.append(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        if val not in self.dict:
            return False
        # update
        rm_idx = self.dict[val]
        rplace_idx = self.dict[self.list[-1]]

        self.dict[self.list[-1]] = rm_idx
        self.list[rm_idx], self.list[rplace_idx] = self.list[rplace_idx], self.list[rm_idx]

        # delete
        self.list.pop()
        del self.dict[val]
        return True

    def getRandom(self) -> int:
        return choice(self.list)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()