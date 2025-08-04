# sliding window - medium
from typing import List
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:

        n = len(fruits)
        # in short we want to having a (virtual) window over which 
        # we have the greatest length and contain only two types of fruits
        picked_fruit = dict() # storing <fruit_id, fruits_picked>

        l, ans = 0, 0
        for r in range(n):

            curr_fruit = fruits[r]
            
            if curr_fruit not in picked_fruit:

                if len(picked_fruit) >= 2:

                    ans = max(ans, r-l)
                    while len(picked_fruit) >= 2:

                        fruit_del = fruits[l]
                        picked_fruit[fruit_del] -= 1
                        if picked_fruit[fruit_del] == 0:
                            del picked_fruit[fruit_del]

                        l += 1

                else:
                    ans = max(ans, r-l+1)

                picked_fruit[curr_fruit] = 1

            else:
                picked_fruit[curr_fruit] += 1
                ans = max(ans, r-l+1)

        return ans
    
fruits = [1,2,1]
fruits = [0,1,2,2]
fruits = [1,2,3,2,2]

Solution().totalFruit(fruits)