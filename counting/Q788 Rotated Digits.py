# counting - medium
class Solution:
    def rotatedDigits(self, n: int) -> int:
        
        ans = 0
        for x in range(n+1):

            isValid, isDiff = True, False
            for c in str(x):
                if c in ['3','4','7']:
                    isValid = False
                    break

                if c in ['2','5','6','9']:
                    isDiff = True

            if isValid and isDiff:
                ans += 1

        return ans

n = 1
n = 2
n = 10

Solution().rotatedDigits(n)