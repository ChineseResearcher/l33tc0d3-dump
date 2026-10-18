# number theory - hard
import math
MOD = int(1e9 + 7)
class Solution:
    def numOfWays(self, nums: list[int]) -> int:
        
        n = len(nums)
        fmax = lambda a, b: a if a > b else b
        # key ideas:
        # 1) combinatorics + recursion
        # 2) first build the correct BST using nums, and record the left / right nodes
        # of every (distinct) node, using two arrays
        # 3) for counting of permutations, notice that for any subtrees, the answer is
        # equivalent to counting the valid arrangements of the combined results from 
        # left / right children, taking into account of the node counts of child subtrees
        root = nums[0]
        L, R = [None] * (n + 1), [None] * (n + 1)
        for i in range(1, n):

            x = nums[i]
            curr = root
            while L[curr] or R[curr]:
                nxt = curr
                if L[curr] and x < curr:
                    nxt = L[curr]
                if R[curr] and x > curr:
                    nxt = R[curr]
                if nxt == curr:
                    break
                curr = nxt
            # assign it as a new left node
            if x < curr:
                L[curr] = x
            else:
                R[curr] = x

        def f(curr: int) -> tuple[int, int]:

            if not L[curr] and not R[curr]:
                return (1, 1)

            L_res, L_cnt = 1, 0
            if L[curr]:
                L_res, L_cnt = f(L[curr])

            R_res, R_cnt = 1, 0
            if R[curr]:
                R_res, R_cnt = f(R[curr])

            t_cnt = L_cnt + R_cnt
            # suppose left & right subtree have count of nodes (a, b), and let t = a + b
            # 1) we first permute the seq. by picking "a" (or "b") spots out of t spots -> tCa
            # 2) then multiply the result above by count of permuatations at left & right subtrees
            # (i.e. we denote them as L_res and R_res) 
            res = math.comb(t_cnt, fmax(L_cnt, R_cnt)) * L_res * R_res
            cnt = t_cnt + 1
            return (res % MOD, cnt % MOD)

        ans, _ = f(root)
        return (ans - 1) % MOD

nums = [2,1,3]
nums = [1,2,3]
nums = [3,4,5,1,2]

Solution().numOfWays(nums)