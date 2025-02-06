# monotonic stack - medium
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        # a key intuition is that having smaller digits as early as possible
        # would make our overall num as small as possible
        n = len(num)
        monoAscStack = [num[0]] # monotonically ascending 

        for i in range(1,n):
            
            if not monoAscStack:
                monoAscStack.append(num[i])
                continue
            
            if monoAscStack and (num[i] >= monoAscStack[-1] or k == 0):
                monoAscStack.append(num[i])
                continue
            
            while monoAscStack and num[i] < monoAscStack[-1] and k > 0:
                monoAscStack.pop()
                k -= 1
            monoAscStack.append(num[i])

        while monoAscStack and k > 0:
            monoAscStack.pop()
            k -= 1
            
        minStr = ''.join(monoAscStack).lstrip('0')
        return minStr if minStr != '' else '0'
    
num, k = "1432219", 3
num, k = "10200", 1
num, k = "10", 2
num, k = "1173", 2
num, k = "996", 2
num, k = "1234567890", 9

Solution().removeKdigits(num,k)