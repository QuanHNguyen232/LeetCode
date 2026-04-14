class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        """
        Pair 1: index 0 and 2
        Pair 2: index 1 and 3
        """
        if s1 == s2:
            # NOT swap pair 1 & NOT swap pair 2
            return True
        elif (s1[0] == s2[2] and s1[2] == s2[0]) and (s1[1] == s2[3] and s1[3] == s2[1]):
            # swap pair 1 & swap pair 2
            return True
        elif (s1[0] == s2[2] and s1[2] == s2[0]) and (s1[1] == s2[1] and s1[3] == s2[3]):
            # swap pair 1 & NOT swap pair 2
            return True
        elif (s1[0] == s2[0] and s1[2] == s2[2]) and (s1[1] == s2[3] and s1[3] == s2[1]):
            # NOT swap pair 1 & swap pair 2
            return True
        return False