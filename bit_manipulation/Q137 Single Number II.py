# bit manipulation - medium
from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # question is very challenging due to the fact it wants
        # us to implement constant space solution -> no hashmap to store
        # seen numbers and their frequencies

        # core ideas:
        # maintain two bitmasks called Ones and Twos
        # 1) Ones acts as the counter for bits which did appear once
        # 2) Twos acts as the counter for bits which did appear twice
        # then after processing all nums Ones will be our answer - the element appearing once
        Ones, Twos = 0, 0

        for num in nums:

            # the below transformation can also be summarised as:
            # Ones = (Ones ^ num) & ~Twos
            # Twos = (Twos ^ num) & ~Ones
            for i in range(32):

                # get set bits
                if num & (1 << i) != 0:
                    # if this bit has not appeared once, increment it in Ones
                    if Ones & (1 << i) == 0:
                        Ones |= (1 << i)
                    # if this bit has appeared only once, increment it in Twos
                    elif Ones & (1 << i) != 0 and Twos & (1 << i) == 0:
                        Twos |= (1 << i)
                    # if this bit has appeared twice, decrement in both Ones & Twos
                    elif Ones & (1 << i) != 0 and Twos & (1 << i) != 0:
                        Ones &= ~(1 << i)
                        Twos &= ~(1 << i)

        # detect signed bit in case the unique number is -ve
        if Ones & (1 << 31):
            Ones -= 1 << 32

        return Ones
    
nums = [2,2,3,2]
nums = [0,1,0,1,0,1,99]
nums = [2,2,-9999,2,-1,-1,-1]

Solution().singleNumber(nums)