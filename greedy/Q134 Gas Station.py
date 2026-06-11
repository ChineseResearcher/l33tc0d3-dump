# greedy - medium
from typing import List
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        n = len(gas)
        # key ideas:
        # 1) suppose we have computed net petrol gains for each station

        # 2) if the sum of net gains is smaller than 0, we are guaranteed
        # that is no solution for the problem, why?
        # we prove by contradiction, suppose there is some starting station "i"
        # where the circular route [i -> ... -> n-1 -> 0 -> ... -> i] is valid, but because
        # sum(net) < 0, we know that petrol left at station "i-1" < 0, making it
        # impossible to complete the trip by returning to station "i", directly
        # violating the validity of the route

        # 3) if sum(net) >= 0, then there exists a solution, we just have to locate
        # where that starting station should be

        # 4) to locate the valid starting station, imagine sum(net) >= 0 is satisfied
        # and that by summing our net arrays, we have such a pattern
        # [i1,...,j1, i2,...,j2, i3,...,j3, k....,n-1]
        # where each contiguous (i,j) interval represents a trip starting at "i" and seeing
        # cumulative petrol falling below 0 at "j", and we have no falling-below-0
        # for range [k, n-1], then station k is our valid starting station. Why?
        # The reason is that we have greedily discovered the very first station k
        # such that cumulative petrol does not fall below 0 for range [k,...,n-1]
        # and because sum(net) >= 0, the net decrements given by all prior (i,j) trips
        # will not exceed the sum of petrol from [k,...,n-1], ensuring the petrol
        # level for the trip [k -> ... -> n-1 -> 0 -> ... -> k] always stay non-negative,
        # thus validating the trip.

        net = [gas[i]-cost[i] for i in range(n)]
        if sum(net) < 0: return -1

        cumuSum, k = 0, 0
        for i in range(n):
            cumuSum += net[i]
            if cumuSum < 0:
                k = i + 1   # restart trip at i+1 station
                cumuSum = 0 # reset petrol

        return k

gas, cost = [2,3,4], [3,4,3]
gas, cost = [1,2,3,4,5], [3,4,5,1,2]
gas, cost = [5,1,2,3,4], [4,4,1,5,1]

Solution().canCompleteCircuit(gas, cost)