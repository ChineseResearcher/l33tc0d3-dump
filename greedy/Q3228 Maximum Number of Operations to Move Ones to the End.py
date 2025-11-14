# greedy - medium
class Solution:
    def maxOperations(self, s: str) -> int:

        # track zero and one count
        z, o = 0, 0

        ans = 0
        for char in s:

            if char == '1':
                # shift operations
                if z > 0:
                    ans += o
                    # reset zero count
                    z = 0
                o += 1 # increment 1

            else:
                z += 1

        # deal with '1's that have yet to be shifted
        if z > 0:
            ans += o

        return ans

s = "1001101"
s = "00111"
s = "110"

Solution().maxOperations(s)