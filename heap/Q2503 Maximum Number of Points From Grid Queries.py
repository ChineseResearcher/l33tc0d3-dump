# heap - hard
import heapq
class Solution:
    def maxPoints(self, grid, queries):
        k = len(queries)
        # the beauty of this question lies in processing a sorted queries
        # sorting in ascending order allows us to continually expand our bfs region
        sq = sorted(queries)

        # edge case: the largest query can't beat grid[0][0]
        if sq[-1] <= grid[0][0]:
            return [0] * k

        m, n = len(grid), len(grid[0])
        ans_dict = dict()

        # we always start from top-left
        visited = set(((0,0),))
        # maintain a pointer idx to track the query we are scanning for
        q_idx = 0
        while q_idx < k and sq[q_idx] <= grid[0][0]:
            ans_dict[sq[q_idx]] = 0
            # move q_idx to the correct starting query
            q_idx += 1

        # maintain a running sum of points earned
        earned, min_heap = 0, [[grid[0][0], 0, 0]]

        while min_heap:

            val, r, c = heapq.heappop(min_heap)
            # only credit earned if curr. cell val strictly smaller than curr. query
            if val < sq[q_idx]:
                earned += 1
            else:
                ans_dict[sq[q_idx]] = earned
                q_idx += 1

                heapq.heappush(min_heap, [val, r, c])

                # must terminate if queries exhausted
                if q_idx == k: break

                # before the query become large enough to accommodate
                # the curr. min. cell val., we shall not enqueue any more neighbours
                continue

            # always update best earned for the curr. query
            ans_dict[sq[q_idx]] = earned

            # explore cardinal directions
            if c+1 < n and (r, c+1) not in visited:
                heapq.heappush(min_heap, [grid[r][c+1], r, c+1])
                visited.add((r, c+1))

            if c-1 >= 0 and (r, c-1) not in visited:
                heapq.heappush(min_heap, [grid[r][c-1], r, c-1])
                visited.add((r, c-1))

            if r+1 < m and (r+1, c) not in visited:
                heapq.heappush(min_heap, [grid[r+1][c], r+1, c])
                visited.add((r+1, c))

            if r-1 >= 0 and (r-1, c) not in visited:
                heapq.heappush(min_heap, [grid[r-1][c], r-1, c])
                visited.add((r-1, c))

        # if first query after sorting in ascending order is already
        # able to collect all elements in the grid, then we need to
        # assign earned as answer to remaining queries
        for i in range(q_idx, k):
            ans_dict[sq[i]] = earned

        return [ans_dict[q] for q in queries]
    
grid, queries = [[1,2,3],[2,5,7],[3,5,1]], [5,6,2]
grid, queries = [[5,2,1],[1,1,2]], [3]

Solution().maxPoints(grid, queries)