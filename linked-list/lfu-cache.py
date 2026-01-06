class LFUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.key2val = {}
        self.key2freq = {} # track freq
        self.freq2key = collections.defaultdict(collections.OrderedDict) # track least recent use
        self.minf = 0 # track least freq use

    def get(self, key: int) -> int:
        if key not in self.key2val:
            return -1
        # update freq
        oldfreq = self.key2freq[key]
        newfreq = oldfreq + 1
        self.key2freq[key] = newfreq
        self.freq2key[oldfreq].pop(key) # remove from old-freq
        if not self.freq2key[oldfreq]: # if old-freq is empty -> rm it
            del self.freq2key[oldfreq]
        self.freq2key[newfreq][key] = 1 # just use default val=1, we only care about key
        
        # update least freq
        if self.minf not in self.freq2key:
            self.minf += 1
        return self.key2val[key]

    def put(self, key: int, value: int) -> None:
        if self.cap <= 0:
            return
        if key in self.key2val:
            self.get(key) # to update freq & use order (for least recent use)
            self.key2val[key] = value
            return

        # Rm least frequently used, and if tie → least recently used
        if len(self.key2val) == self.cap:
            delkey, _ = self.freq2key[self.minf].popitem(last=False)
            del self.key2val[delkey]
            del self.key2freq[delkey]

        # Insert new key
        self.key2val[key] = value
        self.key2freq[key] = 1
        self.freq2key[1][key] = 1
        self.minf = 1


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)