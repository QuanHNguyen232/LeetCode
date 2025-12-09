class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        hashmap = defaultdict(list)
        MOD = 1e9+7
        ans = 0

        for i, num in enumerate(nums):
            hashmap[num].append(i)
        
        for num_j in hashmap.keys():
            num_i = num_k = num_j*2
            if num_i not in hashmap: continue
            for idx, j in enumerate(hashmap[num_j]):
                if j == 0 or j==len(nums)-1: # then there is no i or no k
                    continue
                if num_j==num_i:
                    # print(num_j, j, hashmap[num_i])
                    if 0 < idx < len(hashmap[num_j]):
                        cnt_i = idx
                        cnt_k = len(hashmap[num_j]) - idx - 1
                        ans = (ans + cnt_i*cnt_k) % MOD
                else:
                    # search for idx j in hashmap[num_i]
                    # find num of idx i (i<j)
                    # find num of idx k (j<k)
                    cnt_i = bisect_right(hashmap[num_i], j)
                    cnt_k = len(hashmap[num_i]) - cnt_i
                    # print(num_j, j, cnt_i, cnt_k, hashmap[num_i])
                    ans = (ans + cnt_i*cnt_k) % MOD

        return int(ans)