# counting - medium
class Solution:
    def countServers(self, grid) -> int:
        m, n = len(grid), len(grid[0])
        # two servers are said to be communicating if they are on the same row/col
        # even if they are not adjacent to one another

        # maintain the locations of servers in a dict of sets
        # <row i: server at col j> & <col i: server at row j>
        row_loc, col_loc = {r:set() for r in range(m)}, {c:set() for c in range(n)}

        servers = set()
        for r in range(m):
            for c in range(n):

                if grid[r][c] == 1:
                    row_loc[r].add(c)
                    col_loc[c].add(r)

                    servers.add((r,c))

        # iterate through servers again to obtain the count
        ans = 0
        for r, c in servers:

            # check if in the same row/col, there's another server
            if (row_loc[r] - set([c])) or (col_loc[c] - set([r])):
                ans += 1

        return ans
    
grid = [[1,0],[0,1]]
grid = [[1,0],[1,1]]
grid = [[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]

Solution().countServers(grid)