# counting - medium
class Solution:
    # this question was solved using a novel algorithm: Sieve of Eratosthenes
    # solution runs in O(N*LogLogN) time -> took 3500ms which is strange
    def closestPrimes(self, left: int, right: int):
        # create an array of size = right+1 (1-indexing)
        isPrime = [True] * (right+1)

        # first prime number is 2
        for num in range(2, int(right**0.5)+1):
            
            if isPrime[num]:
                
                # important idea of Sieve of Eratosthenes' multiples marking
                # is that for a unmarked prime number, say 7, we start marking
                # from 7 * 7 onwards: 7*7, 7*8, ..., until it breaches n
                # Why? Because 7*6 = 42 would have been marked by 2's multiples
                # or 7*5 = 35 would have been marked by 5's multiples

                multiplier = num
                while num * multiplier <= right:
                    isPrime[num * multiplier] = False
                    multiplier += 1

        # iterate through isPrime for range [left, right], again first prime starts at 2
        rangePrimes = [i for i in range(max(left,2), right+1) if isPrime[i]]

        # init our ans to a inf. range
        ans = [float('-inf'), float('inf')]
        for i in range(len(rangePrimes)-1):
            if rangePrimes[i+1] - rangePrimes[i] < ans[1] - ans[0]:
                ans[0], ans[1] = rangePrimes[i], rangePrimes[i+1]

            # small optimisation, since all prime numbers are odd
            # min. diff is just 2
            if ans[1] - ans[0] == 2: return ans

        return ans if ans[0] > float('-inf') else [-1, -1]

class Solution:
    # forget about Sieve of Eratosthenes, there's ONE critical optimisation
    # to identify twin primes (diff. <= 2) as early as possible to make our
    # O(n*sqrt(n)) solution run much faster -> only took 35ms
    def isPrime(self, num):

        # first prime number starts at 2
        if num < 2:
            return False
        
        # search range would be up to the sqrt of num
        # note that since any multiples of 2 are not prime
        # our increment is set to grow by two from 3 onwards
        searchRange = [2] + [i for i in range(3, int(num**0.5)+1 , 2)]
        for factor in searchRange:
            if factor != num and num % factor == 0:
                return False
            
        return True

    def closestPrimes(self, left: int, right: int):
        rangePrimes = []
        for num in range(left, right+1):
            if self.isPrime(num):
                # optimisation: the smallest diff. between two prime numbers is at most 2
                # e.g. (2,3), having diff. 1 OR (11,13) having diff. 2
                if rangePrimes and num <= rangePrimes[-1] + 2: return [rangePrimes[-1], num]

                rangePrimes.append(num)

        # if there's fewer than 2 primes in the range provided, there's no answer
        if len(rangePrimes) < 2: return [-1, -1]

        # init our ans to a inf. range
        ans = [float('-inf'), float('inf')]
        for i in range(len(rangePrimes)-1):
            if rangePrimes[i+1] - rangePrimes[i] < ans[1] - ans[0]:
                ans[0], ans[1] = rangePrimes[i], rangePrimes[i+1]

        return ans if ans[0] > float('-inf') else [-1, -1]
    
left, right = 10, 19
left, right = 4, 6
# input size up to 1e6
left, right = 2, 1000000
left, right = 255322, 929209

Solution().closestPrimes(left, right)