# heap - hard
import heapq
class Solution:
    def findMaximizedCapital(self, k, w, profits, capital):
        # notice that the arr capital only means that in order to kickstart
        # project i, one has to hold at least capital[i] amount of capital
        # and that the capital required would not be consumed

        # sort both profits and capital according to least capital required
        profits, capital = map(list, zip(*sorted(zip(profits, capital), key = lambda x: x[1])))

        # initiate a maxheap as we are always getting the next most profitable project to work on
        maxheap = []

        # initiate a pointer j to keep track of distinct projects considered
        j = 0 
        while k > 0:
            
            while j < len(capital) and w >= capital[j]:
                heapq.heappush(maxheap, -profits[j])
                j += 1

            # if no project(s) available, means we've reached a dead end
            if not maxheap:
                return w
            
            # increment our capital with the profit of the next best project
            w += -heapq.heappop(maxheap)
            
            # mark project done
            k -= 1

        return w
    
k, w, profits, capital = 2, 0, [1,2,3], [0,1,1]
k, w, profits, capital = 3, 0, [1,2,3], [0,1,2]

Solution().findMaximizedCapital(k, w, profits, capital)