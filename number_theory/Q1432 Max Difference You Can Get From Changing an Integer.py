# number theory - medium
class Solution:
    def maxDiff(self, num: int) -> int:
        
        numStr = str(num)

        # let a be the max possible int after replacement, and b be the min.
        for char in numStr:
            if char < '9':
                break

        a = numStr.replace(char, '9')
        # since we can't have leading 0s in the replaced int.
        # we would have to deal w/ two possible scenarios
        # 1) first integer start w/ 2-9, e.g. 9099
        # 2) first integer start w/ 1, e.g. 1099
        if numStr[0] != '1':
            b = numStr.replace(numStr[0], '1')

        else:

            char = '0'
            # we need to find the first int that is not 0/1
            # and turn it into '0' to obtain min.
            for c in numStr:
                if c not in ['0', '1']:
                    char = c
                    break

            b = numStr.replace(char, '0')

        return int(a) - int(b)
    
num = 555
num = 9
num = 123456
num = 111
num = 1101057

Solution().maxDiff(num)