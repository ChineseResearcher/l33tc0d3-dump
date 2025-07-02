# dp - hard
from itertools import groupby, accumulate
from functools import reduce
class Solution:
    def possibleStringCount(self, word: str, k: int) -> int:

        MOD = int(1e9 + 7)

        # we groupby the string into blocks 
        # e.g. 'aabbbbccc' translates into [2,4,3] where each number is the block length
        groups = [len(list(group)) for _, group in groupby(word)]

        # suppose there's no "k" involved, then we could
        # form strings with a count of len_1 * len_2 * ... * len_m
        all_cnt = reduce(lambda x, y: x * y % MOD, groups, 1)

        m = len(groups)
        # special case: m >= k
        # groups.length = m means the shortest intended string is length-m
        # when m is at least k, it has no constraint on how a string can be form
        # thus making the answer equivalent to all_cnt
        if m >= k:
            return all_cnt

        # since k is quite small (at most 2000)
        # it is very helpful for us to consider the complement problem:
        # what is the count of valid strings w/ length up to w?
        # for a certain k, w = k - 1

        # this is analogous to the classic knapsack problem
        # where we tweak the context a bit to ask for:
        # if we are to include every type of item at least once up to groups[:i]
        # how many choices do we have s.t. the total weight (len_1 + ... len_i) < w?

        # for tabulation we have two dimensions:
        # 1) idx where we consider up to groups[:idx], i.e. we consider groups[:0] -> groups[:m]
        # 2) w in the range [0,1,...,k]
        dp =  [ [0] * (k + 1) for _ in range(m + 1) ]
        for i in range(1, k + 1):

            # if we consider no items (i.e., groups[:0])
            # we assign dummy "1"s to w in range [1, k]
            dp[0][i] = 1

        # O(n * k)
        for i in range(1, m+1):

            x = groups[i-1] # 0-index

            # prefix sum of dp states considering up to groups[:(i-1)]
            # for all weights in range [0, k]
            pfSum = list(accumulate(dp[i-1]))
            for w in range(1, k + 1):

                # the application of prefix sum is crucial to achieve efficiency
                # why does prefix sum work?
                # suppose the curr. item = 3, and w = 7
                # since w > k, possible combinations are:
                # (1, 6), (2, 5), (3, 4)
                # there's no (0, 7) as we have to take at least one occurrence of curr. item
                # thus we are essentially summing dp[i-1][4] + dp[i-1][5] + dp[i-1][6]
                # which can be expressed as pfSum[6] - pfSum[3]
                dp[i][w] = (pfSum[w-1] - (pfSum[w-x-1] if w > x else 0)) % MOD

        return (all_cnt - dp[m][k]) % MOD
    
word, k = "aabbccdd", 7
word, k = "aabbccdd", 8
word, k = "aaabbb", 3
word, k = "aaabb" * int(1e5), 2000 # constraint

Solution().possibleStringCount(word, k)