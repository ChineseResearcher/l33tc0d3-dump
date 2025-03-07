# sorting - medium
from collections import Counter
class Solution:
    def countWays(self, nums) -> int:
        
        n = len(nums)
        # edge case 1: nums.length = 1, there's always one way
        # to select: either by selecting all OR don't select at all
        if len(nums) == 1: return 1

        # question would require us to sort the nums arr.
        nums.sort()

        # count the unique numbers
        num_freq = Counter(nums)

        # build a nextGreater hashmap based on sorted unique numbers
        unique = list(num_freq.keys())
        nextGreater = dict()
        for i in range(len(unique)-1):
            nextGreater[unique[i]] = unique[i+1]

        nextGreater[unique[-1]] = float('inf')

        # access the min. and max. elements
        num_min, num_max = nums[0], nums[-1]

        # init. ans with case of not selecting any students
        # ans would store (group_size, group_max)
        ans = set(((0, num_min),)) if num_min > 0 else set()

        # edge case 2: nums arr only contain one unique num
        if len(num_freq) == 1:
            if n > num_max: ans.add((n, num_max))
            return len(ans)

        # keep track of max. number seen so far
        prevMax = nums[0]
        for i in range(1, n):

            # only trigger update to ans if nums[i] diff. from nums[i-1]
            if nums[i] != nums[i-1]:

                # case 1: select student i
                if (i + num_freq[nums[i]]) > nums[i] and (i + num_freq[nums[i]]) < nextGreater[nums[i]]:
                    # if curr. student selected, group max is nums[i]
                    ans.add((i+num_freq[nums[i]], nums[i]))

                # case 2: do not select student i
                if i > prevMax and i < nums[i]:
                    # if curr. student not selected, group max is prevMax
                    ans.add((i, prevMax))

                # update prevMax
                prevMax = nums[i]

        return len(ans)
    
nums = [0]
nums = [1,1]
nums = [6,0,3,3,6,7,2,7]
nums = [5,0,3,4,2,1,2,4]

Solution().countWays(nums)