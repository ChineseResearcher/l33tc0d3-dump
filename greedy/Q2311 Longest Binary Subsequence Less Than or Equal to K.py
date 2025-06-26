# greedy - medium
class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        # greedy soln turns out to be more straightforward
        # than DP, we just have to keep reducing the "1"s from the front
        # to see when does the decimal value fall below k

        n = len(s)
        rSum = 0 # keep tracking of leading 0s

        discarded, j = set(), 0
        while True:
            
            one_present = False
            for idx in range(j, n):

                char = s[idx]
                if char == '1' and idx not in discarded:
                    discarded.add(idx)
                    j = idx + 1 # reuse travelled pointer
                    one_present = True
                    break

                if char == '0':
                    rSum += 1

            if not one_present:
                rSum -= 1    

            if int(s[idx:], 2) <= k:
                break

        return rSum + (n-idx)
    
s, k = "1001010", 5
s, k = "00101001", 1
s, k = "0", 583196182
s, k = "001010101011010100010101101010010", 93951055

Solution().longestSubsequence(s, k)