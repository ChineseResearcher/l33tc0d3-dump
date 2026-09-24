# dp - medium
from typing import List
class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        
        n = len(arr)
        fmax = lambda a, b: a if a > b else b
        # key ideas:
        # 1) construct 2-D dp nested dicts where dp[x][y] represents the length of 
        # longest fibonacci subsequence in the form [..., y, x-y, x]
        dp = {num: dict() for num in arr}

        ans = 0
        for i in range(2, n):   
            for j in range(i):
                # complement c is valid if c + arr[j] = arr[i]
                c = arr[i] - arr[j]

                # avoid searching on repeated pairs
                if arr[j] >= c:
                    break

                if c in dp:
                    # recognise [c, arr[j], arr[i]] as the length-3 fib subseq.
                    dp[arr[i]][c] = 3

                    # explore longer fib subseq. formations
                    if arr[i] - c in dp[c]:
                        dp[arr[i]][c] = fmax(dp[arr[i]][c], dp[c][arr[i] - c] + 1)
                        
                    # track longest subseq.
                    ans = fmax(ans, dp[arr[i]][c]) 

        return ans
    
arr = [1,2,3,4,5,6,7,8]
arr = [1,3,7,11,12,14,18]
arr = [2,5,6,7,8,10,12,17,24,41,65]
arr = [2,4,7,8,9,10,14,15,18,23,32,50]

Solution().lenLongestFibSubseq(arr)