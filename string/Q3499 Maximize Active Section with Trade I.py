# string - medium
class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        n = len(s)
        # strip the left/right tail 'ones'
        s = s.lstrip('1').rstrip('1')

        # idea is to enumerate all regions of contiguous "ones"
        # record the regions in intervals form in an arr
        active, one_cnt = [], n - len(s)

        # update length
        n = len(s)

        # if string has become empty, e.g. '1111' -> '', return one_cnt 
        if not s:
            return one_cnt

        seqHead = None
        for i in range(n):
            
            if s[i] == '1':
                one_cnt += 1
                
            if i > 0 and s[i-1] == '0' and s[i] == '1':
                seqHead = i
                
            if 0 < i < n-1 and s[i] == '1' and s[i+1] == '0':
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
            
            ans = max(ans, one_cnt + left_zero + right_zero)
            
        return ans
    
s = "01"
s = "0100"
s = "1000100"
s = "01010"

Solution().maxActiveSectionsAfterTrade(s)