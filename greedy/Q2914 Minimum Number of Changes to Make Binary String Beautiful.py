# greedy - medium
class Solution:
    def minChanges(self, s: str) -> int:
        
        n = len(s)
        # key ideas:
        # 1) the smallest partition is of length 2
        # 2) it is optimal to enforce all partitions to be length 2
        ans = 0
        for i in range(0, n - 1, 2):
            if s[i] != s[i + 1]:
                ans += 1
                
        return ans

s = "10"
s = "1001"
s = "0000"

Solution().minChanges(s)