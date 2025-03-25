# graph - hard
from collections import defaultdict, deque
class Solution:
    def numBusesToDestination(self, routes, source, target):

        n = len(routes)
        # create a dict to store <bus_stop_num, set(routes it belongs to)>
        route_dict = defaultdict(set)

        for i in range(n):
            for x in routes[i]:
                route_dict[x].add(i)

        # edge case 1: source = target
        if source == target: return 0 

        # edge case 2: source & target already in the same bus route
        if route_dict[source] & route_dict[target]:
            return 1

        # maintain a set to store the explored bus routes
        # init. to the set of routes that source is involved in
        explored = route_dict[source]
        bfs_queue = deque([(1, route_id) for route_id in explored])

        ans = -1
        while bfs_queue:

            cumu_hop, curr_route = bfs_queue.popleft()
            if curr_route in route_dict[target]:
                ans = cumu_hop
                break

            for bus_stop in routes[curr_route]:
                for r in route_dict[bus_stop]:
                    if r not in explored:
                        bfs_queue.append((cumu_hop+1, r))
                        explored.add(r)

        return ans
    
routes, source, target = [[1,2,7],[3,6,7]], 1, 6
routes, source, target = [[7,12],[4,5,15],[6],[15,19],[9,12,13]], 15, 12

Solution().numBusesToDestination(routes, source, target)