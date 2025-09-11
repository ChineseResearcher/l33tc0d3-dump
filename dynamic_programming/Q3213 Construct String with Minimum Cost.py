# dp - hard
from typing import List
from collections import defaultdict
class Solution:
    def minimumCost(self, target: str, words: List[str], costs: List[int]) -> int:

        # words may not be unique, only keep the one of the smallest cost
        word_cost = dict()
        for i, w in enumerate(words):
            if w not in word_cost:
                word_cost[w] = float('inf')

            word_cost[w] = min(word_cost[w], costs[i])

        # create a dict of list of strings, 
        # 1) <grp_id based on word length, (2)>
        # 2) [w1, w2, ..., wk] of the same length, sorted in ASC order by word_cost
        wg = defaultdict(list)
        for w in word_cost.keys():
            wg[len(w)].append(w)

        for g in wg.keys():
            wg[g].sort(key=lambda x: word_cost[x])

        # pre-compute sorted group sizes (keys)
        sk = sorted(wg.keys())

        n = len(target)
        dp = [float('inf')] * (n+1)
        dp[0] = 0 # zero cost to build empty string

        for i in range(1, n+1):
            
            # explore diff. lengths
            for l in sk:

                if i - l < 0:
                    break

                prev = dp[i-l]
                # meaning target[:i-l] cannot be formed
                if prev == float('inf'):
                    continue
                
                # skip if even the min. word cost from this group of
                # words of certain length l would not beat the best dp[i] found
                if prev + word_cost[wg[l][0]] >= dp[i]:
                    continue
                
                for w in wg[l]:

                    valid, j = True, i-l
                    for char in w:
                        if target[j] != char:
                            valid = False
                            break

                        j += 1

                    if valid:
                        dp[i] = min(dp[i], prev + word_cost[w])
                        break
            
        res = dp[-1]
        return res if res < float('inf') else -1
    
target = "abcdef"
words = ["abdef","abc","d","def","ef"]
costs = [100,1,1,10,5]

target = "aaaa"
words = ["z","zz","zzz"]
costs = [1,10,100]

target = "r"
words = ["r","r","r","r"]
costs = [1,6,3,3]

target = "a" * 50000
words = ['a' * i for i in range(1, 101)]
costs = [1] * 100

Solution().minimumCost(target, words, costs)