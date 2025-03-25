# dp - medium
class Solution:
    def recursive_path(self, currNode, currStopsLeft):
        # one realisation is that there's no need to maintain visited
        # as we have a limit of stops being made anyways

        # terminal condition 1: reached destination
        if currNode == self.dst:
            return 0
            
        # terminal condition 2: exit when k stops have all been used
        if currStopsLeft < 0:
            return float('inf')

        # terminal condition 3: reached a city with no outbound flights:
        if currNode not in self.flight_dict:
            return float('inf')

        # return memoized result
        if (currNode, currStopsLeft) in self.dp:
            return self.dp[(currNode, currStopsLeft)]
            
        cost = float('inf')
        for x in self.flight_dict[currNode]:
            # make sure we do not repeat visiting
            next_cost = self.recursive_path(x[0], currStopsLeft - 1)
            cost = min(cost, x[1] + next_cost)

        # memoization
        self.dp[(currNode, currStopsLeft)] = cost

        return cost

    def findCheapestPrice(self, n, flights, src, dst, k):
        self.flight_dict = dict() # storing <from: [[to_1, cost1, ...]]>
        for x in flights:

            dep, arr, cost = x[0], x[1], x[2]
            if dep not in self.flight_dict:
                self.flight_dict[dep] = []

            self.flight_dict[dep].append([arr, cost])

        self.dp = dict()
        self.src, self.dst, self.k = src, dst, k
        ans = self.recursive_path(self.src, self.k)

        return ans if ans < float('inf') else -1
    
n, flights, src, dst, k = 4, [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], 0, 3, 1
n, flights, src, dst, k = 3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 1
n, flights, src, dst, k = 3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2, 0
n, flights, src, dst, k = 5, [[4,1,1],[1,2,3],[0,3,2],[0,4,10],[3,1,1],[1,4,3]], 2, 1, 1
n, flights, src, dst, k = 5, [[3,0,8],[1,4,1],[1,0,4],[1,3,3],[3,4,1],[2,3,3],[2,0,10]], 1, 4, 4
n, flights, src, dst, k = 5, [[0,1,100],[0,2,100],[0,3,10],[1,2,100],[1,4,10],[2,1,10],[2,3,100],[2,4,100],[3,2,10],[3,4,100]], 0, 4, 3

Solution().findCheapestPrice(n, flights, src, dst, k)