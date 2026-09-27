# stack - medium
class Solution:
    def reverseParentheses(self, s: str) -> str:
        
        n = len(s)
        # key ideas:
        # 1) use a stack to reverse all strings within each pair of brackets

        st = []
        for i in range(n):
            if s[i] == ')':
                aux = []
                while st[-1] != '(':
                    aux.append(st.pop())
                st.pop()
                st.extend(aux)
            else:
                st.append(s[i])
        
        return ''.join(st)

s = "(abcd)"
s = "(u(love)i)"
s = "(ed(et(oc))el)"

Solution().reverseParentheses(s)