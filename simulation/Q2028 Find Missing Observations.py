# simulation - medium
class Solution:
    def handleLO(self, leftover):
        for i in range(len(self.ans)):
            while self.ans[i] < 6:
                self.ans[i] += 1
                leftover -= 1
                if leftover <= 6:
                    return leftover

    def missingRolls(self, rolls, mean, n):
        m = len(rolls)
        non_missing_sum = sum(rolls)
        full_sum = (m + n) * mean

        missing_sum = full_sum - non_missing_sum
        missing_avg = missing_sum / n
        if (missing_avg > 6 or missing_avg < 1) or missing_sum <= 0:
            return []

        self.ans = [int(missing_avg)] * (n-1)
        leftover = int(missing_sum - int(missing_avg) * (n-1))

        if leftover > 6:
            leftover = self.handleLO(leftover)

        self.ans.append(leftover)
        return self.ans
    
rolls, mean, n = [3,2,4,3], 4, 2
rolls, mean, n = [1,5,6], 3, 4
rolls, mean, n = [1,2,3,4], 6, 4
rolls, mean, n = [6,3,4,3,5,3], 1, 6
rolls, mean, n = [4,5,6,2,3,6,5,4,6,4,5,1,6,3,1,4,5,5,3,2,3,5,3,2,1,5,4,3,5,1,5], 4, 40
rolls, mean, n = [4,2,2,5,4,5,4,5,3,3,6,1,2,4,2,1,6,5,4,2,3,4,2,3,3,5,4,1,4,4,5,3,6,1,5,2,3,3,6,1,6,4,1,3], 2, 53

Solution().missingRolls(rolls, mean, n)