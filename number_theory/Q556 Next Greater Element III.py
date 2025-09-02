# number theory - medium
class Solution:
    def nextGreaterElement(self, n: int) -> int:

        # core ideas:
        # 1) to obtain the smallest next larger number, prioritise 
        # re-arranging digits from the least significant to the most (backward scan)

        # 2) double for-loop to determine the best swap
        num_str = str(n)

        ans = -1
        for i in range(len(num_str)-2, -1, -1):

            # next larger digit, and swap index
            nld, si = 10, -1
            for j in range(i+1, len(num_str)):
                if int(num_str[i]) < int(num_str[j]) < nld:
                    nld, si = int(num_str[j]), j

            if nld < 10:
                # bring the swapped digit to the i-th index - (1)
                # and sort the rest of digits to obtain smallest - (2)
                p1 = num_str[:i] + num_str[si]
                p2 = ''.join(sorted(num_str[i] + num_str[i+1:si] + num_str[si+1:]))
                ans = int(p1 + p2)
                break

        return ans if ans < pow(2, 31) else -1
    
n = 12
n = 12343
n = 124651
n = 2147483486

Solution().nextGreaterElement(n)