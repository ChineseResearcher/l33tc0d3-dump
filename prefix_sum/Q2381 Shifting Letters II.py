# prefix sum - medium
from string import ascii_lowercase as asc
class Solution:
    def shiftingLetters(self, s, shifts) -> str:     
        n = len(s)

        # key to solving this problem relies on marking increment/decrement
        # at the left and right + 1 idx of the given range

        # we need size n+1 because the decrement occurs after right bound
        # given that our bound/range here is exclusive on both ends
        diff = [0] * (n + 1)
        for l, r, v in shifts:

            # '0' in our context means left shift by 1
            v = -1 if v == 0 else v

            # increment on l
            diff[l] += v
            if r + 1 < len(diff):

                # decrement on r+1
                diff[r + 1] -= v

        pf_sum = 0
        # then our net_shifts arr. contains the final net shifts 
        # at each character idx after processing all shifts
        net_shifts = [0] * n
        for i in range(n):
            pf_sum += diff[i]
            net_shifts[i] = pf_sum

        # initiate a idx dictionary storing the relative pos of alphabets
        alphabet_idx = {char: idx for idx, char in enumerate(asc)}

        ans = []

        for idx, char in enumerate(s):

            asc_pos = alphabet_idx[char]
            # retrieve net shift
            ns = net_shifts[idx]

            ans.append(asc[(asc_pos + ns) % 26])

        return "".join(ans)

s, shifts = "abc", [[0,1,0],[1,2,1],[0,2,1]]
s, shifts = "dztz", [[0,0,0],[1,1,1]]

Solution().shiftingLetters(s, shifts)