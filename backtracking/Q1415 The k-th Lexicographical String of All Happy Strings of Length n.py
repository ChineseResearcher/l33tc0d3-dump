# backtracking - medium
class Solution:
    def recursive_lexi_form(self, seq):

        if len(seq) == self.n:
            self.soln.append(seq[:])
            return
        
        for char in ['a', 'b', 'c']:
            if not seq or (seq and char != seq[-1]):
                seq.append(char)
                self.recursive_lexi_form(seq)
                seq.pop()

    def getHappyString(self, n: int, k: int) -> str:
        self.n = n
        self.soln = []

        self.recursive_lexi_form([])
        return ''.join(self.soln[k-1]) if k-1 < len(self.soln) else ''
    
n, k = 1, 1
n, k = 1, 4
n, k = 3, 9

Solution().getHappyString(n, k)