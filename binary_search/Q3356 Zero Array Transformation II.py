# binary search - medium
class Solution:
    def canReduce(self, k):

        # k is the k-th query we can consider up to in building our delta arr
        # containing net changes to the number to be added at each index
        delta = [0] * self.n

        for l, r, increment in self.queries[:(k+1)]:
            delta[l] += increment
            if r+1 < self.n: delta[r+1] -= increment

        # after building the delta arr., iterate thru the idx of nums
        # and check if simulated prefix sum at the idx >= original prefix sum at idx
        runningSum, netChange = 0, 0
        for i in range(self.n):

            netChange += delta[i]
            runningSum += netChange

            # there can be a case where the current increment (netChange)
            # itself is smaller than the nums[i], which is also invalid
            if runningSum < self.pfSum[i] or netChange < self.nums[i]:
                return False

        return True

    def minZeroArray(self, nums, queries):
        # edge case: nums arr. is already all zeroes
        if sum(nums) == 0: return 0

        self.n, m = len(nums), len(queries)
        self.nums, self.queries = nums, queries

        # calculate the prefix sum of nums arr.
        self.pfSum = [0] * self.n
        self.pfSum[0] = nums[0]

        for i in range(1, self.n):
            self.pfSum[i] = self.pfSum[i-1] + self.nums[i]

        # to search for the min. k efficiently, use binary search
        l, r = 0, m-1
        ans = m+1
        while l <= r:

            k = (l+r) // 2
            if self.canReduce(k):
                # greedily search for smaller range
                r = k-1
                ans = min(ans, k)
            else:
                l = k+1

        # return answer as 1-index
        return ans+1 if ans+1 < m+1 else -1
    
nums, queries = [2,0,2], [[0,2,1],[0,2,1],[1,1,3]]
nums, queries = [4,3,2,1], [[1,3,2],[0,2,1]]
nums, queries = [0,8], [[0,1,4],[0,1,1],[0,1,4],[0,1,1],[1,1,5],[0,1,2],[1,1,4],[0,1,1],[1,1,3],[0,0,2],[1,1,3],[1,1,2],[0,1,5],[1,1,2],[1,1,5]]

Solution().minZeroArray(nums, queries)