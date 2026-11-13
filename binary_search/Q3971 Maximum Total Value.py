# binary search - hard
class Solution:
    def maxTotalValue(self, value: list[int], decay: list[int], m: int) -> int:

        n = len(value)
        fmax = lambda a, b: a if a > b else b
        # key ideas:
        # 1) the total selection size is monotonic, i.e. as we increase some threshold
        # to include our elements (including the decayed), the selection size becomes smaller

        # 2) binary search on the maximum "t" s.t. we include all values[i]
        # and its decayed series in the selection if the selection size >= m

        # 3) why find the maximum "t"? this is because when we set t as large as possible,
        # the selected values will also be large, thus greedily maximising t while ensuring
        # total selection size >= m is the optimal strategy

        # helper to find lower bound and length of arithemtic series
        # given upper bound x, cutoff t, and step size s
        def g(x: int, t:int, s: int) -> tuple[int, int]:
            # obtain lower bound
            y = x - ((x - t) // s) * s
            # obtain length of series [y, y + decay, y + 2 * decay, ..., x]
            c = ((x - y) // s) + 1
            return y, c

        def f(t: int) -> bool:
            c_acc = 0
            for i, x in enumerate(value):
                if x < t: continue
                y, c = g(x, t, decay[i])
                c_acc += c    
            return c_acc >= m

        l, r, max_t = 1, max(value), 0
        while l <= r:
            mid = (l + r) >> 1
            if f(mid):
                max_t = fmax(max_t, mid)
                l = mid + 1
            else:
                r = mid - 1

        ans, c_acc = 0, 0
        for i, x in enumerate(value):
            if x < max_t: continue
            y, c = g(x, max_t, decay[i])
            # add arithmetic sum to answer
            ans += c * (x + y) // 2
            c_acc += c

        # discount answer with the max. threshold value
        # why are we guaranteed that all extra copies = t exactly?
        # suppose we want to choose from array [1,2,8,8,9], and we want at least 2 elements
        # if we set t = 8, we get 3 elements, and once we cross over to t = 9,
        # our selection size reduces to 1, and binary search is to help us locate the max.
        # threshold that ensures selection of 3, so it will not stop when t is in range [3, 7]
        if c_acc > m: ans -= (c_acc - m) * max_t
        return ans % int(1e9 + 7)

value, decay, m = [6], [4], 8
value, decay, m = [4,3], [5,4], 5
value, decay, m = [5,7], [4,3], 1
value, decay, m = [9,9,7], [1,5,2], 2
value, decay, m = [6,5,4], [2,1,1], 4
value, decay, m = [7,2,2], [3,2,1], 2
value, decay, m = [9,10,7], [1,2,8], 7

Solution().maxTotalValue(value, decay, m)