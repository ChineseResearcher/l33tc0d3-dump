# binary search - hard
from typing import List
import bisect
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:

        n = len(envelopes)
        # there's a need to sort width ascending and height descending
        # otherwise, when we encounter a new envelop w/ greater height but the same
        # width as previous, then just by looking at the height we would
        # erroneously include this new envelop as a candidate in the LIS
        e = sorted(envelopes, key = lambda x: (x[0], -x[1]))

        # because we are just interested in the length of LIS and not the
        # actual subsequence itself, we could use sorting + binary search to achieve O(nlogn) TC
        h_subseq = []
        # since width are sorted in asc. order already
        # we "reduce" the problem into finding LIS in the height dimension
        for _, h in e:

            j = bisect.bisect_left(h_subseq, h)
            # if new height is strictly larger than the curr. largest
            # we expand the container by length 1
            if j == len(h_subseq):
                h_subseq.append(h)

            # otherwise, we make a swap w/ the index j
            else:
                h_subseq[j] = h

        return len(h_subseq)
    
envelopes = [[5,4],[6,4],[6,7],[2,3]]
envelopes = [[1,3],[2,2],[3,3],[3,4]]
envelopes = [[1,3],[3,5],[6,7],[6,8],[8,4],[9,5]]
envelopes = [[1,2],[2,3],[3,4],[4,5],[5,6],[5,5],[6,7],[7,8]]
envelopes = [[1,2],[2,3],[3,4],[3,5],[4,5],[5,5],[5,6],[6,7],[7,8]]

Solution().maxEnvelopes(envelopes)