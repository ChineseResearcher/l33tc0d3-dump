# bit manipulation - hard
from typing import List
class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        
        n = len(nums)
        # for trees:
        # 1) it is fully connected
        # 2) the path between any pair of nodes is unique

        # to flip a pair (a,b) that is not directly connected (e.g. a -> d -> e -> b)
        # it is important to realise that if we are to pass the
        # flipping commands down the path, nodes in between (i.e. d & e) would
        # not be flipped eventually

        # therefore, by greedy thinking, we would process all the nodes
        # which would benefit from flipping
        delta = sorted([(num ^ k) - num for num in nums])

        # flip all +ve delta pairs, for the only one unpaired
        # +ve delta node, pair it w/ the node w/ least negative delta
        net_improve = 0
        while delta and delta[-1] > 0:
            d = delta.pop()
            net_improve += d
            
        if (n - len(delta)) % 2 != 0:
            if not delta:
                net_improve -= d # backtrack
            else:
                # it could be 0 or -ve delta node
                if d + delta[-1] > 0:
                    net_improve += delta.pop()
                else:
                    net_improve -= d # backtrack
            
        return sum(nums) + net_improve
    
nums, k, edges = [1,2,1], 3, [[0,1],[0,2]]
nums, k, edges = [2,3], 7, [[0,1]]
nums, k, edges = [7,7,7,7,7,7], 3, [[0,1],[0,2],[0,3],[0,4],[0,5]]
nums, k, edges = [24,78,1,97,44], 6, [[0,2],[1,2],[4,2],[3,4]]
nums, k, edges = [67,13,79,13,75,11,0,41,94], 7, [[0,1],[3,7],[4,7],[6,5],[6,0],[0,2],[7,2],[7,8]]
nums, k, edges = [49,67,81,34,32], 6, [[1,0],[4,0],[4,2],[3,4]]

Solution().maximumValueSum(nums, k, edges)