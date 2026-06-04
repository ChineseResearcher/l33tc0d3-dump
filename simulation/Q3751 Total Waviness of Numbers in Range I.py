# simulation - medium
class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        
        ans = 0
        for x in range(num1, num2+1):
            s = str(x)
            k = len(s)
            for i in range(1, k-1):
                if s[i] > s[i-1] and s[i] > s[i+1]:
                    ans += 1
                if s[i] < s[i-1] and s[i] < s[i+1]:
                    ans += 1

        return ans
    
num1, num2 = 120, 130
num1, num2 = 198, 202
num1, num2 = 4848, 4848

Solution().totalWaviness(num1, num2)