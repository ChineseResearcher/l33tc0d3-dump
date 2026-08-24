# number theory - medium
from typing import List
class Solution:
    def kthPalindrome(self, queries: List[int], intLength: int) -> List[int]:

        # key ideas:
        # 1) compute the base length (i.e. the length of left or right mirror)
        # so as to determine the max k-th possible palindrome

        # 2) for each queries[i]-th palindrome, if queries[i] <= k, we construct
        # the left mirror by performing division by 10 starting from the most significant digit

        base_len = (intLength // 2) + (intLength % 2)
        base = pow(10, base_len - 1)

        # upper limit on querying
        maxK = 9 * base

        ans = []
        for q in queries:
            if q > maxK:
                ans.append(-1)
                continue

            # the q-th smallest is the (q-1)-th smallest above base
            res = base + q - 1

            # construct the final palindrome
            if intLength % 2 == 1:
                mid = res % 10
                left = res // 10
                if left > 0:
                    q_num = int(str(left) + str(mid) + str(left)[::-1])
                else:
                    q_num = int(str(mid))
            else:
                left = res
                q_num = int(str(left) + str(left)[::-1])

            ans.append(q_num)

        return ans

queries, intLength = [2,4,6], 4
queries, intLength = [1,2,3,4,5,90], 3

Solution().kthPalindrome(queries, intLength)