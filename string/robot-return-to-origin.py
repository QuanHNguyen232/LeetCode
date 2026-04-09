class Solution:
    def judgeCircle(self, moves: str) -> bool:
        cnter = Counter(list(moves))

        return cnter.get('D')==cnter.get('U') and cnter.get('R')==cnter.get('L')