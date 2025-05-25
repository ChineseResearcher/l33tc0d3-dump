# dp - hard
from typing import List
from collections import defaultdict
class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        
        m, n = len(edges), len(colors)

        graph, indeg = defaultdict(list), [0] * n
        for u, v in edges:
            graph[u].append(v)
            indeg[v] += 1

        def has_cycle(node):
            # for every node we run this dfs-based cycle checker

            # return memoized result
            if cache[node] == -1:
                return True
            if cache[node] == 1:
                return False

            # first mark currNode as unsafe until proven otherwise
            cache[node] = -1
            for neighbor in graph[node]:
                if has_cycle(neighbor):
                    return True
            
            # re-flag the currNode's status to 1 (backtracking)
            cache[node] = 1
            return False

        cache = [0] * n
        for node in range(n):
            if has_cycle(node):
                return -1
                
        # after the cycle checker, we would have been guaranteed a DAG
        # solve the problem w/ dp by dfs down from every node with indeg = 0
        def recursive_visit(currNode):
            
            if not graph[currNode]:
                return {colors[currNode]:1}
            
            if currNode in dp:
                return dp[currNode]
            
            curr_res = defaultdict(int)
            for neighbour in graph[currNode]:
                
                for k, v in recursive_visit(neighbour).items():
                    curr_res[k] = max(curr_res[k], v)
            
            # add currNode as well
            curr_res[colors[currNode]] += 1
            dp[currNode] = curr_res
            return curr_res

        dp, ans = dict(), 0
        for i in range(n):
            if indeg[i] == 0:
                ans = max(ans, max(recursive_visit(i).values()))
                
        return ans
    
colors, edges = "abaca", [[0,1],[0,2],[2,3],[3,4]]
colors, edges = "a", [[0,0]]
colors, edges = "hhqhuqhqff", [[0,1],[0,2],[2,3],[3,4],[3,5],[5,6],[2,7],[6,7],[7,8],[3,8],[5,8],[8,9],[3,9],[6,9]]

Solution().largestPathValue(colors, edges)