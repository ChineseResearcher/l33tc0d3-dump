# greedy - medium
from typing import List
class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        
        m, n = len(landStartTime), len(waterStartTime)

        L = []
        for i in range(m):
            L.append((landStartTime[i] + landDuration[i], landStartTime[i]))

        W = []
        for j in range(n):
            W.append((waterStartTime[j] + waterDuration[j], waterStartTime[j]))

        # shortest duration, followed by earliest startTime
        L.sort()
        W.sort()

        op1 = float('inf')
        # option 1: land first -> water second
        for k in range(n):
            op1 = min(op1, max(L[0][0], W[k][1]) + (W[k][0] - W[k][1]))

        op2 = float('inf')
        # option 2: water first -> land second
        for k in range(m):
            op2 = min(op2, max(W[0][0], L[k][1]) + (L[k][0] - L[k][1]))

        return min(op1, op2)

landStartTime, landDuration, waterStartTime, waterDuration = [2,8], [4,1], [6], [3]
landStartTime, landDuration, waterStartTime, waterDuration = [5], [3], [1], [10]
landStartTime, landDuration, waterStartTime, waterDuration = [99], [59], [99,54], [85,20]
landStartTime, landDuration, waterStartTime, waterDuration = [31,8], [47,64], [3,7], [95,44]

Solution().earliestFinishTime(landStartTime, landDuration, waterStartTime, waterDuration)