# dp - hard
lc = "abcdefghijklmnopqrstuvwxyz"
# map letters to index in range [0...25]
P = {c: ord(c) - ord('a') for c in lc}
class Solution:
    def appealSum(self, s: str) -> int:

        n = len(s)
        # key ideas:
        # 1) use a prev array to record the previous appearing index of a letter
        # 2) consider a linear DP where dp[i] stores the sum of appeal of all
        # substrings ending at index i
        # 3) optimize to O(1) space by only keeping the prev. dp val.
        prev, prevDP, ans = [-1] * 26, 1, 1
        prev[P[s[0]]] = 0

        for i in range(1, n):
            j = P[s[i]]
            increment = i - prev[j]
            # update position of appearing char.
            prev[j] = i
            # curr. result builds on prev. DP value
            currDP = increment + prevDP
            ans += currDP
            prevDP = currDP

        return ans

s = "code"
s = "abbca"

Solution().appealSum(s)