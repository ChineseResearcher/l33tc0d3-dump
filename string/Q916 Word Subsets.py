# string - medium
from collections import Counter
class Solution:
    def wordSubsets(self, words1, words2):

        # to find alls words in word1 that all words in words2 are subset of
        # we can perform a frequency mapping all every word in words2
        # s.t. we only keep the maximum frequency of every alphabet
        subsetMap = dict()
        for word in words2:
            for alphabet, freq in Counter(word).items():
                if alphabet not in subsetMap:
                    subsetMap[alphabet] = freq

                subsetMap[alphabet] = max(subsetMap[alphabet], freq)

        # each word is at most length 10, so it should be constant time
        # when we count its alphabet frequencies as we iterate
        ans = []
        for word in words1:
            sourceMap = Counter(word)

            isSubset = True
            for alphabet, freq in subsetMap.items():
                if alphabet not in sourceMap or sourceMap[alphabet] < freq:
                    isSubset = False
                    break

            if isSubset: ans.append(word)

        return ans
    
words1 = ["amazon","apple","facebook","google","leetcode"]
words2 = ["e","o"]

words1 = ["amazon","apple","facebook","google","leetcode"]
words2 = ["l","e"]

words1 = ["amazon","apple","facebook","google","leetcode"]
words2 = ["lo","eo"]

Solution().wordSubsets(words1, words2)