# backtracking - hard
from typing import List
class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        def dfs(arr):

            if len(arr) == 1:
                return set(tuple(arr))
            
            curr = set()
            for i in range(1, len(arr)):
                left, right = dfs(arr[:i]), dfs(arr[i:])
                for x in left:
                    for y in right:
                        
                        curr.add(x + y)
                        curr.add(x - y)
                        curr.add(y - x)
                        curr.add(x * y)
                        if y != 0:
                            curr.add(x / y)
                        if x != 0:
                            curr.add(y / x)

            return curr

        # take [3,3,8,8] for example, we can get 8 / (3 - 8 / 3) = 24 only if we
        # allow precision to be off by a very small epsilon
        EPS = 1e-5 
        def backtrack(used, seq):

            if len(used) == 4:
                prod = dfs(seq)
                for p in prod:
                    if abs(p - 24) <= EPS:
                        return True
                    
                return False
            
            for idx in [0,1,2,3]:
                if idx not in used:

                    seq.append(cards[idx])
                    used.add(idx)

                    if backtrack(used, seq):
                        return True
                    
                    seq.pop()
                    used.discard(idx)

            return False

        return backtrack(set(), [])
    
cards = [4,1,8,7]
cards = [1,2,1,2]
cards = [1,9,1,2]
cards = [3,3,8,8]

Solution().judgePoint24(cards)