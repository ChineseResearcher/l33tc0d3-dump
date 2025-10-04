# sorting - hard
from typing import List
from collections import Counter
class Solution:
    def recoverArray(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        # first create a frequency map of all the number thats appear
        freq = Counter(nums)

        # it is necessary to sort the numbers
        # so that we could optimally obtain the paired elements
        nums.sort()

        # since the question guarantees an answer, for the first 
        # element of nums, is bound to be a correct pair with some another number
        for i in range(1, n):

            # assume we are making a pair with nums[i]
            # note: diff. would have to be even
            diff = nums[i] - nums[0]
            if diff > 0 and diff % 2 == 0:
                
                curr_freq = freq.copy()
                # deplete the assumed pair from freq.
                curr_freq[nums[0]] -= 1
                if curr_freq[nums[0]] == 0:
                    del curr_freq[nums[0]]

                curr_freq[nums[i]] -= 1
                if curr_freq[nums[i]] == 0:
                    del curr_freq[nums[i]]

                curr_ans = [min(nums[0], nums[i]) + diff // 2]
                # ensure the diff. can be valid for all remaining elements
                for j in range(n):
                    if nums[j] in curr_freq:
                        
                        # deal with larger paired element
                        larger = nums[j] + diff
                        if larger in curr_freq:

                            curr_freq[larger] -= 1
                            if curr_freq[larger] == 0:
                                del curr_freq[larger]

                            curr_freq[nums[j]] -= 1
                            if curr_freq[nums[j]] == 0:
                                del curr_freq[nums[j]]

                            curr_ans.append(nums[j] + diff // 2)
                            continue

                        # otherwise, no valid paired element found
                        # which means curr. assumed diff is invalid
                        break

                # curr_ans only valid if it consists of exactly n // 2 elements
                if len(curr_ans) == n // 2:
                    break
            
        return curr_ans
    
nums = [5,435]
nums = [1,1,3,3]
nums = [2,10,6,4,8,12]
nums = [8,4,5,1,9,8,6,5,6,9,7,3,8,3,6,7,10,11,6,4]

Solution().recoverArray(nums)