# greedy - medium
from collections import Counter
class Solution:
    def minimumPushes(self, word: str) -> int:

        # key ideas:
        # 1) as there can be multiple occurrences of the same char., 
        # we need to prioritise assigning an earlier position (in a key) to that char.
        # 2) sort the char. frequencies to help us decide greedy assignments
        freq = Counter(word)

        ans = 0
        for idx, f in enumerate(sorted(freq.values(), reverse=True)):
            ans += ((idx // 8) + 1) * f

        return ans

word = "abcde"
word = "xyzxyzxyzxyz"
word = "aabbccddeeffgghhiiiiii"

Solution().minimumPushes(word)