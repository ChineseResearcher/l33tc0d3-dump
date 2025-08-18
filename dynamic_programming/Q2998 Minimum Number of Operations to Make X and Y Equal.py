# dp - medium
from functools import cache
class Solution:
    def minimumOperationsToMakeEqual(self, x: int, y: int) -> int:
        
        @cache
        def recursive_op(x):
            
            # when x <= y, we can only increase x to make it equal y
            if x <= y:
                return y-x
            
            # when x > y, the ready choice would be x - 1 - .., -1 = y
            curr_res = x-y

            # mod 11
            mod_11 = x % 11
            if mod_11 < 11 / 2:
                # subtract mod_11 from x to make it divisble by 11
                curr_res = min(curr_res, mod_11 + 1 + recursive_op((x - mod_11) // 11))
            else:
                # add (11-mod_11) to x to make it divisible by 11
                curr_res = min(curr_res, (11-mod_11) + 1 + recursive_op((x + (11-mod_11)) // 11))
            
            # mod 5
            mod_5 = x % 5
            if mod_5 < 5 / 2:
                curr_res = min(curr_res, mod_5 + 1 + recursive_op((x - mod_5) // 5))
            else:
                curr_res = min(curr_res, (5-mod_5) + 1 + recursive_op((x + (5-mod_5)) // 5))

            return curr_res

        return recursive_op(x)
    
x, y = 26, 1
x, y = 54, 2
x, y = 25, 30

Solution().minimumOperationsToMakeEqual(x, y)