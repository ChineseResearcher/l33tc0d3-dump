# prefix sum - medium
import bisect
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        
        n = len(s)
        # first record the indices of "0"
        zi = [i for i in range(n) if s[i] == '0']

        # record number of "0"s
        m = len(zi)

        # append a dummy index to the back 
        zi.append(n)

        # prepare a prefix sum of "1" in s
        rSum, pf_o = 0, []
        for i in range(n):
            if s[i] == '1':
                rSum += 1
            pf_o.append(rSum)

        # range-query for prefix sum helper
        def rq(arr, l, r):

            l_res = arr[l] if l >= 0 else 0
            r_res = arr[r] if r >= 0 else 0
            return r_res - l_res

        # O(n) outer loop to explore every s[i] as the head of substring
        ans = 0
        for i in range(n):

            # locate index i in the list of "0" indices
            j = bisect.bisect_left(zi, i)

            # curr. substring length
            sl = n-i

            # also determine the upper bound for number of "0"s to explore
            ub = int(sl ** 0.5) + 1

            pzi = i - 1
            for k in range(j, min(j + ub, len(zi))):

                # curr. zero's index in s
                czi = zi[k]

                # compute number of 0 in range [i...czi]
                if czi == n:
                    z = m - j
                    czi -= 1
                else:
                    z = k - j # we only count the "0"s before czi

                o_pf = rq(pf_o, i-1, pzi)
                o_curr = rq(pf_o, pzi, czi)

                if o_curr > 0:
                    
                    excl = pow(z, 2) - o_pf
                    if excl <= 0:
                        ans += o_curr
                    else:
                        increment = o_curr - excl + 1
                        if increment > 0:
                            ans += increment       

                if z > 0 and o_pf >= pow(z, 2):
                    ans += 1

                pzi = czi

        return ans

s = "00011"
s = "101101"
# constraint
s = "1" * 50 + "0" * 39900 + "1" * 50

Solution().numberOfSubstrings(s)