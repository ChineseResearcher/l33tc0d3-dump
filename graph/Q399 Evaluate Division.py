# graph - medium
from collections import deque
class Solution:
    def calcEquation(self, equations, values, queries):
        
        # question provides values[i] as the hypothetical division result
        # to equations[i][0] / equations[i][1], where the numerators and
        # denominators are defined as a string with length <= 5
        n = len(equations)

        # in terms of building the "edges", we would have bidirectional
        # edges with different "weights", that is given 'a' / 'b' = 2.0
        # one edge is a -> b with weight 2, and another is b -> a with weight 0.5
        edges = dict()
        for i in range(n):

            numer, denom = equations[i][0], equations[i][1]
            # build bi-directional edges
            if numer not in edges:
                edges[numer] = dict()
            if denom not in edges:
                edges[denom] = dict()

            edges[numer][denom] = values[i]
            edges[denom][numer] = 1 / values[i]

        # since the number of queries is small, we can run bfs for each query
        # starting from node = query[i][0], and ending at query[i][1] if such a path exists
        ans = []
        for u, v in queries:

            # invalid starting point
            if u not in edges:
                ans.append(-1)
                continue
            
            currAns = -1
            # otherwise we init. bfs queue
            bfs_queue = deque([[u, 1]])
            visited = set([u])
            while bfs_queue:

                curr, cumuProd = bfs_queue.popleft()
                # found the denom
                if curr == v:
                    currAns = cumuProd
                    break

                for neighbour, div_val in edges[curr].items():
                    if neighbour not in visited:
                        bfs_queue.append([neighbour, cumuProd * div_val])
                        visited.add(neighbour)

            ans.append(currAns)

        return ans
    
equations, values, queries = [["a","b"],["b","c"]], [2.0,3.0], [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
equations, values, queries = [["a","b"],["b","c"],["bc","cd"]], [1.5,2.5,5.0], [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
equations, values, queries = [["a","b"]], [0.5], [["a","b"],["b","a"],["a","c"],["x","y"]]

Solution().calcEquation(equations, values, queries)