# monotonic stack - medium
class Solution:
    def sumSubarrayMins(self, arr):
        # we could model this problem as the Largest Rectangle Problem (LC84)
        # Note: an array of size n would have n * (n+1) / 2 subarrays
        heights = arr

        # a dummy index of -1 points to a dummy height of 0 at the end
        # this monoStack would be ascending, and get popped upon smaller
        heights.append(0)
        st = [-1]

        ans, MOD = 0, int(1e9+7)
        for i in range(len(heights)):
            
            while heights[i] < heights[st[-1]]:
                pi = st.pop()
                # the popped index (pi) is used as the target
                # min. for any potential subarrs. containing it
                h = heights[pi]

                # number of heights to the left that are >= h
                left_cnt = pi - st[-1]

                # number of height to the right that are >= h
                right_cnt = i - pi

                # the number of subarr. combinations
                ans += (left_cnt * right_cnt) * h
                ans %= MOD
                
            st.append(i)

        return ans
    
arr = [3,1,2,4]
arr = [11,81,94,43,3]

Solution().sumSubarrayMins(arr)