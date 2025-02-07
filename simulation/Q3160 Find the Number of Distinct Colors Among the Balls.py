# simulation - medium
class Solution:
    def queryResults(self, limit, queries):
        # record the latest color of balls colored
        ball_color = dict()

        # record the set of balls colored by each used color
        # the length of this dict is our ans after the i-th query
        color_set = dict()

        ans = []
        for ball, color in queries:

            if ball in ball_color:
                last_color = ball_color[ball]
                color_set[last_color].discard(ball)

                # important to always drop out a color if no balls are colored by it
                if not color_set[last_color]:
                    del color_set[last_color]

            # override color
            ball_color[ball] = color

            if color not in color_set:
                color_set[color] = set()

            color_set[color].add(ball)

            # update the number of distinct colors
            ans.append(len(color_set))

        return ans

limit, queries = 4, [[1,4],[2,5],[1,3],[3,4]]
limit, queries = 4, [[0,1],[1,2],[2,2],[3,4],[4,5]]

Solution().queryResults(limit, queries)