# backtracking - medium
from collections import Counter
class Solution:
    def recursive_tile_formation(self, seq, usage):

        if seq: self.soln.append(''.join(seq))

        if len(seq) == len(self.tiles):
            return
        
        for tile, f in usage.items():
            if f > 0:
                seq.append(tile)
                usage[tile] -= 1

                self.recursive_tile_formation(seq, usage)

                # backtacking
                seq.pop()
                usage[tile] += 1

    def numTilePossibilities(self, tiles: str) -> int:
        self.tiles = tiles
        self.soln = []

        self.recursive_tile_formation([], Counter(tiles))
        return len(self.soln)
    
tiles = "AAB"
tiles = "AAABBC"
tiles = "V"

Solution().numTilePossibilities(tiles)