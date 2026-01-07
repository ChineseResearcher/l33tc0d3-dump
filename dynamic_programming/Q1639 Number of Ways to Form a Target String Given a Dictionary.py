# dp - hard
from collections import defaultdict
from typing import List
class Solution:
    def recursiveForming(self, idx_k, idx_t):
        if idx_t == self.n:
            return 1
        
        if idx_k == self.m:
            return 0
        
        # return memoization result
        if (idx_k, idx_t) in self.dp:
            return self.dp[(idx_k, idx_t)]
        
        # Skip the current index in words
        curr_result = self.recursiveForming(idx_k + 1, idx_t)
        
        # Use matching characters at the current index
        if self.target[idx_t] in self.freq[idx_k]:
            curr_result += (self.freq[idx_k][self.target[idx_t]] * \
                            self.recursiveForming(idx_k + 1, idx_t + 1)) % (1e9 + 7)

        # memoize
        self.dp[(idx_k, idx_t)] = curr_result 

        return curr_result

    def numWays(self, words: List[str], target: str) -> int:
        self.n = len(target)
        self.m = len(words[0]) # all words have same length

        self.words = words
        self.target = target

        # Precompute frequency map
        self.freq = [defaultdict(int) for _ in range(self.m)]
        for word in self.words:
            for i, char in enumerate(word):
                self.freq[i][char] += 1

        self.dp = dict()

        return int(self.recursiveForming(0, 0) % (1e9 + 7))
    
words, target = ["acca","bbbb","caca"], "aba"
words, target = ["abba","baab"], "bab"
# constraint
words, target = ["a"*1000] * 1000, "a"*1000

Solution().numWays(words, target)