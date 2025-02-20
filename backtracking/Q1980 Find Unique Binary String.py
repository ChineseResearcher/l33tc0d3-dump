# backtracking - medium
class Solution:
    def recursive_bin_str(self, seq):

        if len(seq) == self.n:
            self.soln.extend(seq)
            return
        
        for char in ['0', '1']:
            seq.append(char)
            if ''.join(seq) not in self.avoid:
                self.recursive_bin_str(seq)

            # backtrack
            seq.pop()

            # early stopping
            if self.soln: break

    def findDifferentBinaryString(self, nums):
        # nums contain unique binary strings of length n, maximally
        # 16 such binary strings of length 16
        self.n = len(nums)

        # set the numbers for efficient lookup
        self.avoid = set(nums)

        self.soln = []
        self.recursive_bin_str([])
        return ''.join(self.soln)
    
nums = ["01","10"]
nums = ["00","01"]
nums = ["111","011","001"]

Solution().findDifferentBinaryString(nums)