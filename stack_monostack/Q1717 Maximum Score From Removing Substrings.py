# stack - medium
class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:

        def match(ss, pat):

            # pat is either 'ab' or 'ba'
            st, cnt = [], 0

            for char in ss:

                if st and st[-1] == pat[0] and char == pat[1]:
                    st.pop()
                    cnt += 1

                else:
                    st.append(char)

            return st, cnt

        score = 0

        if x >= y:

            st, cnt = match(s, 'ab')
            s = ''.join(st)
            score += x * cnt

            st, cnt = match(s, 'ba')
            score += y * cnt

        else:

            st, cnt = match(s, 'ba')
            s = ''.join(st)
            score += y * cnt

            st, cnt = match(s, 'ab')
            score += x * cnt

        return score
    
s, x, y = "cdbcbbaaabab", 4, 5
s, x, y = "aabbaaxybbaabb", 5, 4

Solution().maximumGain(s, x, y)