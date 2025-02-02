# greedy - medium
class Solution:
    def mergeTriplets(self, triplets, target) -> bool:
        candidate = [0, 0, 0]
        # greedily replace our candidate if any of the three values exceed target's
        for tpl in triplets:

            skip = False
            for idx, val in enumerate(tpl):
                if val > target[idx]:
                    skip = True
                    break

            if skip: continue
            
            for idx, val in enumerate(candidate):
                candidate[idx] = max(candidate[idx], tpl[idx])

            if candidate == target:
                return True

        return False
    
triplets, target = [[2,5,3],[1,8,4],[1,7,5]], [2,7,5]
triplets, target = [[3,4,5],[4,5,6]], [3,2,5]
triplets, target = [[2,5,3],[2,3,4],[1,2,5],[5,2,3]], [5,5,5]

Solution().mergeTriplets(triplets, target)