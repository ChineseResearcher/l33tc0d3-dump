# dp - medium
class Solution:
    def recursive_guess(self, lb, ub):

        # lb, ub defines the range of a game (or sub-game)
        # when ub <= lb, the game would have stopped
        if ub <= lb: return 0

        if (lb, ub) in self.dp: return self.dp[(lb, ub)]
        
        # otherwise, the game continues and we explore any
        # number as our guess in the range given
        currCost = float('inf')

        # at each sub-game, we want to choose the guess
        # that results in a mini-max amt. of money to play
        for num in range(lb, ub+1):
            currCost = min(currCost, num + \
                           max(self.recursive_guess(lb, num-1), self.recursive_guess(num+1, ub)) )

        self.dp[(lb, ub)] = currCost
        return currCost

    def getMoneyAmount(self, n: int) -> int:
        self.dp = dict()
        return self.recursive_guess(1, n)
    
n = 10
n = 200

Solution().getMoneyAmount(n)