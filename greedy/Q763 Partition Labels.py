# greedy - medium
from string import ascii_lowercase as asc
class Solution:
    def partitionLabels(self, s:str):   

        n = len(s)

        # idea is to first construct a dictionary storing 
        # the first/last appearance idx of all characters possible
        char_start_end = {c:[] for c in asc}
        for char in asc:

            for idx, str_char in enumerate(s):
                if str_char == char:
                    char_start_end[char].append(idx)
                    break

            for idx, str_char in enumerate(s[::-1]):
                if str_char == char:
                    char_start_end[char].append(n-idx-1)
                    break

        # for characters that do appear, we take their first/last appearance idx
        # as an interval and sort them altogether
        line_sweep = sorted([v for k,v in char_start_end.items() if v])

        # ans records the indices at which a new partition is formed
        ans = []

        # for the line_sweep arr, we are essentially doing the "merge interval" problem
        for i in range(1, len(line_sweep)):

            if line_sweep[i][0] <= line_sweep[i-1][1]:
                line_sweep[i] = [min(line_sweep[i-1][0], line_sweep[i][0]), 
                                 max(line_sweep[i-1][1], line_sweep[i][1])]
            else:
                ans.append(line_sweep[i][0])

        # collect the last interval
        ans.append(line_sweep[-1][1]+1)

        # final ans is just the difference between all recorded indices in ans
        return [ans[0]] + [ans[i] - ans[i-1] for i in range(1, len(ans))]
    
s = "ababcbacadefegdehijhklij"
s = "eccbbbbdec"

Solution().partitionLabels(s)