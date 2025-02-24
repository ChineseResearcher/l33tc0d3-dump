# recursion - medium
class Solution:
    def recursiveLexiNumber(self, i, base, series):
        for num in range(i*base, i*base+base):
            if num > self.n:
                return
            else:
                series.append(num)
                self.recursiveLexiNumber(num, base, series)

    def lexicalOrder(self, n):
        self.n = n
        ans = []

        for i in range(1,10):
            
            if i <= self.n:
                ans.append(i)
                series = []
                self.recursiveLexiNumber(i, 10, series)
                ans.extend(series)

        return ans
    
n = 100
n = 34
n = 13
n = 2

Solution().lexicalOrder(n)