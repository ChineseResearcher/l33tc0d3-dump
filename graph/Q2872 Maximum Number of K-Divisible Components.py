# graph - hard
class Solution:
    def dfs(self, curr, parent):
        
        # assume we are rooted at node 0 and we dfs down the tre
        component_sum = self.values[curr]
        for child in self.tree_connect[curr]:
            
            # make sure we are only dfs down the tree
            if child != parent:
                component_sum += self.dfs(child, curr)
                    
        if component_sum % self.k == 0:
            self.ans += 1
            # since we've identified a tree component with sum divisible by k
            # we return 0 to indicate a cutting from its parent
            return 0
        else:     
            return component_sum

    def maxKDivisibleComponents(self, n, edges, values, k):
        self.values, self.k = values, k
        # first build the tree connections
        self.tree_connect = {i:[] for i in range(n)}

        for e in edges:
            self.tree_connect[e[0]].append(e[1])
            self.tree_connect[e[1]].append(e[0])
            
        self.ans = 0
        # define a dummy parent -1 and call from root 0
        _ = self.dfs(0, -1)

        return self.ans

n, edges, values, k = 7, [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6]], [3,0,6,1,5,2,1], 3
n, edges, values, k = 5, [[0,2],[1,2],[1,3],[2,4]], [1,8,1,4,4], 6

Solution().maxKDivisibleComponents(n, edges, values, k)