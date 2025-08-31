# prefix sum - medium
from typing import List
class Solution:
    def distance(self, nums: List[int]) -> List[int]:

        n = len(nums)
        # core ideas:
        # 1) approach w/ two passes, one forward, one backward
        # 2) in each pass, track the freq. of seen numbers, and a running sum of
        # seen indices for each number alongside the freq. 
        ans = [0] * n

        def iter_helper(direc: str) -> None:

            num_info = dict() # <freq, index_sum>
            if direc == 'forward':
                ii = [i for i in range(n)]
            elif direc == 'backward':
                ii = [i for i in range(n-1, -1, -1)]

            for i in ii:

                curr_num = nums[i]
                if curr_num not in num_info:
                    num_info[curr_num] = [0, 0]

                # increment freq
                num_info[curr_num][0] += 1
                # increment index sum
                num_info[curr_num][1] += i

                freq, iSum = num_info[curr_num]
                ans[i] += abs(freq * i - iSum)

        iter_helper('forward')
        iter_helper('backward')

        return ans
    
nums = [1,3,1,1,2]
nums = [0,5,3]

Solution().distance(nums)