# stack - medium
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        
        # key ideas:
        # 1) use a stack to process valid pairs, and for unclosed
        # right brackets increment our moves
        st = []

        ans = 0
        for x in s:
            if x == ')':
                if st:
                    st.pop()
                else:
                    ans += 1
            else:
                st.append('(')

        # remaining left brackets need equivalent moves to close
        ans += len(st)
        return ans

s = "())"
s = "((("

Solution().minAddToMakeValid(s)