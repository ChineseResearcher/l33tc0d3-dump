# dp - hard
from typing import List
from functools import cache
from collections import defaultdict
class Solution:
    def minimumTotalPrice(self, n: int, edges: List[List[int]], price: List[int], trips: List[List[int]]) -> int:
  
        # key ideas:
        # 1) our final total cost is price[i] * freq[i] where freq[i] is the number of
        # times node i is visited considering all trips
        # 2) first use a dfs process to compute such freq[i] for all nodes
        # 3) then solve a knapsack DP problem to derive the optimal discounting regime 

        g = defaultdict(set)
        for u, v in edges:
            g[u].add(v)
            g[v].add(u)

        def dfs(curr:int, prev: int, dest:int) -> bool:

            if curr == dest:
                freq[curr] += 1
                return True
            
            is_on_path = False
            for neighbour in g[curr]:
                if neighbour != prev:
                    is_on_path |= dfs(neighbour, curr, dest)

            if is_on_path:
                freq[curr] += 1

            return is_on_path

        freq = [0] * n
        for u, v in trips:
            _ = dfs(u, -1, v)

        # we need to root our tree at certain node (say node 0), and make it directed
        # this is to facilitate the set-up of our dp problem below
        def reroot(curr:int, prev:int) -> None:

            g[curr].discard(prev)
            for neighbour in g[curr]:
                _ = reroot(neighbour, curr)

        _ = reroot(0, -1)

        @cache
        def f(curr:int, prev_is_halved:bool) -> int:

            ud = price[curr] * freq[curr]
            for neighbour in g[curr]:
                ud += f(neighbour, False)

            if prev_is_halved: # then no do discounting at curr. node
                return ud

            # otherwise, we can minimise between undiscounted & discounted
            d = (price[curr] // 2) * freq[curr]
            for neighbour in g[curr]:
                d += f(neighbour, True)

            return min(ud, d)

        return f(0, False)

n, edges, price, trips = 2, [[0,1]], [2,2], [[0,0]]
n, edges, price, trips = 4, [[0,1],[1,2],[1,3]], [2,2,10,6], [[0,3],[2,1],[2,3]]

Solution().minimumTotalPrice(n, edges, price, trips)