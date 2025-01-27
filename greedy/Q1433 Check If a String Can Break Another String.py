# greedy - medium
class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        n = len(s1)
        s1_, s2_ = sorted(s1), sorted(s2)

        breakS1, breakS2 = True, True
        for i in range(n):

            if s1_[i] < s2_[i]:
                breakS2 = False

            if s2_[i] < s1_[i]:
                breakS1 = False

        return (breakS1 or breakS2)
    
s1, s2 = "abc", "xya"
s1, s2 = "abe", "acd"
s1, s2 = "leetcodee", "interview"

Solution().checkIfCanBreak(s1, s2)