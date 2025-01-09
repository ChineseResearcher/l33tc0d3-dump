# greedy - medium
class Solution():
    def jump(self, nums):
        def minMoves(nums):
            
            # as we are standing at pos 0, we've already reached the end
            if len(nums) == 1:
                return 0
            
            last_position = 0
            for i in range(len(nums)):
                # greedily update the furthest reachable position
                last_position = max(last_position, i+nums[i])

                # signal reaching the end
                if last_position >= len(nums) - 1:
                    cutoff_idx = i
                    break
            
            # recursive call to the next sub-problem concerning the remaining length
            return 1 + minMoves(nums[:cutoff_idx+1])
        
        return minMoves(nums)
    
nums = [2,3,1,1,4]
nums = [2,3,0,1,4]

Solution().jump(nums)