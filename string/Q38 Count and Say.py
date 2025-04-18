# string - medium
class Solution:
    def countAndSay(self, n):

        # we have to solve this iteratively
        # i.e. we have no knowledge of countAndSay(n) unless we know the RLE of n-1

        # start from base = 1, with base string = '1'
        curr_str = '1'

        for i in range(n-1):

            # think of the subarray processing like a sliding window
            RLE = ''
            l = 0
            strLength = len(curr_str)

            for r in range(strLength):
                c = curr_str[r]
                
                if r > 0 and c != curr_str[l]:
                    RLE += str(r-l) + curr_str[l]
                    l = r # window shifted

                if r == strLength - 1:
                    RLE += str(r-l+1) + curr_str[r]

            curr_str = RLE

        return curr_str
    
n = 1
n = 5
n = 30

Solution().countAndSay(n)