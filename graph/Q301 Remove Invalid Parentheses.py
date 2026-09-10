# graph - hard
from typing import List
from collections import deque
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        
        n = len(s)
        # key ideas:
        # 1) model the problem as a graph problem, solved by BFS by tracking
        # number of removals during traversal
        # 2) start with initial state s (i.e. our original string), for every
        # transition u -> v, remove a bracket from u
        # 3) the first time we reach a state v with no invalid parantheses will
        # be the min. removals needed due to nature of BFS, and we record all
        # variations of sequences with the same no. of removals 

        # helper to validate a string
        def isValid(currString: str) -> bool:
            diff = 0
            for c in currString:
                if c == "(":
                    diff += 1
                if c == ")":
                    diff -= 1
                if diff < 0: return False
            return diff == 0

        b_c, b_seq = float('inf'), []

        q = deque([s])
        v = set(q)
        while q:

            s = q.popleft()
            # c: number of removals uniquely determined by curr. string length
            c = n - len(s) 
            if isValid(s):
                if c < b_c:
                    b_seq = [s]
                    b_c = c
                elif c == b_c:
                    b_seq.append(s)
                continue

            # stop searching when curr. steps >= best steps found
            if c >= b_c: continue

            for i in range(len(s)):
                if s[i] in ['(', ')']:
                    ns = s[:i] + s[i+1:]
                    if ns not in v:
                        q.append(ns)
                        v.add(ns)

        return b_seq

s = ")("
s = "()())()"
s = "(a)())()"
s = "()" * 12 + ")"

Solution().removeInvalidParentheses(s)