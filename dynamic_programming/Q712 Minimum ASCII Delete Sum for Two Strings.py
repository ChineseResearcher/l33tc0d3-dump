# dp - medium
class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        m, n = len(s1), len(s2)
        # 2D dp storing the min. ASCII deletion sum for subproblem
        # concerning up to s1[:i] and s2[:j]
        dp = [ [0] * (n+1) for _ in range(m+1)]

        # prefill for first row (delete s2) and first col (delete s1)
        for i in range(1, n+1):
            dp[0][i] = dp[0][i-1] + ord(s2[i-1])
            
        for i in range(1, m+1):
            dp[i][0] = dp[i-1][0] + ord(s1[i-1])
            
        for i in range(1, m+1):
            for j in range(1, n+1):
                
                # op1: inherit from s1[:i-1] & s2[:j-1]
                op1 = dp[i-1][j-1] + (0 if s1[i-1] == s2[j-1] else ord(s1[i-1]) + ord(s2[j-1]))
                
                # op2: inherit from s1[:i] & s2[:j-1], delete curr s2 char
                op2 = dp[i][j-1] + ord(s2[j-1])
                
                # op3: inherit from s1[:i-1] & s2[:j], delete curr s1 char
                op3 = dp[i-1][j] + ord(s1[i-1])
                
                dp[i][j] = min(op1, min(op2, op3))
                
        return dp[-1][-1]
    
s1, s2 = "sea", "eat"
s1, s2 = "delete", "leet"

Solution().minimumDeleteSum(s1, s2)