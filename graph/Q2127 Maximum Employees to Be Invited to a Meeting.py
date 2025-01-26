# graph - hard
class Solution:
    def compute_cycle_size(self, node, path_pos, pos):
        # by relying on the path_pos dict which stores <node, visited_order>
        # we can compute the cycle count (guaranteed to be larger than 2) in a network given

        self.visited.add(node)
        # terminal cond: we found a repeating member
        if node in path_pos:
            return pos - path_pos[node]

        # each person only has one favorite
        path_pos[node] = pos
        return self.compute_cycle_size(self.favorite[node], path_pos, pos+1)

    def dfs_length(self, node, avoid):
        # for a special case of 2-member cycle
        # check the potential longest acyclic chain at each end

        self.visited.add(node)
        if not self.inEdge[node]:
            return 1
        
        maxDepth = 0
        for inNode in self.inEdge[node]:
            # avoid visiting the other node in the cycle
            if inNode != avoid:
                maxDepth = max(maxDepth, 1+self.dfs_length(inNode, avoid))
            
        return maxDepth

    def maximumInvitations(self, favorite) -> int:
        ### three non-trivial observations:

        # 1) for this problem to have a solution, a cycle must exist
        # hence, any soln has to involve at least one cycle

        # 2) soln case 1: select the biggest cycle 

        # 3) soln case 2: select all 2-member cycles, and add the length(s) of potentially
        # acyclic chains to each end of a 2-member cycle to the soln

        n = len(favorite)
        self.favorite = favorite
        # build in-edges
        self.inEdge = [[] for _ in range (n)]
        for i in range(n):

            self.inEdge[self.favorite[i]].append(i)

        # maintain a global var
        self.visited = set()

        case2 = 0
        for i in range(n):

            # detect special case of two-member cycle
            if favorite[favorite[i]] == i and i not in self.visited:
                case2 += 2 + \
                        max(0, self.dfs_length(i, self.favorite[i])-1) + \
                        max(0, self.dfs_length(self.favorite[i], i)-1)

        case1 = 0    
        for i in range(n):

            if i not in self.visited:
                case1 = max(case1, self.compute_cycle_size(i, dict(), 0))

        return max(case1, case2)
        
favorite = [2,2,1,2]
favorite = [1,2,0]
favorite = [3,0,1,4,1]
favorite = [1,0,3,2,5,6,7,4,9,8,11,10,11,12,10]

Solution().maximumInvitations(favorite)