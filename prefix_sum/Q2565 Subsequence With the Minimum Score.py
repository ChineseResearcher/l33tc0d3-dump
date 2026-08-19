# prefix sum - hard
class Solution:
    def minimumScore(self, s: str, t: str) -> int:

        m, n = len(s), len(t)
        fmin = lambda a, b: a if a < b else b
        fmax = lambda a, b: a if a > b else b
        # key ideas:
        # 1) suppose the best removed section [0, ..., (l, ..., r), ..., n - 1]
        # is enclosed by l & r, then it must satisfy that [0...l - 1] and [r + 1...n - 1]
        # are both valid prefix and suffix subsequences respectively 

        # 2) pre-process "s" and "t" with two pointers to track:
        # - for prefix array, with length equal to t, pf_t[i] indicates the matching index in "s"
        # - for suffix array, with length equal to s, sf_s[i] indicates the count of matched suffix
        # in t by using s[i...m-1]

        # 3) iterate through "t" and use the preprocessed info to determine smallest [l, r]

        pf_t, j = [-1] * n , 0
        for i in range(n):
            while j < m and s[j] != t[i]:
                j += 1

            if j < m:
                pf_t[i] = j
                j += 1 
            else:
                break

        sf_s, j = [0] * m, n - 1
        for i in range(m - 1, -1, -1):
            if i < m - 1:
                sf_s[i] = sf_s[i + 1]
            if j >= 0 and s[i] == t[j]:
                sf_s[i] += 1
                j -= 1

        ans = n
        for i in range(n):
            if i > 0 and pf_t[i - 1] == -1:
                break

            # define our partition s.t. we only use s[p:]
            p = pf_t[i - 1] if i > 0 else -1
            # get suffix match count
            c = sf_s[p + 1] if p + 1 < m else 0
            ans = fmin(ans, fmax(n - i - c, 0))

        return ans

s, t = "abca", "c"
s, t = "cde", "xyz"
s, t = "abacaba", "bzaa"
s, t = "adebddaccdcabaade", "adbae"
s, t = "acdedcdbabecdbebda", "bbecddb"

Solution().minimumScore(s, t)