# number theory - hard
class Solution:
    def nearestPalindromic(self, n: str) -> str:
        if len(n) == 1: return str(int(n)-1)

        if len(n) % 2 == 0:

            left_half = n[:(len(n) // 2)]
            # the naive/default case would be left half plus its mirror image
            naive = left_half + left_half[::-1]
            # we assign a base number from which we add/minus one
            base_str = left_half

        # for odd-case, we have to consider middle digit
        else:
            mid = n[len(n) // 2]
            left_half = n[:(len(n) // 2)]
            naive = left_half + mid + left_half[::-1]
            base_str = left_half + mid

        # 1) find the smaller palindrome
        if int(naive) >= int(n):
            minus1 = str(int(base_str) - 1).lstrip('0')
            
            if not minus1 or len(minus1) < len(base_str):
                smaller = '9' * (len(n)-1)
            else:
                smaller = minus1 + minus1[::-1] if len(n) % 2 == 0 \
                else minus1[:-1] + minus1[-1] + minus1[:-1][::-1]
        else:
            smaller = naive

        # 2) find the bigger palindrome
        if int(naive) <= int(n):
            plus1 = str(int(base_str) + 1)

            if len(plus1) > len(base_str):
                bigger = '1' + '0' * (len(n)-1) + '1'
            else:
                bigger = plus1 + plus1[::-1] if len(n) % 2 == 0 \
                else plus1[:-1] + plus1[-1] + plus1[:-1][::-1]
        else:
            bigger = naive

        smaller_diff = abs(int(smaller) - int(n))
        bigger_diff = abs(int(bigger) - int(n))

        if smaller_diff <= bigger_diff:
            return smaller
        else:
            return bigger
        
n = "123"
n = "1212"
n = "1234"
n = "12121"
n = "1"
n = "1001"
n = "100001"
n = "999"
n = "10"

Solution().nearestPalindromic(n)