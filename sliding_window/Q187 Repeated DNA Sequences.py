# sliding window - medium
from collections import deque
class Solution:
    def findRepeatedDnaSequences(self, s: str):
    
        n = len(s)
        # slide a window of fixed length 10 as the question wants repeating length-10 substring
        queue = deque([char for char in s[:10]])

        # a dict to track the frequency of substring pattern
        pattern = dict()
        pattern[''.join(queue)] = 1

        for r in range(10, n):

            queue.popleft()
            queue.append(s[r])

            curr_pattern = ''.join(queue)
            if curr_pattern not in pattern:
                pattern[curr_pattern] = 1
            else:
                pattern[curr_pattern] += 1

        # answer
        return [k for k,v in pattern.items() if v > 1]
    
s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
s = "AAAAAAAAAAAAA"

Solution().findRepeatedDnaSequences(s)