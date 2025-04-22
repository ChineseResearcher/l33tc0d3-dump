# number theory - medium
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:

        def getDecimals(numerator, denominator):
            # initiate a set storing the divisions encountered
            divSet = set([numerator])
            # maintain a dict to indicate which ops does a divison fall under
            divOps = {numerator:0}

            curr, decimals, ops = numerator, [], 0
            # the loop for decimal subproblems
            while True:

                while curr < denominator:
                    curr *= 10
                    if curr in divSet:
                        return decimals[:divOps[curr]] + ['('] + decimals[divOps[curr]:] + [')']
                    decimals.append(str(curr // denominator))

                    if curr < denominator:
                        divSet.add(curr) 
                        ops += 1
                        divOps[curr] = ops

                curr = curr - (curr // denominator) * denominator
                # detect exact divisions (e.g. 4 / 8 = 0.5)
                if curr == 0:
                    break
                
                # detect recurring decimals
                if curr in divSet:
                    return decimals[:divOps[curr]] + ['('] + decimals[divOps[curr]:] + [')']
                divSet.add(curr) 
                ops += 1
                divOps[curr] = ops

            return decimals

        # edge case: numerator = 0
        if numerator == 0:
            return "0"

        sign = 1
        # pre-processing the -ve sign(s) of numerator & denominator
        if numerator < 0 and denominator < 0:
            numerator = -numerator
            denominator = -denominator

        elif numerator < 0 or denominator < 0:
            # either being negative 
            sign = -1

        # separate the division into the non-decimal and decimal (if any) parts
        intPart = int(abs(numerator) / abs(denominator))

        # decrement numerator to decimal division (if possible)
        if intPart >= 0 and sign == 1:
            numerator -= abs(numerator) // abs(denominator) * denominator
        else:
            numerator += abs(numerator) // abs(denominator) * denominator

        signStr = '' if sign == 1 else '-'
        if numerator != 0:
            return signStr + str(intPart) + '.' + ''.join(getDecimals(abs(numerator), abs(denominator)))
        else:
            return signStr + str(intPart)
        
numerator, denominator = 4, 333
numerator, denominator = 400, 333
numerator, denominator = 41, 8
numerator, denominator = 40, 8
numerator, denominator = 10, 23
numerator, denominator = 1, 6
numerator, denominator = -50, 8
numerator, denominator = 1, -1
numerator, denominator = 7, -12
numerator, denominator = 1, 214748364

Solution().fractionToDecimal(numerator, denominator)