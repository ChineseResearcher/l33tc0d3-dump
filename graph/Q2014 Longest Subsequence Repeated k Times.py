# graph - hard
from collections import Counter, deque
class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
    
        def detect(pat, s, k):

            pat = ''.join(pat) * k

            j = 0 # pointer for pat
            for char in s:

                if char == pat[j]:
                    j += 1
                    if j == len(pat):
                        return True
                    
            return False

        # perform a freq. count and only keep characters that 
        # have at least k occurrences initially
        freq = {key: v for key, v in Counter(s).items() if v >= k}

        # although tag suggests backtracking, which would check from
        # longest to shortest, BFS turns out to be much faster
        ans, q = '', deque([''])
        while q:

            curr = q.popleft()
            for char in freq.keys():

                new_pat = curr + char
                if detect(new_pat, s, k):
                    if len(new_pat) > len(ans):
                        ans = new_pat
                    else:
                        ans = max(ans, new_pat)

                    # bfs enqueue
                    q.append(new_pat)

        return ans
    
s, k = "letsleetcode", 2
s, k = "bb", 2
s, k = "ab", 2

Solution().longestSubsequenceRepeatedK(s, k)