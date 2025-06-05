# dp - hard
class Solution:
    def numPermsDISequence(self, s: str) -> int:
        n = len(s)
        MOD = int(1e9 + 7)

        def recursive_perm(pos, smallerCnt):

            if pos == n:
                return 1
            
            if (pos, smallerCnt) in dp:
                return dp[(pos, smallerCnt)]

            # use m to represent curr. available count of numbers
            m = n - pos

            # then we have m possible splits
            curr_res = 0
            if s[pos] == 'D':
                
                for i in range(0, smallerCnt):
                    curr_res += recursive_perm(pos+1, i)
                    curr_res %= MOD

            elif s[pos] == 'I':

                for j in range(smallerCnt, m):
                    curr_res += recursive_perm(pos+1, j)
                    curr_res %= MOD

            dp[(pos, smallerCnt)]= curr_res
            return curr_res

        dp = dict()

        ans = 0
        for i in range(0, n+1):
            ans += recursive_perm(0, i)
            ans %= MOD

        return ans
    
s = "D"
s = "DID"
s = "DI" * 100

Solution().numPermsDISequence(s)