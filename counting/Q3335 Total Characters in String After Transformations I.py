class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        
        # build a counter array which gets updated for every transformation
        # freq[i] denotes the number of letters[i] we have 
        freq = [0] * 26

        # init. freq with letter frequencies of "s"
        for char in s:
            freq[ord(char) - ord("a")] += 1

        MOD = int(1e9 + 7)
        for _ in range(t):

            # store count of 'z's
            z_cnt = freq[-1]

            # inherit count from reverse direction:
            # i.e. "z" from "y", ..., up to "b" from "a"
            # Note: "a" gets reset to 0
            for j in range(25, 0, -1):
                freq[j] = freq[j-1]

            freq[0] = 0
            # increment both "a" & "b" by count of z from prev round
            # as any "z"s gets transformed into "ab" 
            freq[0] += z_cnt % MOD
            freq[1] += z_cnt % MOD

        return sum(freq) % MOD

s, t = "abcyy", 2
s, t = "azbk",  1

Solution().lengthAfterTransformations(s, t)