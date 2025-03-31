# sorting - hard
class Solution:
    def putMarbles(self, weights, k):
        n = len(weights)
        # edge case: as illustrated in sample TC2, when k = n
        # it means every weight is to be assigned to a bag, so diff. is 0
        if n == k or k == 1: return 0

        # since all weights should be used, first and last marble is always
        # used, and the final formation would consist of k subarrays with k-1 partitions

        # the approach to solving this problem is to find k-1 partitions
        # that would give rise to max./min. total score respectively

        # this would mean sorting the pair sums for weights[i] & weights[i+1]
        # where 0 <= i < n-1, representing a potential partition at i & i+1
        pairSum = sorted([weights[i] + weights[i+1] for i in range(n-1)])

        # find k-1 largest & smallest pairSums
        return sum(pairSum[-(k-1):]) - sum(pairSum[:(k-1)])
    
weights, k = [1,3,5,1], 2 # max: [1,3], [5,1]; min: [1], [3,5,1]
weights, k = [1,3], 2
weights, k = [5,4,3,2,1], 2 # max: [5], [4,3,2,1]; min: [5,4,3,2], [1]
weights, k = [1,2,3,1,4], 3 # max: [1,2],[3,1],[4]; min: [1],[2,3],[1,4]

Solution().putMarbles(weights, k)