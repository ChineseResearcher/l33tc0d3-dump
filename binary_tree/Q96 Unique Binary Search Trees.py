# binary tree - medium
import math
class Solution:
    def nCk(self, n, k):
        return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))

    def recursiveBTree(self, cumu_nodes, cumu_ways, last_node_cnt):
        if cumu_nodes == self.n:
            self.ans += cumu_ways
            return

        # our current level's available nodes would have to depend on
        # the number of chosen nodes from the previous level
        curr_avail_nodes = 2*last_node_cnt
        for choice in range(1, curr_avail_nodes+1):
            # we can only choose up to n node
            if choice <= self.n - cumu_nodes:
                ways = self.nCk(curr_avail_nodes, choice)
                self.recursiveBTree(cumu_nodes+choice, cumu_ways*ways, choice)

    def numTrees(self, n: int) -> int:
        self.n = n
        self.ans = 0

        self.recursiveBTree(1,1,1)
        return self.ans
    
n = 5
n = 1
n = 7

Solution().numTrees(n)