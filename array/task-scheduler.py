class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cnter = Counter(tasks)
        heap = [(-count, char) for char, count in cnter.items()]
        heapify(heap)

        hashmap = {} # store char with last time used
        ans = [] # easier to debug

        while heap:
            curr_idx = len(ans)
            tmp_store = []
            cnt_add, val_add = None, None

            # find next possible item to add
            while heap:
                count, val = heapq.heappop(heap)
                if (val in hashmap) and (curr_idx - hashmap[val] <= n):
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
                    heapq.heappush(heap, (cnt_add, val_add))
            else:
                # if cannot find any other char -> add "idle"
                ans.append("idle")

            for item in tmp_store:
                heapq.heappush(heap, item)

        return len(ans)
