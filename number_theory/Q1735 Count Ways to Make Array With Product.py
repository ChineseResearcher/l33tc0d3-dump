# number theory - hard
import math
class Solution:
    def prime_factorisation(self, num):
        # given a integer num, deconstruct the integer into
        # its prime factorisation, e.g. 24 = 2^3 * 3
        # so we return [(2,3),(3,1)]
        if num < 2:
            return []
        
        searchRange = [2] + [x for x in range(3, int(num ** 0.5) +1)]
        
        pf = []
        for divisor in searchRange:
            
            if num % divisor == 0:
                p_cnt = 0
                while num >= divisor and num % divisor == 0:
                    p_cnt += 1
                    num //= divisor
                pf.append((divisor, p_cnt))
            
            if num == 1:
                break
                
        if num != 1:
            pf.append((num, 1))
                
        return pf

    def waysToFillArray(self, queries):
        
        MOD = int(1e9 + 7)
        # the approach is highly similar to LC2338, where a partition
        # technique is used to solve the underlying combinatorial problem
        ans_arr = []
        for n, k in queries:
            
            # we first compute the prime factor 
            # representation of target product k
            pf = self.prime_factorisation(k)
            
            # the underlying combinatorial problem:
            # for a prime factor y, how many ways are there to place
            # all occurrences of y into the n-size arr. (imagine n buckets)
            curr_ans = 0
            
            mul = 1
            for prime, freq in pf:
                mul *= math.comb(n + freq - 1, freq)
                mul %= MOD
                
            curr_ans += mul
            curr_ans %= MOD
            # record ans. for curr. query
            ans_arr.append(curr_ans)
            
        return ans_arr
    
queries = [[2,6],[5,1],[73,660]]
queries = [[1,1],[2,2],[3,3],[4,4],[5,5]]

Solution().waysToFillArray(queries)