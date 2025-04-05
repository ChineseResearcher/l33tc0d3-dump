# binary search - hard
class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        def valid(targetNum, k):
            # given a targetNum locked in by binary search
            # we test if there are at least k occurrences
            # of numbers in the multiplcation table smaller than it

            # because m * n goes up to ~ 10^9, 
            # this query function has to run efficiently

            # one nice observation is that for some target,
            # it is guaranteed to be larger than "target // n" numbers in the table
            smallerCnt = (targetNum // n) * n
            if smallerCnt >= k: 
                return True
            
            # we explore further rows to see if there are more numbers
            # in the table <= targetNum, using targetNum // (r+1)
            for r in range(targetNum // n, m):
                if targetNum < r+1: 
                    break

                smallerCnt += targetNum // (r+1)
                if smallerCnt >= k:
                    return True

            return False

        def isPresent(targetNum):
            # verify if targetNum can be found in table
            for r in range(m):
                if targetNum % (r+1) == 0 and targetNum // (r+1) <= n:
                    return True

            return False

        # perform binary search on the answer
        # overall complexity is O(M * Log(M*N))
        l, r = 1, m * n

        ans = r
        while l <= r:

            mid = (l + r) // 2
            if valid(mid, k):
                if isPresent(mid):
                    ans = min(ans, mid)

                r = mid - 1
            else:
                l = mid + 1

        return ans
    
m, n, k = 3, 3, 5
m, n, k = 2, 3, 6

Solution().findKthNumber(m, n, k)