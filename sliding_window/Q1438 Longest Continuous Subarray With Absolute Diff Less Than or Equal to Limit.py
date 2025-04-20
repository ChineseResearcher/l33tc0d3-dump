# sliding window - medium
from collections import deque
class Solution:
    def longestSubarray(self, nums, limit) -> int:
        
        # Max & Min always keeps track of the max. and min. element in the curr. window
        Max, Min, answer, left = deque(), deque(), 0, -1
        for right, num in enumerate(nums):
            
            # greedily updates Max s.t. Max[0] is always the subarray max.
            while Max and Max[-1] < num: 
                Max.pop()
            Max.append(num)

            # greedily updates Min s.t. Min[0] is always the subarray min.
            while Min and Min[-1] > num: 
                Min.pop()
            Min.append(num)

            # controls the window sliding
            while Max[0] - Min[0] > limit:
                left += 1
                # popleft() is key to sliding the left end of the window
                if Max[0] == nums[left]: 
                    Max.popleft() 
                if Min[0] == nums[left]: 
                    Min.popleft()

            answer = max(answer, right - left)

        return answer
    
nums, limit = [8,2,4,7], 4
nums, limit = [10,1,2,4,3,7,2], 4
nums, limit = [10,1,2,4,7,2], 5
nums, limit = [4,2,2,2,4,4,2,2], 0

Solution().longestSubarray(nums, limit)