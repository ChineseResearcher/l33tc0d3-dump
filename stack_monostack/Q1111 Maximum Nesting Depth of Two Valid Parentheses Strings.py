# stack - medium
from typing import List
class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        
        n = len(seq)
        fmax = lambda a, b: a if a > b else b
        # keep track of max. depth
        unclosed, max_depth = 0, 0
        for brkt in seq:
            if brkt == '(':
                unclosed += 1
                max_depth = fmax(max_depth, unclosed)
            else:
                unclosed -= 1
                
        # if max depth is just 1, safe to just assign all brackets to group A
        if max_depth == 1: return [0] * n

        # otherwise we need to assign to A or B based on the depth of a closing bracket
        st, ans = [], [-1] * n
        for i in range(n):
            if seq[i] == '(':
                st.append(i)       
            else:
                if len(st) <= max_depth // 2:
                    ans[i] = ans[st.pop()] = 0
                else:
                    ans[i] = ans[st.pop()] = 1 
                    
        return ans
    
seq = "(()())"
seq = "()(())()"
seq = "(((()))((())))"

Solution().maxDepthAfterSplit(seq)