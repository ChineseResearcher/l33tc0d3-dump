# heap - hard
import string
import heapq
class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        
        n = len(password)
        # first define the booleans to check for the three conds.
        hasLC, hasUC, hasDigit = False, False, False
        # second thing is to break down password into contiguous blocks
        blocks, l = [], 0

        for r in range(n):
            curr = password[r]

            if not hasLC and curr in string.ascii_lowercase:
                hasLC = True
            if not hasUC and curr in string.ascii_uppercase:
                hasUC = True
            if not hasDigit and curr in string.digits:
                hasDigit = True

            # groupby
            if r > 0 and curr != password[r-1]:
                blocks.append([password[l], r-l])
                l = r
            
            if r == n-1:
                # collect last
                blocks.append([password[l], r-l+1])

        # define lack as the conditions that have yet to be fulfilled
        lack = 3 - sum([hasLC, hasUC, hasDigit])

        # as per hint, we need to discuss solution separately
        # to the following cases, note that for every length-3
        # contiguous block there's one op at least to correct

        # scan through "blocks" and compute the three-repeat violations
        repCnt = 0
        for _, length in blocks:
            repCnt += length // 3 

        if n <= 6:
            return max(6-n, max(lack, repCnt))

        elif 6 < n <= 20:
            # if the length of password is already of satisfying length
            # we only perform "replace" operation as the optimal move
                return max(repCnt, lack)

        else:
            # for password already exceeding max. length allowed
            # we need to make use of minheap to delete some blocks
            minheap = []
            for char, length in blocks:
                # only handle blocks that would have length violations
                if length >= 3:
                    # the biggest challenge lies in why do we need to
                    # order the minheap by length MOD 3, suppose we only
                    # have two blocks: 'a' w/ length 6, 'b' w/ length 7
                    # op1: remove 1 char from 'a'
                    # op2: remove 1 char from 'b'
                    # it is clear that combining the follow-up replacements
                    # needed, removing op1 would be more optimal as it leads
                    # to fewer replacements needed afterwards
                    # Note: when there's a tie on MOD 3, break tie by the larger length
                    # this is because reduction priority is given to longer repeated block
                    heapq.heappush(minheap, [length % 3, -length, char])

            deleteOps = 0
            while minheap and n > 20:
                _, length, char = heapq.heappop(minheap)
                length = abs(length) - 1
                if length > 0:
                    heapq.heappush(minheap, [length % 3, -length, char])
                n -= 1
                # tabulate number of deletion operations
                deleteOps += 1
            
            if n > 20: deleteOps += n-20

            # after reducing n to at most length 20, it degenerates into
            # the case of 6 < n <= 20, and we compute repCnt again
            repCnt = 0
            for _, length, _ in minheap:
                repCnt += abs(length) // 3 
            return max(repCnt, lack) + deleteOps
        
password = "1337C0d3"
password = "aA1"
password = "aaaAAA"
password = "......"
password = "..."
password = "b1111"
password = "bbaaaaaaaaaaaaaaacccccc"
password = "ABABABABABABABABABAB1"
password = "A1234567890aaabbbbccccc"
password = "aaaaaa1234567890123Ubefg"

Solution().strongPasswordChecker(password)