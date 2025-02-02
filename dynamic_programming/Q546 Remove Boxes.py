# dp - hard
class Solution:
    # runs in O(N^4) time and O(N^3) memory
    # the challenge lies in 1) realising that memoization is 3-D with an additional k, not just (i,j)
    # 2) sequential duplication from RHS should be removed while incrementing k
    def recursiveRemoval(self, i: int, j: int, k: int) -> int:
        # eventually if we have reduced to subproblem where we only have one element
        # then next subproblem where j -= 1 would trigger exit
        if i > j: return 0
        
        if (i,j,k) in self.dp: return self.dp[(i,j,k)]

        i_, j_, k_ = i, j, k

        # Check if we can reduce the sub-problem size
        # e.g. [2,1,1,2,2,2] is reduced to [2,1,1,2], with k = 2
        while i < j and self.boxes[j] == self.boxes[j-1]:
            j -= 1
            k += 1

        # If we have processed all the boxes, return the score
        if i == j:
            return (k+1)**2

        # Case 1: Remove the last k+1 boxes and recurse on the remaining sub-problem
        ans = (k+1)**2 + self.recursiveRemoval(i, j-1, 0)

        # Case 2: Merge boxes[j] with some box in the subarray i to j-1 and recurse on the two resulting sub-problems
        for m in range(j-1, i-1, -1):
            # e.g. if we have boxes [4,1,1,2,3,3,2,2,2]
            # we already have k+1 = 3 boxes of '2' on the right
            # if we are at index 3, the subproblems become: [4,1,1,2] & [3,3]
            # where sub-problem [4,1,1,2] does inherit the count of '2' boxes
            if self.boxes[m] == self.boxes[j]:
                ans = max(ans, self.recursiveRemoval(i, m, k+1) + self.recursiveRemoval(m+1, j-1, 0))

        self.dp[(i_,j_,k_)] = ans
        return ans
    
    def removeBoxes(self, boxes) -> int:
        # dp(i, j, k) := max score of boxes[i..j] if k boxes equal to boxes[j]
        self.dp = dict()
        self.boxes = boxes
        
        return self.recursiveRemoval(0, len(boxes)-1, 0)
    
boxes = [1,3,2,2,2,3,4,3,1]
boxes = [1,3,2,2,2,3,3,4,3,1]
boxes = [1,1,1]
boxes = [1]
boxes = [1] * 30 + [2] * 50 + [1] * 30 # ans=6100
boxes = [1,2,3,1,2,3] # ans=8
boxes = [1,2,3,2,1,2,3] # ans=13
boxes = [2,1,2,3,2,4,2] # ans=19
boxes = [2,3,2,3,2,3,2,3] # ans=20
boxes = [1,1,2,2,3] # ans=9
boxes = [1,2,3,1,4,4,3,2,1] # ans=17
boxes = [3,8,8,5,5,3,9,2,4,4,6,5,8,4,8,6,9,6,2,8,6,4,1,9,5,3,10,5,3,3,9,8,8,6,5,3,7,4,9,6,3,9,4,3,5,10,7,6,10,7]

Solution().removeBoxes(boxes)