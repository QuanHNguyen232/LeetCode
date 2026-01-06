class Solution:
    def minimizedStringLength(self, s: str) -> int:
        # in short, just remove all duplicates
        return len(set((s)))
