# dp - medium
class Solution:
    def maxSubstringLength(self, s: str, k: int) -> bool:

        if k == 0:
            return True

        n = len(s)
        # from string s, mark the first / last appearance index of every
        # character that appears in the string
        char_idx = dict()
        for idx, char in enumerate(s):

            if char not in char_idx:
                char_idx[char] = [idx, idx]

            char_idx[char][1] = idx

        # retrieve the indice pairs and sort them
        blocks = list(char_idx.values())
        # addtional step:
        # we must extend the blocks if necessary to cover the full
        # range of any characters appearing in 
        final_blocks = []
        for l, r in blocks:
            
            ul, ur = l, r
            # keep updating (ul,ur) to make sure all index i
            # s.t. any character at s[i] where ul <= u <= ur have first and
            # last appearance within (ul,ur)
            while True:

                nl, nr = ul, ur
                char_set = set(s[ul:ur+1])
                for x in char_set:
                    nl = min(nl, char_idx[x][0])
                    nr = max(nr, char_idx[x][1])

                if nl == ul and nr == ur:
                    break

                ul, ur = nl, nr

            final_blocks.append([ul, ur])

        blocks = sorted(final_blocks)

        # note that m is maximally 26 in size
        m = len(blocks)
        dp = [0] * m
        for i in range(m):
            if blocks[i][1] - blocks[i][0] + 1 < n:
                dp[i] = 1

        maxDisjointCnt = dp[0]
        for i in range(1, m):
            for j in range(i):
                if blocks[j][1] < blocks[i][0]:
                    dp[i] = max(dp[i], 1 + dp[j])

            maxDisjointCnt = max(maxDisjointCnt, dp[i])

        return maxDisjointCnt >= k
    
s, k = "abcdbaefab", 2
s, k = "cdefdc", 3
s, k = "abeabe", 0
s, k = "cbcaba", 1

Solution().maxSubstringLength(s, k)