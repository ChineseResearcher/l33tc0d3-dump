# dp - medium
class Solution:
    def lenLongestFibSubseq(self, arr):
        n = len(arr)
        # we are guaranteed a monotonically increasing arr.
        # and thus every number is also unique

        # construct a dict to store the first previous fib num
        dp = {num: dict() for num in arr}
        # num_idx = {num: idx for idx, num in enumerate(arr)}

        ans = 0
        # question specifies a fib seq. must be at least of length 3
        for i in range(2, n):
            
            for j in range(i):

                # query if the complement number is present s.t.:
                # nums[j] + complement = nums[i], i.e. a fib seq
                complement = arr[i] - arr[j]

                # searching arr[j] is equivalent to searching its complement
                if arr[j] >= complement:
                    break

                if complement in dp:
                    
                    # it is now at least length 3 fib seq
                    dp[arr[i]][complement] = 3

                    # explore the last fib. number leading up to complement
                    # (ABSOLUTELY no idea why this loop is constant time...)
                    for prevFib, prevLength in dp[complement].items():
                        if prevFib + complement == arr[i]:
                            dp[arr[i]][complement] = max(dp[arr[i]][complement], prevLength + 1)

                    # update ans after searching
                    ans = max(ans, dp[arr[i]][complement]) 

        return ans
    
arr = [1,2,3,4,5,6,7,8]
arr = [1,3,7,11,12,14,18]
arr = [2,4,7,8,9,10,14,15,18,23,32,50]
arr = [2,5,6,7,8,10,12,17,24,41,65]

Solution().lenLongestFibSubseq(arr)