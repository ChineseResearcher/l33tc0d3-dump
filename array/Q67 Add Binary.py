# array - easy
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        # key ideas:
        # 1) we make a & b lists of integers and process backwards
        # 2) keep processing as long as index pointers to either list >= 0
        # or we still have carry leftover

        m, n = len(a), len(b)
        a, b = list(map(int, a)), list(map(int, b))

        carry, i1, i2 = 0, m-1, n-1
        res = []
        while i1 >= 0 or i2 >= 0 or carry > 0:

            d1 = a[i1] if i1 >= 0 else 0
            d2 = b[i2] if i2 >= 0 else 0

            currSum = d1 + d2 + carry
            currD = currSum % 2
            res.append(currD)
            # update carry
            carry = 1 if currSum > 1 else 0

            i1 -= 1
            i2 -= 1

        return ''.join(list(map(str, res[::-1])))

a, b = "11", "1"
a, b = "11", "11"
a, b = "1010", "1011"

Solution().addBinary(a, b)