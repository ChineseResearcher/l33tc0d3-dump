# dp - hard
class Solution:
    def recursive_cnt(self, pos, tight):
    
        if pos == self.k:
            return 0
        
        if (pos, tight) in self.dp: 
            return self.dp[(pos, tight)]
        
        ub = self.digits[pos] if tight else 9
        curr_cnt = 0
        for digit in range(0, ub + 1):
            
            nextTight = tight and digit == ub
            # depending on whether next digit pos is tight
            # calculate number of '1's for the curr. level
            one_cnt = 0
            if digit == 1:
                if pos + 1 == self.k:
                    one_cnt += 1
                else:
                    # the number of times that this curr '1' would
                    # appear depends on how many possible branches we have until we hit k
                    if nextTight:
                        j = pos + 1
                        while j < self.k:
                            one_cnt += (self.digits[j]) * pow(10, self.k-j-1)
                            j += 1
                        # also accrue the one single tight-only path
                        one_cnt += 1
                    else:
                        one_cnt += pow(10, self.k-pos-1)
            
            curr_cnt += one_cnt + self.recursive_cnt(pos + 1, nextTight)
            
        self.dp[(pos, tight)] = curr_cnt
        return curr_cnt

    def countDigitOne(self, n: int) -> int:
        self.k = len(str(n))
        self.digits = list(map(int, str(n)))

        self.dp = dict()
        return self.recursive_cnt(0, True)
    
n = 0
n = 13
n = 100
n = int(1e9)

Solution().countDigitOne(n)