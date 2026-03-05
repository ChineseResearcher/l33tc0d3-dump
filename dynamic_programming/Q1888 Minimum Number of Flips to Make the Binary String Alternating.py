# dp - medium
class Solution:
    def minFlips(self, s: str) -> int:
        
        n = len(s)
        fmin = lambda a, b: a if a < b else b

        o = {"0":0, "1":0}
        e = {"0":0, "1":0}

        for i, x in enumerate(s):
            if i % 2 == 0:
                e[x] += 1
            else:
                o[x] += 1

        # define k as the number of flipping ops required
        # to convert string into "1010..."
        k = e['0'] + o['1']
        ans = fmin(k, n-k)

        # start shifting front chars to the end
        for x in s:
            e[x] -= 1
            o, e = e, o
            if n % 2 == 0:
                o[x] += 1
            else:
                e[x] += 1

            k = e['0'] + o['1']
            ans = fmin(ans, fmin(k, n-k))

        return ans

s = "010"
s = "1110"
s = "111000"

Solution().minFlips(s)