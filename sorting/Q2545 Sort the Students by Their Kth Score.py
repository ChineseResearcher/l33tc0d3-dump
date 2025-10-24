# sorting - medium
from typing import List
class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:

        m = len(score)
        exam_k = [(score[r][k], r) for r in range(m)]
        exam_k.sort(key=lambda x: x[0], reverse=True)

        res = [None] * m
        for r in range(m):
            res[r] = score[exam_k[r][1]]

        return res
    
score, k = [[10,6,9,1],[7,5,11,2],[4,8,3,15]], 2
score, k = [[3,4],[5,6]], 0

Solution().sortTheStudents(score, k)