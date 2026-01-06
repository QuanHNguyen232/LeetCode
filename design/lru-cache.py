class LRUCache:
    '''
    least recently used key: either get or put
    LRUCache lRUCache = new LRUCache(2);
    lRUCache.put(1, 1); // cache is {1=1} // use recent_use = [1]
    lRUCache.put(2, 2); // cache is {1=1, 2=2} // use [2, 1] (2 is more recent)
    lRUCache.get(1);    // return 1 //use [1, 2]
    lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3} // use [3, 1]
    lRUCache.get(2);    // returns -1 (not found) // use [3, 1]
    lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3} // use [4, 3]
    '''
    def __init__(self, capacity: int):
        self.capacity = capacity
        
        # whether use approach 1 (doubly linked-list) or approach 2 (OrderedDict)
        self.approach_1 = True

        if self.approach_1:
            self.hash = {}
            self.tracker = DoublyLinkedListTracker() # first item: most use, last item: least use
        else:
            self.tracker = collections.OrderedDict() # first item: least use, last item: most use

    def get(self, key: int) -> int: # must O(1)
        if self.approach_1:
            if key in self.hash:
                self.tracker.remove(key)
                self.tracker.insert_front(key)
                return self.hash[key]
            return -1
        
        # approach 2:
        else:
            if key in self.tracker:
                self.tracker.move_to_end(key, last=True) # last=True: move to right-end
                return self.tracker[key]
            return -1

    def put(self, key: int, value: int) -> None: # must O(1)
        '''
        cases:
            key in hash --> update key-val
            key not in hash:
                if max capacity:
                    remove least recent use
                    insert into hash
                else:
                    insert into hash
        '''
        if self.approach_1:
            if key in self.hash: # update recent use --> most recent use
                self.tracker.remove(key)

            # add new key-val
            self.tracker.insert_front(key)
            self.hash[key] = value

            if len(self.hash) > self.capacity: # if max capacity:
                least_key = self.tracker.get_least_key()
                self.tracker.remove(least_key)
                del self.hash[least_key]

        else:
            if key in self.tracker: # update recent use --> most recent use
                self.tracker.move_to_end(key, last=True)


            if len(self.tracker) >= self.capacity: # if max capacity:
                self.tracker.popitem(last=False)

            # add new key-val
            self.tracker[key] = value



class Node:
    def __init__(self, key, prevNode, nextNode):
        self.key = key
        self.prev = prevNode
        self.next = nextNode

class DoublyLinkedListTracker:
    def __init__(self):
        self.map = {}
        self.head = None
        self.tail = None
    
    def remove(self, key):
        # case map is empty (len(map) < 1)
        # do nothing

        # case key is also head (len(map) == 1)
        if len(self.map) == 1:
            # remove key is also empty everything
            del self.map[key]
            self.head = None
            self.tail = None
        elif len(self.map) > 1:
            # case map is NOT empty (len(map) > 1)
            currNode = self.map[key]
            del self.map[key]

            if key == self.tail:
                prevNode = currNode.prev
                prevNode.next = None
                self.tail = prevNode.key
            elif key == self.head:
                nextNode = currNode.next
                nextNode.prev = None
                self.head = nextNode.key
            else: # key is middle node
                prevNode = currNode.prev
                nextNode = currNode.next

                prevNode.next = nextNode
                nextNode.prev = prevNode

    def insert_front(self, key):
        # case map is empty
        currNode = Node(key, None, None)

        if len(self.map) == 0:
            self.tail = key
        # map not empty
        else:
            headNode = self.map[self.head]
            currNode.next = headNode
            headNode.prev = currNode

        self.map[key] = currNode
        self.head = key

    def get_least_key(self):
        return self.tail
        
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)