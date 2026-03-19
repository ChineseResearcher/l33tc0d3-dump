# stack - hard
import re
from typing import List, Tuple
from collections import defaultdict
class Solution:
    def countOfAtoms(self, formula: str) -> str:

        s = formula
        n = len(s)
        # a helper to split by uppercase chars.
        def sp1(s: str) -> List[str]:
            return re.findall('[A-Z][^A-Z]*', s)

        # a helper to split a element-freq pair
        def sp2(s: str) -> Tuple[str, int]:
            freq, idx = 1, len(s) - 1
            st = []
            while idx >= 0 and s[idx].isnumeric():
                st.append(s[idx])
                idx -= 1

            if st:
                st = st[::-1]
                freq = int(''.join(st))

            return s[:idx+1], freq

        # first pass to un-pack all the brackets and re-append
        # the correct formula substrings e.g. (OH)2 -> O2H2
        st, idx = [], 0
        while idx < n:

            if s[idx] != ')':
                st.append(s[idx])
                idx += 1
                continue

            # find the left bracket
            temp = []
            while st and st[-1] != '(':
                temp.append(st.pop())
            
            # pop the left bracket
            if st: st.pop()
            
            bracket_str = ''.join(temp[::-1])
            
            idx += 1
            temp = []
            # find the multiplier of this bracket
            while idx < n and s[idx].isnumeric():
                temp.append(s[idx])
                idx += 1

            mul = int(''.join(temp)) if temp else 1

            temp = []
            # process and bracket string and expand the formula
            for pair in sp1(bracket_str):
                element, freq = sp2(pair)
                temp.append(element + str(freq * mul))

            st.extend(temp)

        # update string
        s = ''.join(st)

        # create a hashmap for storing element frequencies
        f = defaultdict(int)

        # second pass to obtain answer
        for pair in sp1(s):
            element, freq = sp2(pair)
            f[element] += freq

        res = []
        for k in sorted(f.keys()):
            res.append(k)
            res.append(str(f[k]) if f[k] > 1 else '')

        return ''.join(res)
    
formula = "H2O"
formula = "Mg(OH)2"
formula = "Mg(H2O)N"
formula = "K4(ON(SO3)2)2"

Solution().countOfAtoms(formula)