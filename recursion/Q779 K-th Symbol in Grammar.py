# recursion - medium
class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        
        # we are given n iterations (1-index) starting with a '0'
        if n == 1:
            return 0

        # pow: curr. exponential number
        # leftCnt: count of numbers in the FINAL n-th iteration before this num
        # state: digit 0/1
        def dfs(pow, leftCnt, state):

            if leftCnt + 1 == k:
                return state
            
            # compute the next smaller cnt
            nextCnt = leftCnt + ((2 << (pow-1)) if pow > 0 else 1)

            # key ideas:
            # 1) we only need to go to either left or right split
            # depending on where k falls at
            # 2) '0' -> '01' and '1' -> '10', so for right split digit always invert
            # whereas for left split it always remains the same

            # right split 
            if k > nextCnt and pow - 1 >= -1:
                return dfs(pow-1, nextCnt, 1 - state) 
            # left split
            elif k <= nextCnt and pow - 1 >= -1:
                return dfs(pow-1, leftCnt, state)

        # starting from the root "0" and deal w/ n-2 powers
        return dfs(n-2, 0, 0)
    
n, k = 1, 1
n, k = 2, 1
n, k = 2, 2
n, k = 3, 1
n, k = 30, int(1e4)

Solution().kthGrammar(n, k)