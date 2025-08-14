# counting - medium
from typing import List
from collections import Counter
class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        
        # core ideas:
        # 1) construct a frequency map for each unique number
        # 2) for each number x, generate all possible powers of 2 called y, check if x-y exists in freq
        freq = Counter(deliciousness)

        # max. bound for us to search powers of 2 up to
        max_comple = max(freq.keys())

        ans, MOD = 0, int(1e9 + 7)
        for x in deliciousness:
            
            # init. power s.t. power of 2 is the next immediate one
            # e.g. if x = 15, curr_power = 4; if x = 16, curr_power = 4
            if x & (x-1) == 0:
                curr_power = x.bit_length() - 1
            else:
                curr_power = x.bit_length()

            while True:
                y = pow(2, curr_power)

                complement = y - x
                if complement > max_comple:
                    break
                
                if x == complement:
                    ans += freq[complement] - 1
                else:
                    ans += freq[complement]

                ans %= MOD
                curr_power += 1

            # we need to decrement count of curr x
            # so that it won't be double counted
            freq[x] -= 1

        return ans
    
deliciousness = [1,3,5,7,9]
deliciousness = [1,1,1,3,3,3,7]

Solution().countPairs(deliciousness)