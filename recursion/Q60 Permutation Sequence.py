# recursion - hard
class Solution:
    def recursive_seq(self, availStr, k):

        # given available number string, e.g. '123'
        # permute each number whilst decrementing k as much as possible

        # if k is only 1, the availStr in its curr. order is the answer
        if k == 1: return availStr
        
        idx = 0
        # decrement is determined as (len(availStr)-1)!
        # because we are fixing availStr[idx] and letting the remaining permute
        decrement = self.factorial[len(availStr) - 1]
        while idx < len(availStr):

            if k - decrement <= 0:
                break

            k -= decrement
            idx += 1

        idx = min(idx, len(availStr)-1)
        nextAvail = availStr[:idx] + availStr[(idx+1):]

        # if k is used up at the curr level exactly, we fix availStr[idx]
        # as the head, and appened the remaining numbers in desc. fashion
        if k == 0:
            return availStr[idx] + nextAvail[::-1]
        else:
            return availStr[idx] + self.recursive_seq(nextAvail, k)

    def getPermutation(self, n: int, k: int) -> str:

        # pre-compute factorial for 1! to (n-1)! for decrement ref.
        self.factorial = dict()
        currProd = 1
        for i in range(1, n):
            currProd *= i
            self.factorial[i] = currProd

        return self.recursive_seq(''.join([str(i) for i in range(1, n+1)]), k)
    
n, k = 3, 3
n, k = 4, 9
n, k = 3, 1

Solution().getPermutation(n, k)