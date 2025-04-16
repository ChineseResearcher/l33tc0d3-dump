# number theory - medium
class Solution:
    def countHomogenous(self, s: str) -> int:
        n = len(s)
        # for contiguous homogenous array of length k
        # there can be k * (k+1) // 2 subarrays.
        contiguousCnt = 1

        ans = 0
        for i in range(1, n):
            if s[i] != s[i-1]:
                # collect result for curr. homo arr.
                ans += contiguousCnt * (contiguousCnt + 1) // 2
                ans %= int(1e9 + 7)
                # reset
                contiguousCnt = 1
            else:
                contiguousCnt += 1
                
        # collect last
        ans += contiguousCnt * (contiguousCnt + 1) // 2
        ans %= int(1e9 + 7) 

        return ans
    
s = "abbcccaa"
s = "xy"
s = "zzzzz"

Solution().countHomogenous(s)