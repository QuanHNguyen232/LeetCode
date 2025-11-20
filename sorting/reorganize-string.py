class Solution:
    def reorganizeString(self, s: str) -> str:
        # Similar to: https://leetcode.com/problems/task-scheduler/
        cnter = Counter(s)
        hashmap = {} # store char with last time used
        ans = []
        
        max_heap = [(-count, char) for char, count in cnter.items()]
        heapify(max_heap)

        while max_heap:
            curr_idx = len(ans)
            tmp_store = []
            cnt_add, val_add = None, None

            # find next possible item to add
            while max_heap:
                count, val = heapq.heappop(max_heap)
                if (val in hashmap) and (curr_idx - hashmap[val] <= 1):
                    # if cannot add, move to storage
                    tmp_store.append((count, val))
                else:
                    cnt_add, val_add = count, val
                    break
            
            if (cnt_add is not None) and (val_add is not None):
                # if find char to add
                hashmap[val_add] = len(ans)
                ans.append(val_add)
                cnt_add += 1
                if cnt_add < 0:
                    heapq.heappush(max_heap, (cnt_add, val_add))
                
                for item in tmp_store:
                    heapq.heappush(max_heap, item)
            else:
                # if cannot find any other char -> return ""
                return ""

        return ''.join(ans)