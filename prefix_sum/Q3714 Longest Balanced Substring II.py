# prefix sum - medium
class Solution:
    def longestBalanced(self, s: str) -> int:

        n = len(s)
        fmax = lambda a, b: a if a > b else b
        # key ideas:
        # 1) as per hints, solve the case of 1-/2-/3-distinct character separately
        # 2) for case of 1-distinct, just find the longest repeating subarray
        # 3) for case of 2-distinct, hash the diff between the prefix count of the 
        # first char. and the second char.
        # 4) for case of 3-distinct, suppose the prefix count of 3 chars are u1, u2, u3
        # hash the prefix counts in the form of (u1-u2, u1-u3)

        ans = 1
        # 1-distinct case
        rlen = 1
        for i in range(1, n):
            if s[i] == s[i-1]:
                rlen += 1
            else:
                rlen = 1

            ans = fmax(ans, rlen)

        # 2-distinct case: (a,b), (a,c), (b,c)
        for u1, u2 in [(0,1), (0,2), (1,2)]:
            cnt = [0] * 3
            # dict storing u1-u2 as key, and idx as val
            pf = {0:-1}

            for i in range(n):
                j = ord(s[i]) - ord('a')
                if j not in [u1, u2]:
                    pf = {0:i}
                    cnt = [0] * 3
                    continue

                # otherwise, we mark increments to cnt
                cnt[j] += 1
                hkey = cnt[u1]-cnt[u2]
                if hkey in pf:
                    ans = fmax(ans, i-pf[hkey])
                else:
                    pf[hkey] = i

        # 3-distinct case: (a,b,c)
        pf = {(0,0):-1}
        cnt = [0] * 3
        for i in range(n):

            j = ord(s[i]) - ord('a')
            cnt[j] += 1
            hkey = (cnt[0]-cnt[1], cnt[0]-cnt[2])
            if hkey in pf:
                ans = fmax(ans, i-pf[hkey])
            else:
                pf[hkey] = i

        return ans
    
s = "aba"
s = "aabac"
s = "aabcc"
s = "abcbc"
s = "bbcba"
s = "abcaaaa"
s = "bacabba"
s = "ccbacccca"

Solution().longestBalanced(s)