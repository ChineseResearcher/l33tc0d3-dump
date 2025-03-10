# sliding window - medium
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        # s only made up of characters 'a', 'b' and 'c'
        # the approach to fully count the # of substrings is similar
        # to LC3306, where we maintain a dict to store the last seen
        # idx at which our desired chars (a,b,c) occur
        abcIdx = {'a':-1, 'b':-1, 'c':-1}

        ans = 0
        for i in range(n):

            # mark s[i]'s index
            abcIdx[s[i]] = i

            if all(idx >= 0 for idx in abcIdx.values()):
                ans += min(abcIdx.values()) + 1

        return ans
    
s = "abcabc"
s = "caaaab"
s = "aaacb"
s = "abc"

Solution().numberOfSubstrings(s)