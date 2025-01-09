# dp - hard
class Solution:
    def trap(self, height) -> int:
        n = len(height)
        rightMax, leftMax = [0]*n, [0]*n

        for i in range(n-2, -1, -1):
            rightMax[i] = max(rightMax[i+1], height[i+1])

        for j in range(1, n):
            leftMax[j] = max(leftMax[j-1], height[j-1])

        vol = 0 # answer
        for k in range(n):
            leftmax, rightmax, currHeight = leftMax[k], rightMax[k], height[k]
            vol += max(min(leftmax-currHeight, rightmax-currHeight), 0)

        return vol
    
height = [0,1,0,2,1,0,1,3,2,1,2,1]
height = [4,2,0,3,2,5]
height = [4,2,3]
height = [5,4,1,2]
height = [2,8,5,5,6,1,7,4,5]

Solution().trap(height)