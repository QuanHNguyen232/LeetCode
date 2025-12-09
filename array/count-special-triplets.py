class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        hashmap = defaultdict(list)
        MOD = 1e9+7
        ans = 0

        for i, num in enumerate(nums):
            hashmap[num].append(i)

        for num_j in hashmap.keys():
            target = num_j * 2
            if target not in hashmap: continue
            for idx, j in enumerate(hashmap[num_j]):
                if j == 0 or j==len(nums)-1: continue # then there is no i (j=0) or no k (j=len(nums)-1)
                if num_j == target and 0 < idx < len(hashmap[num_j]):
                    cnt_i = idx
                    cnt_k = len(hashmap[num_j]) - idx - 1
                else: # case: num_j != target
                    cnt_i = bisect_right(hashmap[target], j) # search for idx j in hashmap[target]
                    cnt_k = len(hashmap[target]) - cnt_i
                ans = (ans + cnt_i*cnt_k) % MOD

        return int(ans)