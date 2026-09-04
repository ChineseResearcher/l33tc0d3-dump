# dp - hard
from typing import List
from functools import cache
class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:

        n = len(words)
        fmax = lambda a, b: a if a > b else b
        # key ideas:
        # 1) words.length <= 15, so knapsack-style bitmask DP is feasible
        # 2) use a bitmask to store the set of chosen words

        # map letters to their frequencies
        letter_freq = [0] * 26
        for x in letters:
            letter_freq[ord(x) - ord('a')] += 1

        # helper to determine the total score a set of words
        @cache
        def wscore(mask:int) -> int:
            curr_freq, total_score = [0] * 26, 0
            for i in range(mask.bit_length()):
                if mask & (1 << i):
                    w = words[i]
                    for x in w:
                        j = ord(x) - ord('a')
                        curr_freq[j] += 1
                        if curr_freq[j] > letter_freq[j]:
                            return -1
                        total_score += score[j]
            return total_score

        @cache
        def f(i:int, mask:int) -> int:

            if i == n:
                return wscore(mask)
            
            # not pick i
            skip = f(i + 1, mask)

            # pick i
            pick = f(i + 1, mask | (1 << i))

            return fmax(skip, pick)

        return f(0, 0)

words = ["dog","cat","dad","good"]
letters = ["a","a","c","d","d","d","g","o","o"]
score = [1,0,9,5,0,0,3,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0]

words = ["xxxz","ax","bx","cx"]
letters = ["z","a","b","c","x","x","x"]
score = [4,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,10]

Solution().maxScoreWords(words, letters, score)