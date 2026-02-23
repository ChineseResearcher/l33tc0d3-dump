# bit manipulation - medium
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:

        n = len(s)
        # key ideas:
        # 1) maintain a rolling hash of length-k binary code
        # 2) forgo / ingest an old / new bit for every index of string s
        rhash = int('0b' + s[:k], 2)

        seen = set()
        seen.add(rhash)

        for i in range(k, n):
            rhash <<= 1
            # forgo k-th bit
            rhash &= ~(1 << k)
            # set a new bit if s[i] = '1'
            if s[i] == '1':
                rhash |= (1 << 0)
            seen.add(rhash)

        return len(seen) == pow(2,k)
    
s, k = "00100110", 2
s, k = "0110", 1
s, k = "0110", 2

Solution().hasAllCodes(s, k)