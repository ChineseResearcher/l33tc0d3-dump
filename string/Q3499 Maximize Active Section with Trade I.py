# string - medium
class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:

        n = len(s)
        fmax = lambda a, b: a if a > b else b
        # strip the left/right tail 'ones'
        s = s.lstrip('1').rstrip('1')

        # if string has become empty, e.g. '1111' -> '', n active section(s)
        if not s: return n

        # idea is to enumerate all regions of contiguous "ones"
        # record the regions in intervals form in an arr
        active, one_cnt = [], n - len(s)

        # update length
        n = len(s)

        seqHead = -1
        for i in range(1, n):
            
            if s[i] == '1':
                one_cnt += 1
                
            if s[i] == '1' and s[i-1] == '0':
                seqHead = i
                
            if i < n-1 and s[i] == '1' and s[i+1] == '0':
                active.append([seqHead, i])
                
        ans = one_cnt
        # explore diff. contiguous blocks of "ones"
        m = len(active)
        for i in range(m):
            
            l, r = active[i]
            # count '0's to the left
            left_zero = l - active[i-1][1] - 1 if i > 0 else l
            
            # count '0's to the right
            right_zero = active[i+1][0] - r - 1 if i < m-1 else n - r - 1
            
            ans = fmax(ans, one_cnt + left_zero + right_zero)
            
        return ans
    
s = "01"
s = "0100"
s = "01010"
s = "1000100"

Solution().maxActiveSectionsAfterTrade(s)