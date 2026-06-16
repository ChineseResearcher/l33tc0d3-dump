# backtracking - medium
from typing import List
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        n = len(digits)
        
        d = {'2':'abc', '3':'def',
             '4':'ghi', '5':'jkl', '6':'mno',
             '7':'pqrs', '8':'tuv', '9':'wxyz'}

        ans = []
        def f(i:int, seq:List[str]) -> None:
            
            nonlocal ans
            if i == n: 
                ans.append(''.join(seq))
            else:
                for c in d[digits[i]]:
                    seq.append(c)
                    _ = f(i+1, seq)
                    seq.pop() # backtrack

        _ = f(0, [])
        return ans

digits = "2"
digits = "23"
digits = "333"

Solution().letterCombinations(digits)