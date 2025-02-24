# recursion - hard
class Solution:
    def numberToWords(self, num):
        # 2^31 = 2147483648, which means the largest possible unit is billion(s)
        ans = []
        num_str = str(num)
        units = ['', 'Thousand', 'Million', 'Billion']
        d = {0: "Zero", 1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven",
            8: "Eight", 9: "Nine", 10: "Ten", 11: "Eleven", 12: "Twelve", 13: "Thirteen", 14: "Fourteen",
            15: "Fifteen", 16: "Sixteen", 17: "Seventeen", 18: "Eighteen", 19: "Nineteen", 20: "Twenty",
            30: "Thirty", 40: "Forty", 50: "Fifty", 60: "Sixty", 70: "Seventy", 80: "Eighty", 90: "Ninety"}

        # unit_choice will start with index 0
        def helper(num_str, unit_choice, answer):
            
            curr_chunk = int(num_str[-3:])
            curr_ans = []

            hundreds = curr_chunk // 100
            tens = (curr_chunk - 100 * hundreds) // 10
            ones = curr_chunk - 100 * hundreds - 10 * tens

            if hundreds > 0:
                curr_ans.extend([d[hundreds], 'Hundred'])
            
            # direct ref. to d for tens + ones < 20
            if tens == 0 and ones > 0:
                curr_ans.append(d[ones])
            elif tens == 1:
                curr_ans.append(d[(10*tens + ones)])
            elif tens > 1:
                curr_ans.append(d[10*tens])
                if ones > 0:
                    curr_ans.append(d[ones])

            # lastly, deal with unit
            # case 1: unitless when this chunk is all zeroes
            if hundreds == tens == ones == 0:
                if len(num_str) <= 3: # special case: num = 0 so return 'zero'
                    curr_ans.append(d[0])
            # case 2: has unit as long as this chunk is non-zero
            else:
                if unit_choice > 0:
                    curr_ans.append(units[unit_choice])

            answer = curr_ans + answer

            next_chunk = num_str[:-3]
            if next_chunk:
                unit_choice += 1
                return helper(next_chunk, unit_choice, answer)
            else:
                return answer

        return ' '.join(helper(num_str, 0, ans))
    
num = 20
num = 100
num = 0
num = 10
num = 1000
num = 1234567
num = 1000000
num = 1001000
num = 1001000001

Solution().numberToWords(num)