# monotonic stack - medium
class Solution:
    # this is arguably the most challenging stack (monoStack) problem
    def find132pattern(self, nums):
        n = len(nums)
        
        # the stack is 2D, storing <"3", curr "1" (i.e. smallest seen so far)>
        # both "3" & "1" val are monotonic decreasing
        st = []
        currMin = nums[0]

        for currNum in nums[1:]:

            # always pop (any) "3" assignments in the stack smaller than currNum
            # this ensures we would have the largest possible "3" in the stack
            # thus creating greater room for another num to be assigned as "2"
            while st and currNum >= st[-1][0]:
                st.pop()
            
            # pattern found!
            if st and currNum > st[-1][1]:
                return True
            
            st.append([currNum, currMin])
            currMin = min(currMin, currNum)
        
        return False
    
nums = [3,1,4,2]
nums = [1,2,3,4]
nums = [-1,3,2,0]
nums = [3,5,0,3,4]
nums = [1,0,1,-4,-3]
nums = [-2,1,2,-2,1,2]
nums = [1,3,2,4,5,6,7,8,9,10]
nums = [1,4,0,-1,-2,-3,-1,-2]

Solution().find132pattern(nums)
