# dp - hard
class Solution:
    def maxSumOfThreeSubarrays(self, nums, k):
        n = len(nums)

        # precompute window sum of size equal k
        window_sum = sum(nums[:k])
        window_arr = [window_sum]

        for i in range(k, n):

            window_sum += nums[i]
            window_sum -= nums[i-k]

            window_arr.append(window_sum)

        # extend wind_arr to match length n
        window_arr.extend([float('-inf')] * (k-1))

        # prepare two auxiliary leftMax/rightMax array
        # storing the lexicographically smallest indices which would 
        # yield the largest window sum while respecting distancing of k
        leftMax = [-1] * n
        max_val, max_idx = -1, -1
        for i in range(n-k):
            # we always want the smallest index possible
            if window_arr[i] > max_val:
                max_idx = i
                max_val = window_arr[i]

            leftMax[i+k] = max_idx 

        rightMax = [-1] * n
        max_val, max_idx = -1, -1
        for j in range(n-1, k-1, -1):
            if window_arr[j] >= max_val:
                max_idx = j
                max_val = window_arr[j]
            
            rightMax[j-k] = max_idx

        ans = []
        maxThreeSum = 0
        for k in range(n):

            # check for valid three non-overlapping subarrays
            if leftMax[k] != -1 and rightMax[k] != -1:
                currSum = window_arr[leftMax[k]] + window_arr[k] + window_arr[rightMax[k]]
                if currSum > maxThreeSum:
                    ans = [leftMax[k], k, rightMax[k]]
                    # update max
                    maxThreeSum = currSum

        return ans
    
nums = [1,2,1,2,6,7,5,1]
k = 2

nums = [1,2,1,2,1,2,1,2,1]
k = 2

Solution().maxSumOfThreeSubarrays(nums, k)
