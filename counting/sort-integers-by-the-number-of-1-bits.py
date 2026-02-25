class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def getNumBits(n):
            count = 0
            while n:
                count += 1
                n &= (n-1)
            return count
        
        arr.sort(key = lambda x: (getNumBits(x), x))
        return arr