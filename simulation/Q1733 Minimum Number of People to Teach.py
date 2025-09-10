# simulation - medium
from typing import List
class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:

        canSpeak = dict()
        for i, l in enumerate(languages):
            canSpeak[i+1] = set(l)

        # pre-compute the pairs who can speak a common lang.
        canTalk = set()
        for u, v in friendships:
            if canSpeak[u] & canSpeak[v]:
                canTalk.add((u, v))

        ans = float('inf')
        for new_lang in range(1, n+1):

            taught = set()
            for u, v in friendships:
                # if already can speak a common lang.
                if (u, v) in canTalk:
                    continue

                # otherwise, teach the new lang.
                if new_lang not in canSpeak[u]:
                    taught.add(u)
                if new_lang not in canSpeak[v]:
                    taught.add(v)

            ans = min(ans, len(taught))
            
        return ans
    
n, languages, friendships = 2, [[1],[2],[1,2]], [[1,2],[1,3],[2,3]]
n, languages, friendships = 3, [[2],[1,3],[1,2],[3]], [[1,4],[1,2],[3,4],[2,3]]

Solution().minimumTeachings(n, languages, friendships)