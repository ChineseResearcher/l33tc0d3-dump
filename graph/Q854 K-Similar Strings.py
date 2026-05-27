# graph - hard
from collections import deque, defaultdict
class Solution:
    def kSimilarity(self, s1: str, s2: str) -> int:

        n = len(s1)

        q = deque([(0,s1)])
        visited = set([s1])

        ans = -1
        while q:

            swap, curr = q.popleft()
            if curr == s2:
                ans = swap
                break

            char_idx = defaultdict(list)
            for i in range(n):
                char_idx[curr[i]].append(i)

            # find the first index that mismatches
            for i in range(n):
                if curr[i] != s2[i]:
                    break

            # perform swaps
            for j in char_idx[s2[i]]:
                if j < i: continue
                new_str = curr[:i] + s2[i] + curr[i+1:j] + curr[i] + curr[j+1:]
                if new_str not in visited:
                    q.append((swap+1, new_str))
                    visited.add(new_str)

        return ans

s1, s2 = "ab", "ba"
s1, s2 = "abc", "bca"
s1, s2 = "abcdefabcdefabcdef", "cdcedffebbafbdaace"

Solution().kSimilarity(s1, s2)