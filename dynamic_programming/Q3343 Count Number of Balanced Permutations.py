# dp - hard
from collections import Counter
class Solution:
    def countBalancedPermutations(self, num: str) -> int:
        
        def recursive_permute(currDigit, pLen, pSum):
            # take the perspective of thee odd-index partition
            # i.e. if num is length n, we want to achieve 
            # targetSum = sum(num) // 2 AND targetLen = len(num) // 2
            
            # note that when we arrive at currDigit = 10, there's only
            # one time that the pSum and pLen satisfy above
            # we need to return the total number of permutations:
            # i.e. if we consider two partitions with size H & K
            # if we disregard the repeated elements in each partition
            # then we would have H! * K!
            if currDigit == '10':
                if pSum == targetSum and pLen == targetLen:
                    return (fac[targetLen] * fac[n - targetLen]) % MOD
                return 0
            
            # invalid
            if pLen > targetLen or pSum > targetSum:
                return 0
            
            if (currDigit, pLen, pSum) in dp:
                return dp[(currDigit, pLen, pSum)]
            
            curr_res = 0
            # iterate through the number of times that current digits can be used
            for freq in range(digit_freq[currDigit]+1):
                res = recursive_permute(str(int(currDigit)+1),
                                        pLen + freq,
                                        pSum + freq * int(currDigit))
                
                # apply combinatorics to discount duplicated elements
                # note: if we just apply // factorials for respective frequencies
                # in both partitions, because of the MOD causing roll-over, the result
                # would be inaccurate. A workaround is to apply fermat's little theorem
                # to find the inverser factorial properly considering MOD
                res *= invFac[freq]
                res %= MOD
                res *= invFac[digit_freq[currDigit] - freq]
                res %= MOD 

                curr_res += res
                curr_res %= MOD
                
            dp[(currDigit, pLen, pSum)] = curr_res
            return curr_res

        n = len(num)
        str_sum = sum([int(x) for x in num])
        # if total digits sum is odd, then it's impossible to divide
        # the sum into two partitions (i.e. odd-index partition & even-index partition)
        if str_sum % 2 != 0:
            return 0

        targetSum, targetLen = str_sum // 2, n // 2

        MOD = int(1e9 + 7)
        # precompute factorials & inverse-factorials
        fac, invFac = [0] * (n+1), [0] * (n+1)
        fac[0] = 1
        for i in range(1, n+1):
            fac[i] = (i * fac[i-1]) % MOD

        invFac[0] = 1
        for i in range(1, n+1):
            invFac[i] = pow(fac[i], MOD-2, MOD)

        digit_freq = Counter(num)
        dp = dict()
        return recursive_permute('0',0,0)
    
num = "123"
num = "112"
num = "12345"
num = "2719707018802576"
nums = "02827971717103551"
num = "1234567890" * 8 # testing max. length

Solution().countBalancedPermutations(num)