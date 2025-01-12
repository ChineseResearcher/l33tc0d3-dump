class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        # general idea is to take care of the locked ')' then locked '('
        # what makes this question very difficult is that we have to realise locked ')'
        # should be preferably balanced by any locked '(' that came before

        # odd-length str can never balance
        if len(s) % 2 == 1: return False

        # initiate two stacks storing the (bracket, index) of locked '(' and unlocked respectively
        stack_lb_locked, stack_unlocked = [], []
        for idx, brkt in enumerate(s):

            if brkt == ')' and locked[idx] == '1':

                if not stack_lb_locked and not stack_unlocked:
                    return False

                # prefer to use from stack_lb_locked
                # as we want to be left with as many wildcards as possible
                if stack_lb_locked:
                    stack_lb_locked.pop()
                    continue

                stack_unlocked.pop()
            
            elif locked[idx] == '0':
                # unlocked '(' or ')' both treated as wildcards
                stack_unlocked.append(['*', idx])

            elif brkt == '(' and locked[idx] == '1':
                stack_lb_locked.append([brkt, idx])

        # one trivial result is that if no locked '(' remains after above
        # we are left with only wildcards that are surely even in length (so valid)
        if not stack_lb_locked: return True
    
        # iterate stack_unlocked from backwards to balance the remaining locked '('
        for brkt, idx in stack_unlocked[::-1]:
            
            # at any point, if the rightmost locked '(' cannot be
            # balanced by the rightmost unlocked '*', then we fail
            if idx < stack_lb_locked[-1][1]:
                return False

            stack_lb_locked.pop()
            if not stack_lb_locked: return True

        # there can still be locked '(' left after we exhausted all unlocked '*'
        if stack_lb_locked: return False

s, locked = "))()))", "010100"
s, locked = "()))", "1010"
s, locked = "((", "00"
s, locked = ")(", "00"
s, locked = "())()))()(()(((())(()()))))((((()())(())", "1011101100010001001011000000110010100101"
s, locked = "((()(()()))()((()()))))()((()(()", "10111100100101001110100010001001"

Solution().canBeValid(s, locked)
