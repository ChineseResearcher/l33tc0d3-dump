# array - hard
class Solution:
    # the real challenge was to solve in O(1) memory/space
    # i.e. no set/hashmap to store seen numbers
    # and to achieve that, the concept of "circular sorting" is used

    def firstMissingPositive(self, nums) -> int:
        n = len(nums)
        # there are two types of numbers to skip according to the question:
        # 1) numbers <= 0
        # 2) numbers that are greater than n, length of arr

        # reason for 2) being that in the mostly condensed case where the
        # entire arr. is all +ve int and contiguous, i.e. [1,...,n]
        # we would have largest +ve int = n, so any larger int would not
        # change our answer, and we skip it while processing nums arr.

        for i in range(n):

            # skip cases
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = -1
                continue
            
            # we keep modifying nums[i] in-place whenever we see a mismatch
            # between index and the actual number
            while i + 1 != nums[i]:
                swapped = nums[nums[i]-1]

                # swap in-place
                nums[nums[i]-1] = nums[i]

                # duplicate found OR skip cases encountered
                if swapped == nums[i] or swapped <= 0 or swapped > n:
                    nums[i] = -1
                    break

                nums[i] = swapped

        # print('after circular sorting:', nums)
        for i in range(n):
            if nums[i] == -1: return i+1
        
        # otherwise, we have encountered the worst case explained above
        # where we are dealing with unsorted [1,...,n], and next missing +ve = n+1
        return n+1
    
nums = [3,-1,1,8,4,2,6]
nums = [3,4,-1,1]
nums = [1,2,0]
nums = [7,8,9,11,12]
nums = [3,2]
nums = [1,1]
nums = [1,2,3,4,5,6,7,8,9,20]
nums = [2,3,4,5,6,7,8,9,10,20]

Solution().firstMissingPositive(nums)