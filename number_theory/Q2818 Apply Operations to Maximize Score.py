# number theory - hard
# this question is a combination of three challenging parts:
# 1) find prime score for a large input of nums
# 2) determine the right bounds for computing number of subarrs.
# 3) optimise A^B%C using fast exponentiation
class Solution:
    def maximumScore(self, nums, k) -> int:

        def prime_score(n):
            score = 0
            
            # Check divisibility by 2
            if n % 2 == 0:
                score += 1
                while n % 2 == 0:
                    n //= 2
            
            # Check divisibility by odd numbers up to sqrt(n)
            for i in range(3, int(n**0.5) + 1, 2):
                if n % i == 0:
                    score += 1
                    while n % i == 0:
                        n //= i

            # If n is still greater than 1, it's a prime factor
            if n > 1:
                score += 1
            
            return score

        def fast_exponentiation(A, B, C):
            # this is used in the final aggregation step
            result = 1 
            A = A % C
            
            while B > 0:
                # If B is odd, multiply A with result
                if B % 2 == 1:  
                    result = (result * A) % C

                # Square A
                A = (A * A) % C  
                # Reduce exponent by half
                B //= 2  
            
            return result

        # use a dict to avoid unnecessary re-calculation
        score_dict = dict()

        # with spf and score helper, we pre-compute the prime score for
        # each number in nums, with limit up to max(nums)
        pscore = []
        for num in nums:
            if num not in score_dict:
                score_dict[num] = prime_score(num)

            pscore.append(score_dict[num])

        n = len(nums)
        # an important step to solving this question after prime
        # score is pre-computed is to apply monotonic stack and
        # find the number of possible subarrs. with pscore[i] being
        # the highest prime score at the smallest index
        # find prev. greater or equal using monoStack
        prev_ge = [-1] * n
        monoStack = []

        # iterate backwards
        for i in range(n-1, -1, -1):

            while monoStack and pscore[i] >= pscore[monoStack[-1]]:
                prev_ge[monoStack.pop()] = i

            monoStack.append(i)

        # find next strictly greater 
        next_g = [n] * n
        monoStack = []

        # iterate forward
        for i in range(n):

            while monoStack and pscore[i] > pscore[monoStack[-1]]:
                next_g[monoStack.pop()] = i

            monoStack.append(i)

        # apply sorting to pscore & number, storing its idx alongside
        asc = sorted([(nums[i], pscore[i], i) for i in range(n)])

        # we would process the multiplication with the highest
        # prime score, break tie by actual numbers
        ans = 1
        while k > 0 and asc:

            currNum, _, currIdx = asc.pop()
            # determine the number of possible subarrs. with
            # currNum being the target number
            subarr_cnt = (next_g[currIdx] - 1 - currIdx + 1) * (currIdx - (prev_ge[currIdx] + 1) + 1)
            
            ans *= fast_exponentiation(currNum, min(subarr_cnt, k), int(1e9 + 7))
            
            # decrement k
            k -= subarr_cnt

        return ans % int(1e9 + 7)
    
nums, k = [8,3,9,3,8], 2
nums, k = [19,12,14,6,10,18], 3
nums, k = [3289,2832,14858,22011], 6

Solution().maximumScore(nums, k)