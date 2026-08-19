# number theory - hard
import math
class Solution:
    def smallestNumber(self, num: str, t: int) -> str:

        # exclusion algo for invalid "t":
        # if t is factorised by any prime(s) not in the range [2, 9]
        # then num is surely divisible by t as we have a digit product 
        temp = t
        for i in range(2, 10):
            while temp % i == 0:
                temp //= i

        if temp > 1:
            return "-1"

        n = len(num)
        # key ideas:
        # 1) re-use the prefix of original number as much as possible, so
        # we enumerate possible suffix modications backwards
        # 2) for every curr. digit at index i, we start exploring at the next
        # higher digit, then fill the rest of digits with ones that are divisible
        # by t_now, i.e. the factors that the modified suffix have to contribute
        # for the whole new number to be divisible by "t"
        rem = [0] * (n + 1)
        rem[0] = t
        pos = n - 1

        num_list = list(num)
        for i in range(n):
            # longest usable prefix ends before the 1st zero
            if num_list[i] == "0":
                pos = i
                break
            rem[i + 1] = rem[i] // math.gcd(rem[i], int(num_list[i]))

        if rem[n] == 1:
            return num

        for i in range(pos, -1, -1):
            while True:
                # why next higher instead of num_list[i]?
                # we need to ensure new number >= curr. number
                num_list[i] = chr(ord(num_list[i]) + 1)
                if num_list[i] > "9":
                    break

                t_now = rem[i] // math.gcd(rem[i], int(num_list[i]))
                k = 9

                for j in range(n - 1, i, -1):
                    while t_now % k != 0:
                        k -= 1
                    t_now //= k
                    num_list[j] = str(k)

                if t_now == 1:
                    return "".join(num_list)

        ans = []
        original_t = t
        for i in range(9, 1, -1):
            while original_t % i == 0:
                ans.append(str(i))
                original_t //= i

        # edge case:
        # all positions in "num" is maxed out at 9
        # and we have no available higher digits to place as pivots
        # we apply padding of "1"s s.t. the final string is exactly longer by 1 char.  
        ans_str = "".join(ans)
        padding = max(n + 1 - len(ans_str), 0) 
        ans_str += "1" * padding

        return ans_str[::-1]

num, t = "19", 2
num, t = "10", 320
num, t = "1234", 256
num, t = "12", 22020096000
num, t = "9999999999999999999", 99995938560000

Solution().smallestNumber(num, t)