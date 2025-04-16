# sliding window - medium
class Solution:
    def maxSatisfied(self, customers, grumpy, minutes) -> int:
        
        if len(grumpy) <= minutes or sum(grumpy) == 0:
            return sum(customers)

        # first window is just the window (0, minutes)
        windowSum = sum(customers[:minutes])
        windowlessSum = sum([v for idx, v in enumerate(customers) if grumpy[idx] == 0])
        # we need to initialise currSum, which includes removing the double counted happy states (0 states)
        currSum = windowSum + windowlessSum - sum([customers[idx] for idx, state in enumerate(grumpy[:minutes]) if state == 0])

        maxSum = currSum

        for left in range(1, len(grumpy)-minutes+1):

            # we check every possible window of size = minutes
            deleted, added = customers[left-1], customers[left + minutes - 1]
            currSum = currSum - deleted + added
            
            # deal with double counting
            if grumpy[left-1] == 0:
                currSum += deleted
                
            if grumpy[left + minutes - 1] == 0:
                currSum -= added
                
            maxSum = max(maxSum, currSum)
            
        return maxSum
    
customers, grumpy, minutes = [1,0,1,2,1,1,7,5], [0,1,0,1,0,1,0,1], 3
customers, grumpy, minutes = [10,1,7], [0,0,0], 2
customers, grumpy, minutes = [4,10,10], [1,1,0], 2

Solution().maxSatisfied(customers, grumpy, minutes)