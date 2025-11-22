class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        hashmap = defaultdict(list)
        for trans in transactions:
            name, time, amount, city = trans.split(',')
            hashmap[name].append([name, time, amount, city])

        ans = []
        for name in hashmap.keys():
            trans = hashmap[name]
            trans.sort(key=lambda x: int(x[1])) # sort by time

            for i in range(len(trans)):
                prev = trans[i]
                prevStr = ",".join(prev)

                if int(prev[2]) > 1000:
                    ans.append(prevStr)

                for j in range(i+1, len(trans)):
                    curr = trans[j]
                    currStr = ",".join(curr)
                    # check time <= 60mins
                    if (
                        int(curr[1]) - int(prev[1]) <= 60 # time bw transactions <= 60mins
                        and curr[-1] != prev[-1] # same name, diff city
                    ):
                        # add to ans
                        if currStr not in ans: ans.append(currStr)
                        if prevStr not in ans: ans.append(prevStr)

        return ans