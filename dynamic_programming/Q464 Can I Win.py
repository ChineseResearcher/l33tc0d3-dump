# dp - medium
class Solution:
    def recursive_play(self, curr_total, choosable):
    
        if (curr_total, choosable) in self.dp: return self.dp[(curr_total, choosable)]
        
        # otherwise we go on exploring numbers from max. choosable int
        # all the way to number 1, early return if curr. max. choosable ends game
        canWin = False
        for i in range(self.maxChoosableInteger-1, -1, -1):
            
            # check if a bit is 0 at index i (from right)
            # which indicates an unused integer
            if not (choosable & (1 << i)):

                # our terminate cond.
                if curr_total + i + 1 >= self.desiredTotal: return True

                # encode the curr number (i+1) as taken by setting the i-th bit of choosable to 1
                canWin = (canWin or not self.recursive_play(curr_total+(i+1), choosable | (1 << i)))
            
        self.dp[(curr_total, choosable)] = canWin
        return canWin

    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        # edge case: the game would not result in any winner
        if sum([i for i in range(1, maxChoosableInteger+1)]) < desiredTotal: return False

        self.desiredTotal, self.maxChoosableInteger = desiredTotal, maxChoosableInteger
        self.dp = dict()
        # choosable is initiated to 0 as all our integers have not been used yet
        return self.recursive_play(0, 0)
    
maxChoosableInteger, desiredTotal = 10, 11
maxChoosableInteger, desiredTotal = 10, 0
maxChoosableInteger, desiredTotal = 10, 1
maxChoosableInteger, desiredTotal = 5, 12
maxChoosableInteger, desiredTotal = 10, 40
maxChoosableInteger, desiredTotal = 5, 50

Solution().canIWin(maxChoosableInteger, desiredTotal)