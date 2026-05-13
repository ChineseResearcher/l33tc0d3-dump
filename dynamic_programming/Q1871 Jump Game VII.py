# dp - medium
class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        
        n = len(s)
        # key ideas:
        # 1) for any index i where s[i] = '0', where are interested in whether
        # there were any previous reachable '0's falling in the range [i-maxJump, i-minJump]
        # 2) maintain a prefix sum of successful reaches, and query the range
        # to determine if curr. '0' is reachable

        state_pf = [1] # first '0' is where we started

        for i in range(1, n):

            if s[i] == '0':
                incl = state_pf[i-minJump] if i - minJump >= 0 else 0
                excl = state_pf[i-maxJump-1] if i - maxJump - 1 >= 0 else 0

                if incl - excl > 0:
                    state_pf.append(state_pf[-1] + 1)
                else:
                    state_pf.append(state_pf[-1])

            else:
                state_pf.append(state_pf[-1])

        return state_pf[-1] > state_pf[-2]

s, minJump, maxJump = "011010", 2, 3
s, minJump, maxJump = "01101110", 2, 3

Solution().canReach(s, minJump, maxJump)