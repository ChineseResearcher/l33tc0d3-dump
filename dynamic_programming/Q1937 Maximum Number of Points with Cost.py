# dp - medium
class Solution:
    # the trick to optimise the soln into O(n*m) is that we tabulate the
    # leftMax/rightMax arr. for each row (row > 0) iterated
    # e.g. suppose we have arr [5,2,1,2], taking into account the penalty from col. distance
    # leftMax = [7,6,8,7], rightMax = [6,7,8,4] 

    def leftMax(self, row, dp):
        # given row > 0, find the leftMax arr. 
        # based on the prev. row in dp for the curr. row

        res = [dp[row-1][0]] + (self.n-1) * [0]
        for i in range(1, self.n):
            res[i] = max(res[i-1]-1, dp[row-1][i])

        return res

    def rightMax(self, row, dp):
        # given row > 0, find the rightMax arr. 
        # based on the prev. row in dp for the curr. row

        res = (self.n-1) * [0] + [dp[row-1][-1]]
        for i in range(self.n-2, -1, -1):
            res[i] = max(res[i+1]-1, dp[row-1][i])

        return res

    def maxPoints(self, points) -> int:
        self.m, self.n = len(points), len(points[0])

        ans = max(points[0])
        # we don't need to process row 1 as the ans is as it is
        for i in range(1, self.m):
            
            # the brute force approach is that for every cell in the curr. row,
            # we inherit from the max. possible cell from prev. row
            lm, rm = self.leftMax(i, points), self.rightMax(i, points)
            for j in range(self.n):
                
                # inherit from leftMax
                op1 = lm[j]
                
                # inherit from rightMax
                op2 = rm[j]

                # inherit directly from above cell
                op3 = points[i-1][j]

                points[i][j] = points[i][j] + max(op1, max(op2, op3))
                ans = max(ans, points[i][j])

        return ans
    
points = [[1,2,3],[1,5,1],[3,1,1]]
points = [[1,5],[2,3],[4,2]]
points = [[1,5],[3,2],[4,2]]
points = [[5,2,1,2],[2,1,5,2],[5,5,5,0]]
points = [[0,4,7,1,1],[3,8,2,6,7],[5,10,8,6,9],[2,6,10,1,7],[9,6,4,0,5],[3,7,7,3,5]]

Solution().maxPoints(points)