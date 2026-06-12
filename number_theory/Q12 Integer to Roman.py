# number theory - medium
class Solution:
    def intToRoman(self, num: int) -> str:

        # key ideas:
        # 1) explore divisors from big to small, i.e. [1000, 100, 10, 1]
        # 2) when we get special quotient such as following we map separately
        # 400 / 900 -> CD / CM
        # 40 / 90 -> XL / XC
        # 4 / 9 -> IV / IX

        DIV_MAP = {1: 'I', 5: 'V',
                10: 'X', 50: 'L',
                100: 'C', 500: 'D',
                1000: 'M'}

        DIV_MAP_2 = {4: 'IV', 9: 'IX',
                    40: 'XL', 90: 'XC',
                    400: 'CD', 900: 'CM'}

        # first mod by 1000
        ans = [(num // 1000) * DIV_MAP[1000]]
        num %= 1000

        for d in [100, 10, 1]:
            q = num // d
            if q == 4 or q == 9:
                ans.append(DIV_MAP_2[q * d])
            else:
                # address 5 / 50 / 500
                d_mul_5 = d * 5
                if num >= d_mul_5:
                    ans.append(DIV_MAP[d_mul_5])
                    num -= d_mul_5 # update num
                    q = num // d    # update q

                ans.append(q * DIV_MAP[d])

            num %= d

        return ''.join(ans)
    
num = 58
num = 1994
num = 3749

Solution().intToRoman(num)