# greedy - medium
class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        
        n = num
        # key ideas:
        # 1) greedily assign min(remSum, 9) as the curr. digit
        # 2) if there is leftover sum after greedy assignments, no valid string possible
        if sum > n * 9:
            return ''

        ans = (sum // 9) * '9' + (str(sum % 9) if sum % 9 else '')
        if len(ans) < n:
            ans += (n - len(ans)) * '0'

        return ans

num, sum = 2, 3
num, sum = 1, 9
num, sum = 2, 17
num, sum = 1, 10

Solution().maxSumOfSquares(num, sum)