# sliding window - medium
class Solution:
    def balancedString(self, s: str) -> int:
        # we know that Q,W,E,R each only appear n/4 times
        # suppose we iterate through string in forward & backward manner
        # we want to locate the first violation idx identified in forward & backward scan altogether

        n = len(s)
        freq_cap = n // 4

        iterated_freq = {'Q':0, 'W':0, 'E':0, 'R':0}
        l = None
        for i in range(n):

            currChar = s[i]
            iterated_freq[currChar] += 1

            if iterated_freq[currChar] > freq_cap:
                l = i
                break

        # take care of already balanced string
        if l is None:
            return 0

        r, ans = n-1, float('inf')
        for i in range(l, -1, -1):

            iterated_freq[s[i]] -= 1

            shifted = True if max(iterated_freq.values()) <= freq_cap else False  
            while max(iterated_freq.values()) <= freq_cap:

                iterated_freq[s[r]] += 1
                r -= 1

            if shifted:
                ans = min(ans, r+1-i+1)

        return ans
    
s = "QWER"
s = "QQWE"
S = "QQQW"
s = "WWEQERQWQWWRWWERQWEQ"

Solution().balancedString(s)