# greedy - medium
class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        # locate the first index where it is smaller than prev
        # and lower that prev digit & append remaining length with '9's

        n = str(n)

        while True:
            
            updated = False
            for i in range(1, len(n)):
                if n[i] < n[i-1]:

                    if i-1 == 0:
                        # e.g. 1001
                        n = str(int(n[i-1])-1) + (len(n)-1) * '9'
                    else:
                        # e.g. 1100
                        n = n[:(i-1)] + str(int(n[i-1])-1) + (len(n)-i) * '9'

                    # strip leading zeros
                    n = n.lstrip('0')

                    updated = True
                    break
            
            if not updated:
                break

        return int(n)
    
n = 1100
n = 1234
n = 332
n = 333

Solution().monotoneIncreasingDigits(n)