class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        freq = Counter(operations)
        
        add = freq["++X"] + freq["X++"]
        minus = freq["--X"] + freq["X--"]
        return add - minus