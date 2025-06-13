# greedy - hard
from typing import List
class Solution:
    def findMinMoves(self, machines: List[int]) -> int:
        n, unitSum = len(machines), sum(machines)
        # if sum of all units of dressings in machines cannot be divisible by n
        # then we say it is not possible to equally distribute dresses
        if unitSum % n != 0:
            return -1

        target = unitSum // n
        # build a diff arr. detailing the deficiency/sufficiency at every index
        diff = [x - target for x in machines]

        # build a leftwards / rightwards prefix sum
        # interpretation:
        # at index i, think of lpf[i-1] as the number of clothes needed
        # to fulfil on the left handside, similarly for rpf[i+1]
        rSum, lpf = 0, [0] * n
        for i in range(n):
            rSum += diff[i]
            lpf[i] = rSum

        rSum, rpf = 0, [0] * n
        for j in range(n-1, -1, -1):
            rSum += diff[j]
            rpf[j] = rSum

        # then we explore all indices to calculate max(left + right)
        # note that max(abs(left + right)) might exceed diff[i]
        # so this means while we are tracking the max. "donations" from a single machine[i]
        # it does not mean that every donation comes from the single machine itself
        # that machine could have received some clothes from another machine in the first place
        # and then make that donation, so a more accurate way to internalise is:
        # what is the max "outflow" ever needed for machine[i]?
        ans = 0
        for k in range(n):

            lmax = min(lpf[k-1], 0) if k > 0 else 0
            rmax = min(rpf[k+1], 0) if k < n-1 else 0

            ans = max(ans, abs(lmax) + abs(rmax))

        return ans
    
machines = [1,0,5]
machines = [0,3,0]
machines = [0,2,0]
machines = [4,0,0,4]
machines = [4,0,4,0]
machines = [0,0,11,5]

Solution().findMinMoves(machines)