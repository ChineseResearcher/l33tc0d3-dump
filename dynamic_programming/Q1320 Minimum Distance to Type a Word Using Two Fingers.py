# dp - hard
from functools import cache
from string import ascii_uppercase as upc
class Solution:
    def minimumDistance(self, word: str) -> int:

        n = len(word)
        fmin = lambda a, b: a if a < b else b
        # key ideas:
        # 1) preprocess 26 alphabets by encoding it as coords in 2-D grid
        # and precomputing the distance between any two alphabets
        # 2) top-down dfs with states (idx, fg1, fg2) where fg1
        # indicates the last typed character using first finger
        pos = dict()
        for idx, x in enumerate(upc):
            pos[x] = (idx // 6, idx % 6)

        dist = dict()
        for i in range(26):
            for j in range(i, 26):
                cd = abs(pos[upc[i]][0] - pos[upc[j]][0]) + \
                     abs(pos[upc[i]][1] - pos[upc[j]][1])
                
                dist[(upc[i], upc[j])] = cd
                dist[(upc[j], upc[i])] = cd

        @cache
        def f(idx:int, f1:str, f2:str) -> int:

            if idx == n:
                return 0
            
            # explore both fingers as the next-to-type finger
            op1 = (dist[(word[idx], f1)] if f1 else 0) + \
                  f(idx + 1, word[idx], f2)
            
            op2 = (dist[(word[idx], f2)] if f2 else 0) + \
                  f(idx + 1, f1, word[idx])

            return fmin(op1, op2)

        return f(0, '', '')
    
word = "CAKE"
word = "HAPPY"
word = "ABC" * 100

Solution().minimumDistance(word)