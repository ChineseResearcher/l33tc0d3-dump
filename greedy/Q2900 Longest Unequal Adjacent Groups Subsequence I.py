# greedy - easy
from typing import List
class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        n = len(words)
        # this problem can be better solved by greedy
        # i.e whenever we encounter a group, that is the first or different from prev. chosen group
        # we can add it to our LAS, as local optimality leads to global optimality

        LAS = [0]
        for i in range(1, n):
            if groups[i] != groups[LAS[-1]]:

                LAS.append(i)

        return [words[i] for i in LAS]
    
words, groups = ["e","a","b"], [0,0,1]
words, groups = ["a","b","c","d"], [1,0,1,1]

Solution().getLongestSubsequence(words, groups)