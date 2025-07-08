# dp - hard
class Solution:
    def binarySearch(self, l, r, startTime, endTime):
        
        # goal is the rightmost valid index such that
        # endTime[index] <= startTime[initial r]
        time_cutoff = startTime[r]
        
        rightMost = -1 # dummy
        while l <= r:
            
            mid = (l+r) // 2
            # print(mid)
            if endTime[mid] <= time_cutoff:
                
                rightMost = max(rightMost, mid)
                l = mid+1
                
            else:
                r = mid-1
                
        return rightMost

    def jobScheduling(self, startTime, endTime, profit):
        n = len(endTime)

        # sort all three arrays by endTime
        sorted_arrays = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])

        # unpack
        startTime, endTime, profit = map(list, zip(*sorted_arrays))

        # construct a dp where dp[i] stores the 
        # subproblem considering indices up to i
        dp = [0] * n

        # first dp value is simply profit[0]
        dp[0] = profit[0]

        # track a running max dp
        curr_max_dp, prev_max_dp = dp[0], {0:dp[0]}
        for i in range(1,n):
            
            # O(logN) time to locate the rightMost valid non-overlapping index
            last_non_overlap = self.binarySearch(0, i, startTime, endTime)
            
            # if no valid index found
            if last_non_overlap == -1:
                dp[i] = profit[i]
                
            else:
                dp[i] = profit[i] + prev_max_dp[last_non_overlap]
        
            curr_max_dp = max(curr_max_dp, dp[i])
            prev_max_dp[i] = curr_max_dp
                     
        return max(dp)  
    
startTime, endTime, profit = [4,2,4,8,2], [5,5,5,10,8], [1,2,8,10,4]
startTime, endTime, profit = [1,2,3,4,6], [3,5,10,6,9], [20,20,100,70,60]
startTime, endTime, profit = [1,1,1], [2,3,4], [5,6,4]
startTime, endTime, profit = [4,2,4,8,2], [5,5,5,10,8], [1,2,8,10,4]

Solution().jobScheduling(startTime, endTime, profit)