# dp - hard
class Solution:
    def recursive_build(self, pos, tight, breached):
    
        if pos == self.n - len(self.s):
            if tight:
                if not breached:
                    if self.subproblem == 'start':
                        return 1 if self.s < self.bs[-len(self.s):] else 0
                    elif self.subproblem == 'finish':
                        return 1 if self.s <= self.bs[-len(self.s):] else 0

                else:
                    return 0

            else:
                return 1 if not breached else 0
        
        upper_bound = self.digits[pos] if tight else 9
        if (pos, tight, breached) in self.dp: return self.dp[(pos, tight, breached)]
        
        curr_cnt  = 0
        for digit in range(0, upper_bound + 1):
            curr_cnt += self.recursive_build(pos + 1, 
                                             tight and (digit == upper_bound),
                                             breached or (digit > self.limit))
            
        self.dp[(pos, tight, breached)] = curr_cnt
        return curr_cnt

    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        # for digit DP problem, we usually have an upper bound to search
        # until and a digit limit constraint, no digits larger than k

        # we can treat this problem as two sub-problems, each searching up
        # to the bound "start" & "finish", and we would be able to say there's
        # 0 occurrence if the upper bound is smaller than s to begin with

        def set_vars(ub):
            # define upper bound as a string
            bs = str(ub)
            digits = list(map(int, bs))
            n = len(bs)
            # set memo dict
            dp = dict()
            
            return bs, digits, n, dp

        self.s, self.limit = s, limit

        # to avoid the case where start == s which leads to undercounting
        if start <= int(self.s):
            ans_start = 0
        else:
            self.bs, self.digits, self.n, self.dp = set_vars(start)
            self.subproblem = 'start'
            ans_start = self.recursive_build(0, True, False)
            
        if finish < int(self.s):
            ans_finish = 0
        else:
            self.bs, self.digits, self.n, self.dp = set_vars(finish)
            self.subproblem = 'finish'
            ans_finish = self.recursive_build(0, True, False)
        
        return ans_finish - ans_start
    
start, finish, limit, s = 1, 6000, 4, "124"
start, finish, limit, s = 15, 215, 6, "10"
start, finish, limit, s = 1000, 2000, 4, "3000"
start, finish, limit, s = 20, 1159, 5, "20"
start, finish, limit, s = 1, 971, 9, "71"

Solution().numberOfPowerfulInt(start, finish, limit, s)