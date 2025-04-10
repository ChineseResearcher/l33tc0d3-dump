# counting - medium
class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int):
        # edge case: both x, y = 1 would not grow
        if x == 1 and y == 1:
            return [2] if bound >= 2 else []

        x, y = max(x, y), min(x, y)
        # notice by enumerating the combinations of powers
        # even for a bound up to 10^6 it won't take many iterations
        ans = set()

        x_pow = 0
        while True:

            # equal sign is rejected too because 
            # we need to leave room for at least y^0 = 1
            if x ** x_pow >= bound:
                break

            if y == 1:
                ans.add(x ** x_pow + 1)
            
            else:
                y_pow = 0
                while True:
                    
                    curr_pow_int = x ** x_pow + y ** y_pow
                    if curr_pow_int > bound:
                        break

                    # otherwise, we record the valid res
                    ans.add(curr_pow_int)
                    y_pow += 1

            x_pow += 1

        return list(ans)
    
x, y, bound = 2, 3, 10
x, y, bound = 3, 5, 15
x, y, bound = 2, 1, 10
x, y, bound = 1, 1, 0

Solution().powerfulIntegers(x, y, bound)