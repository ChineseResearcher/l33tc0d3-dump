# dp - medium
class Solution:
    def recursive_ops(self, currInt):

        # there's a bitwise trick to confirm that an integer
        # is a perfect power of 2 by leveraging on logical AND
        if currInt > 0 and (currInt & (currInt-1)) == 0:

            # if currInt is a perfect square, then it would occupy
            # only one bit, which is definitely unusued for currInt-1
            # then it just takes one deletion op to reduce it to 0
            return 1
            
        if currInt in self.dp: return self.dp[currInt]

        currAns = float('inf')
        # for a given int, we can either add or subtract power2 integer
        # by observation, here we need to access the least significant
        # set bit in currInt as the chosen power

        chosenPower = (currInt & -currInt).bit_length() - 1

        # print(f'subproblem of int: {currInt}, add/subtract 2 to the power of {chosenPower}')
        
        # case 1: add
        currAns = min(currAns, self.recursive_ops(currInt + 2**chosenPower))
        # case 2: subtract
        currAns = min(currAns, self.recursive_ops(currInt - 2**chosenPower))

        # account for the curr. operation
        currAns += 1
        self.dp[currInt] = currAns

        return currAns

    def minOperations(self, n: int) -> int:
        self.dp = dict()
        return self.recursive_ops(n)
    
n = 39
n = 54
n = int(1e5) # constraint

Solution().minOperations(n)