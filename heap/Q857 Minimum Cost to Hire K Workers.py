# heap - hard
import heapq
class Solution:
    def mincostToHireWorkers(self, quality, wage, k):
        n = len(quality)
        # one key realisation is that for a group of k workers, the total cost
        # of hiring depends on the worker with the highest w/q ratio
        # Note: higher w/q indicates lower worth as the cost is higher for a unit of quality

        # sort the w/q in ascending order
        ratio = sorted([(w / q, q) for w, q in zip(wage, quality)])

        # maintain a max heap ordered by quality
        max_heap = []
        quality_sum = 0
        max_ratio = 0.0

        # first build a group of size k and compute ans
        for i in range(k):
            max_ratio = max(max_ratio, ratio[i][0])
            quality_sum += ratio[i][1]
            heapq.heappush(max_heap, -ratio[i][1])

        # as mentioned above, the worker with max w/q ratio determines the total cost
        # and that the cost is computed as the ratio * sum of quality
        ans = max_ratio * quality_sum

        # then if we have more considerations available, we keep adding them
        # and popping worker with the higest quality from max_heap as the lower the 
        # total sum of quality, the lower the total cost
        for i in range(k, n):

            # as we iterate though w/q ratio in ascending order, the max ratio
            # is going to increase, which levels up the total cost
            max_ratio = max(max_ratio, ratio[i][0])

            # change in quality sum:
            # 1) decrement quality of worker popped from max heap
            # 2) increment quality of worker being considered by i
            quality_sum += -abs(heapq.heappop(max_heap)) + ratio[i][1]
            heapq.heappush(max_heap, -ratio[i][1])
            ans = min(ans, max_ratio * quality_sum)

        return ans
    
quality, wage, k = [3,1,10,10,1], [4,8,2,2,7], 3
quality, wage, k = [10,20,5], [70,50,30], 2
quality, wage, k = [5,5,5,1], [14,5,7,5], 3

Solution().mincostToHireWorkers(quality, wage, k)