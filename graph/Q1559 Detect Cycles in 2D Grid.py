# graph - medium
from typing import List
from collections import deque
class UnionFind:
    def __init__(self, size:int):
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, i:int) ->int:
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i:int, j:int) -> None:
        root_i = self.find(i)
        root_j = self.find(j)

        if root_i != root_j:
            if self.rank[root_i] < self.rank[root_j]:
                self.parent[root_i] = root_j
            elif self.rank[root_i] > self.rank[root_j]:
                self.parent[root_j] = root_i
            else:
                self.parent[root_j] = root_i
                self.rank[root_i] += 1

    def connected(self, i:int, j:int) -> bool:
        return self.find(i) == self.find(j)
        
class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:

        m, n = len(grid), len(grid[0])
        # key ideas:
        # 1) use a BFS process to visit cells of the same char.
        # 2) build a DSU that would group two nodes if they are the same char.
        # and if we encounter a node which is already connected before unioning
        # we confirm the existence of a cycle

        dsu = UnionFind(m * n)
        visited = set()
        delta = [(0,1),(0,-1),(1,0),(-1,0)]

        for r in range(m):
            for c in range(n):
                if (r, c) not in visited:
                    
                    visited.add((r,c))
                    q = deque([(r,c,-1,-1)])
                    while q:
                        
                        # (pr, pc) is the prev. cell
                        r, c, pr, pc = q.popleft()
                        for dr, dc in delta:
                            nr, nc = r + dr, c + dc
                            if 0 <= nr < m and 0 <= nc < n:
                                if (nr, nc) != (pr, pc) and grid[nr][nc] == grid[r][c]:
                                    
                                    # cycle found
                                    curr_1d = r * n + c - 1
                                    next_1d = nr * n + nc - 1
                                    if dsu.connected(curr_1d, next_1d):
                                        return True
                                    
                                    # union two cells
                                    dsu.union(curr_1d, next_1d)

                                    q.append((nr,nc,r,c))
                                    visited.add((nr,nc))
                                    
        return False
    
grid = [["a","b","b"],["b","z","b"],["b","b","a"]]
grid = [["a","a","a","a"],["a","b","b","a"],["a","b","b","a"],["a","a","a","a"]]
grid = [["c","c","c","a"],["c","d","c","c"],["c","c","e","c"],["f","c","c","c"]]

Solution().containsCycle(grid)