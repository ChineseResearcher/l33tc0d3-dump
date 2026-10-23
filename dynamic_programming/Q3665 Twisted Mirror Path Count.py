# dp - medium
MOD = int(1e9 + 7)
class Solution:
    def uniquePaths(self, grid: list[list[int]]) -> int:

        M, N = len(grid), len(grid[0])
        # key ideas:
        # 1) use top-down DP to first compute the ending position by entering
        # every mirror cell from both directions
        # 2) use bottom-up for optimized counting of unique paths

        p = [ [[None] * 2 for _ in range(N)] for _ in range(M) ]
        def endPos(r: int, c: int, enterDir: int) -> tuple[int, int]:
            if grid[r][c] != 1:
                return (r, c)
            if p[r][c][enterDir]:
                return p[r][c][enterDir]
            res = (-1, -1)
            # move right into mirror
            if enterDir == 0 and r + 1 < M:
                res = endPos(r + 1, c, 1 - enterDir)
            # move down into mirror
            elif enterDir == 1 and c + 1 < N:
                res = endPos(r, c + 1, 1 - enterDir)
            p[r][c][enterDir] = res
            return res

        for r in range(M):
            for c in range(N):
                if grid[r][c] == 1:
                    if c > 0:
                        _ = endPos(r, c, 0)
                    if r > 0:
                        _ = endPos(r, c, 1)

        dp = [ [0] * N for _ in range(M) ]
        dp[M - 1][N - 1] = 1
        for r in range(M - 1, -1, -1):
            for c in range(N - 1, -1, -1):
                if grid[r][c] == 0:
                    if c + 1 < N:
                        if grid[r][c + 1] == 1:
                            npos = p[r][c + 1][0]
                            if npos and npos != (-1, -1):
                                nr, nc = npos
                                dp[r][c] += dp[nr][nc]
                        else:
                            dp[r][c] += dp[r][c + 1]
                    if r + 1 < M:
                        if grid[r + 1][c] == 1:
                            npos = p[r + 1][c][1]
                            if npos and npos != (-1, -1):
                                nr, nc = npos
                                dp[r][c] += dp[nr][nc]
                        else:
                            dp[r][c] += dp[r + 1][c]
                    dp[r][c] %= MOD

        return dp[0][0]

grid = [[0,0],[0,0]]
grid = [[0,1,1],[1,1,0]]
grid = [[0,1,0],[0,0,1],[1,0,0]]

Solution().uniquePaths(grid)