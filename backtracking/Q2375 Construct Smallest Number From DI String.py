# backtracking - medium
class Solution:
    def recursive_lexi_form(self, seq, digits_used):

        if len(seq) == len(self.pattern) + 1:
            self.soln = ''.join(seq)
            return
        
        start_num = int(seq[-1]) + 1 if seq and self.pattern[len(seq)-1] == 'I' else 1
        end_num = int(seq[-1]) - 1 if seq and self.pattern[len(seq)-1] == 'D' else 9

        for num in range(start_num, end_num+1):

            if num not in digits_used:
                seq.append(str(num))
                digits_used.add(num)

                self.recursive_lexi_form(seq, digits_used)

                # backtracking
                seq.pop()
                digits_used.discard(num)

            if self.soln: break

    def smallestNumber(self, pattern: str) -> str:
        self.pattern = pattern
        self.soln = None

        self.recursive_lexi_form([], set())
        return self.soln
    
pattern = "IIIDIDDD"
pattern = "DDD"

Solution().smallestNumber(pattern)