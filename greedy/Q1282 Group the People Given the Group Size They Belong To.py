# greedy - medium
from collections import defaultdict
class Solution:
    def groupThePeople(self, groupSizes):
        
        # similar to LC781 rabbits in forest, where greedy grouping is needed
        n = len(groupSizes)

        # maintain a dict of subscribed to keep track
        # of the ppl currently belonging to a grpSize of k
        subscribed = defaultdict(list)

        grouping = []
        for i in range(n):

            k = groupSizes[i]
            if len(subscribed[k]) == k:
                # move the fully formed group to answer
                grouping.append(subscribed[k])
                # reset
                subscribed[k] = [i]

            else:
                subscribed[k].append(i)

        # collect the leftover in subscribed
        for _, grp in subscribed.items():
            grouping.append(grp)

        return grouping
    
groupSizes = [3,3,3,3,3,1,3]
groupSizes = [2,1,3,3,3,2]

Solution().groupThePeople(groupSizes)