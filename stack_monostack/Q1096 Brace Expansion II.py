# stack - hard
import re
class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:

        # key ideas:
        # 1) use a stack and address every pair of bracket
        # 2) after a pair of bracket is addressed, the members in this bracket
        # will either be appended or multiplied with the previous set
        
        # add enclosing brackets for all singletons
        def add_brackets(s: str) -> str:
            # Lowercase letters immediately before '{'
            s = re.sub(r'([a-z]+)(?=\{)', r'{\1}', s)
            # Lowercase letters immediately after '}'
            s = re.sub(r'(?<=\})([a-z]+)', r'{\1}', s)
            return s

        st, st2 = [''], []
        for c in add_brackets(expression):
            if c != "}":
                if c in ['{', ',']:
                    if st2:
                        st.append(''.join(st2))
                    st2 = [] # reset
                    st.append(c)
                else:
                    st2.append(c)
                continue

            if st2:
                st.append(''.join(st2))
            st2 = []
            
            curr = set()
            # otherwise, we keep popping the st. until we reach a left bracket
            while st[-1] != "{":
                p = st.pop()
                if p != ',':
                    if isinstance(p, str):
                        curr.add(p)
                    else:
                        curr |= p

            st.pop() # pop the left bracket
            if st[-1] in ['{', ',']:
                st.append(curr)
            else:
                mul = set()
                prev = st.pop() if isinstance(st[-1], set) else set([st.pop()])
                for a in prev:
                    for b in curr:
                        mul.add(a + b)
                st.append(mul)

        st.append(''.join(st2))

        final = set()
        for x in st:
            if isinstance(x, set):
                final |= x
            else:
                if x != ',':
                    final.add(x)

        final.discard('')
        return sorted(final)

expression = "abcd"
expression = "{a,b,c,d},e"
expression = "{a,b}c{d,e}f"
expression = "ee{a,b,c,d},g"
expression = "{a,{b,{c,de}}}"
expression = "{a,b}{c,{d,e}}"
expression = "{{a,z},a{b,c},{ab,z}}"
expression = "a{x,ia,o}w{n,{g,{u,o}},{a,{x,ia,o},w}}er"

Solution().braceExpansionII(expression)