# number theory - medium
class Solution:
    def bulbSwitch(self, n: int) -> int:
        def simulate(n):
    
            # first round is just to light up all bulbs
            states = [1] * n
            
            for rnd in range(n-1):
                # rnd is 1-indexing
                rnd += 1
                for idx in range(rnd, n, rnd+1):
                    states[idx] = 1 - states[idx]
                    
            return sum(states)
            
        # for n in range(1, 101):
        #     print('n = ', n, ', res = ', simulate(n))
            
        # notice that the result grows in a particular pattern
        # i.e. res = 1 up to n = 3, res = 2 up to n = 8, res = 3 up to n = 15
        # we could summarise this behaviour w/ a formula

        if n == 0: return 0

        decrement, res = 3, 0
        while n > 0:
            
            n -= decrement
            # following the arithmetic series: 3, 5, 7, 9, 11, ....
            decrement += 2
            # increment res
            res += 1
            
        return res

# the mathy version - solving the complement problem
class Solution:
    def bulbSwitch(self, n: int) -> int:
        # first realisation is that a bulb at any pos. is turned on
        # if it gets toggled ODD times, and turned off for EVEN times

        # for the light bulb at 8-th pos for example, it will be toggled
        # on round 1, 2, 4, 8, and it is no surprise that [1,2,4,8] are the 
        # divisible factors of 8, and a size of 4 (even)
        # means 8-th light bulb is surely off in the end

        # how do we find the divisible factors of an integer efficiently?
        # let say for pos 18, we have divisible factors [1,2,3,6,9,18]
        # but we don't need to iterate up to 18 to know all, in fact
        # we only need to iterate up to sqrt(18): i.e. (1,2,3) are found, 
        # and obtain (18/1, 18/2, 18/3) = (18, 9, 6) respectively

        # notice that since that we are only interested in whether the
        # number of toggles is odd OR even for a light bulb, and that
        # the pairing above always results in even count, then in order
        # to become odd cnt, the number has to be square-rootable

        # by solving the complement: how many numbers in [1, n] are 
        # square-rootable, we directly obtain the positions of bulb
        # at which there will be odd toggles, hence turned on after all
        on = 0
        for i in range(1, n+1):
            if pow(i, 2) > n:
                break
            on += 1

        return on
    
n = 3
n = 100
n = 99999999

Solution().bulbSwitch(n)