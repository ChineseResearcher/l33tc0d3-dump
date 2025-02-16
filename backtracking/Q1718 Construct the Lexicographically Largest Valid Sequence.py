# backtracking - medium
class Solution:
    def recursive_lexi_form(self, curr_idx, seq, assigned_num, assigned_idx):

        # print(curr_idx, seq, assigned_num)
        if curr_idx == 1 + 2 * (self.n-1):
            self.soln.extend(seq[:])
            return
        
        # case 1: curr_idx is already assigned by a prev. num
        if curr_idx in assigned_idx:
            seq.append(assigned_idx[curr_idx])
            self.recursive_lexi_form(curr_idx+1, seq, assigned_num, assigned_idx)
            seq.pop()
        
        # case 2: curr_idx is unassigned, explore valid numbers
        else:
            for num in range(self.n, 0, -1):
                if num not in assigned_num and (curr_idx + num if num != 1 else -1) not in assigned_idx:
                    seq.append(num)
                    # "1" can only appear once
                    next_idx = curr_idx + num if num != 1 else -1
                    assigned_num[num] = next_idx
                    assigned_idx[next_idx] = num 

                    self.recursive_lexi_form(curr_idx+1, seq, assigned_num, assigned_idx)

                    # backtracking
                    seq.pop()
                    del assigned_num[num]
                    del assigned_idx[next_idx]

                    # we only care about finding the lexicographically largest soln
                    if self.soln: break

    def constructDistancedSequence(self, n):
        self.n = n
        self.soln = []
        self.recursive_lexi_form(0, [], dict(), dict())

        return self.soln
    
n = 2
n = 5

Solution().constructDistancedSequence(n)