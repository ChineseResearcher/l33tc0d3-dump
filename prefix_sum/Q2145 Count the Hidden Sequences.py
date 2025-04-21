# prefix sum - medium
class Solution:
    def numberOfArrays(self, differences, lower, upper):
        n = len(differences)
        # build a running sum as we iterate thru. differences
        rSum, maxDip, maxHike = 0, 0, 0

        for i in range(n):
            rSum += differences[i]
            maxDip = min(maxDip, rSum)
            maxHike = max(maxHike, rSum)
        
        # the solution lies in comparing the bandwidth between maxDip & maxHike
        # and to that of lower & upper, no answer if maxHike - maxDip results in larger width
        sumWidth, allowedWidth = maxHike - maxDip, upper - lower
        if sumWidth <= allowedWidth:
            return allowedWidth - sumWidth + 1
        else:
            return 0
        
differences, lower, upper = [1,-3,4], 1, 6
differences, lower, upper = [3,-4,5,1,-2], -4, 5
differences, lower, upper = [4,-7,2], 3, 6

Solution().numberOfArrays(differences, lower, upper)