# number theory - medium
class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:

        m = 1
        # just need to enumerate all powers of 2 up to n
        # and check if this number can be assembled from n, w/ re-ordering
        while len(str(m)) <= len(str(n)):

            if sorted(str(m)) == sorted(str(n)):
                return True
            m <<= 1

        return False
    
n = 1
n = 35566

Solution().reorderedPowerOf2(n)