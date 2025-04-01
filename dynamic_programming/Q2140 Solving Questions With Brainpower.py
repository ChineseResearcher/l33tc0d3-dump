# dp - medium
class Solution:
    def mostPoints(self, questions):
        n = len(questions)
        # dp[i] stores the max. points if we consider up to the i-th question
        dp = [0] * n

        for i in range(n):

            # op1: skip
            if i + 1 < n:
                dp[i+1] = max(dp[i+1], dp[i])

            # op2: solve curr. question
            solve = questions[i][0]
            next_qn = i + questions[i][1] + 1

            dp[i] += solve
            if next_qn < n:
                dp[next_qn] = max(dp[next_qn], dp[i])

        return max(dp)
    
questions = [[3,2],[4,3],[4,4],[2,5]]
questions = [[1,1],[2,2],[3,3],[4,4],[5,5]]
questions = [[12,46],[78,19],[63,15],[79,62],[13,10]]

Solution().mostPoints(questions)