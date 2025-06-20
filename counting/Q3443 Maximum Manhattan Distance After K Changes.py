# counting - medium
class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        ans = 0
        north = south = west = east = 0
        for char in s:

            if char == 'N':
                north += 1
            elif char == 'S':
                south += 1
            elif char == 'W':
                west += 1
            elif char == 'E':
                east += 1

            # we can calculate the Manhattan dist.
            # by summing and find net. displacements vertically & horizontally
            net = abs(north - south) + abs(west - east)

            # by replacing optimally, for can recoup back 2 units
            # of dist. for each replaced char
            # note: we are bounded by k replacements available
            re = min(min(north, south) + min(west, east), k) * 2
            ans = max(ans, net + re)

        return ans
    
s, k = "NWSE", 1
s, k = "NSWWEW", 3
s, k = "NSES", 1
s, k = 'ENNSW', 1
s, k = "EWWE", 1

Solution().maxDistance(s, k)