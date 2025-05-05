# stack - medium
from typing import List
class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        # use a stack to store unclosed left brackets, along with indices
        st = []

        # first perform one pass to find out the max. depth possible
        # note that we can always know how deep we are
        # in a bracket (of brackets...) if querying len(st) w/ all unclosed '('
        max_depth = 0
        for brkt in seq:
            
            if brkt == '(':
                st.append(brkt)
            else:
                max_depth = max(max_depth, len(st))
                st.pop()
                
        # if max depth is just 1, safe to just assign all brackets
        # to group A, as the max depth can't be further minimised between (0,1)
        if max_depth == 1:
            return [0] * len(seq)

        # otherwise we need to assign to A or B based on whether a closing bracket
        # whose depth falls within [1, floor(max_depth / 2)] or [ceiling(max_depth / 2), max_depth]
        ans = [-1] * len(seq)

        st = []
        for idx, brkt in enumerate(seq):
            
            if brkt == '(':
                st.append([brkt, idx])       
            else:
                if len(st) <= max_depth / 2:
                    _, idx_l = st.pop()
                    ans[idx] = ans[idx_l] = 0

                else:
                    _, idx_l = st.pop()
                    ans[idx] = ans[idx_l] = 1 
                    
        return ans
    
seq = "(()())"
seq = "()(())()"
seq = "(((()))((())))"

Solution().maxDepthAfterSplit(seq)