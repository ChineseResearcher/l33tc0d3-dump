# counting - medium
class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        
        def oe_count(size):

            if size % 2 == 0:
                o, e = size // 2, size // 2
            else:
                o, e = size // 2 + 1, size // 2

            return o, e

        # first lane
        fl_o, fl_e = oe_count(n)

        # second lane
        sl_o, sl_e = oe_count(m)

        # for alice to win, the total number of flowers
        # from both lanes must be odd
        return fl_o * sl_e + fl_e * sl_o
    
n, m = 3, 2
n, m = 1, 1

Solution().flowerGame(n, m)