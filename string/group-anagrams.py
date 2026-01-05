class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        for s in strs:
            key = ''.join(sorted(list(s)))
            hashmap[key].append(s)

        ans = [hashmap[key] for key in hashmap.keys()]
        return ans