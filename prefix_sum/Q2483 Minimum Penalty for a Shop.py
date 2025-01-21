# prefix sum - medium
class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)
        # solution is such that we find some index j for 0 <= j < n
        # such that 'N' count up to j & 'Y' count at and after j is minimised

        pf_y_cnt, pf_n_cnt = [], []
        currY, currN = 0, 0

        for i in range(n):

            currY += 1 if customers[i] == 'Y' else 0
            pf_y_cnt.append(currY)

            currN += 1 if customers[i] == 'N' else 0
            pf_n_cnt.append(currN)

        minPenalty = float('inf')
        ans = -1

        # it is possible to close at the n-th hour too
        for j in range(n+1):

            # open but no customer
            penalty1 = pf_n_cnt[j-1] if j-1 >= 0 else 0
            # closed but have customer visiting
            if j == n:
                penalty2 = 0
            elif j < n:
                penalty2 = pf_y_cnt[n-1] - pf_y_cnt[j-1] if j-1 >= 0 else pf_y_cnt[n-1]

            currPenalty = penalty1 + penalty2
            if currPenalty < minPenalty:
                ans = j
                minPenalty = currPenalty

        return ans
    
customers = "YYNY"
customers = "NNNNN"
customers = "YYYY"

Solution().bestClosingTime(customers)
