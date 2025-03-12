# heap - hard
import heapq
class Solution:
    def getSkyline(self, buildings):
        
        n = len(buildings)
        # sort buildings based on heights
        buildings.sort(key=lambda x: (x[2], x[0], x[1]))

        # keep track of the prev. height being processed
        ph, temp = buildings[0][2], []

        # merge overlapping buildings of the same height
        idx, merged = 0, [] 
        while idx < n:

            ch, l, r = buildings[idx][2], buildings[idx][0], buildings[idx][1]
            if ch > ph:
                temp.extend(merged)
                # empty merged and start merging at a new height
                merged = []
                # override prev. height with curr. height
                ph = ch

            if not merged:
                merged.append([l, r, ch])
            else:
                # line sweep to detect merge-able buildings at same height
                if l <= merged[-1][1]:
                    merged[-1][1] = max(merged[-1][1], r)
                else:
                    merged.append([l, r, ch])
            
            # increment idx of buildings arr.
            idx += 1

        # collect any items in merged
        temp.extend(merged)
        # update buildings arr.
        buildings = temp

        # init. two arrs. storing left/right edges of buildings
        # with an additional indicator 1/-1
        le, re = [], []
        for i in range(len(buildings)):
            l_idx, r_idx, h = buildings[i]
            le.append([l_idx, h, -1, i])
            re.append([r_idx, h, 1, i])

        # sort edges first based on idx, then h * type of edge
        e = sorted(le+re, key=lambda x: (x[0], x[1] * x[2]))

        m, ans, idx = len(e), [], 0
        # maxHeap storing <-height, right_edge_idx>
        maxHeap = []
        while idx < m:

            currX = e[idx][0]
            while maxHeap and maxHeap[0][1] < currX:
                heapq.heappop(maxHeap)
            # record the max. height at this point
            max_h = abs(maxHeap[0][0]) if maxHeap else 0

            # init. max l/r edges' height
            max_le = e[idx][1] if e[idx][2] == -1 else 0
            max_re = e[idx][1] if e[idx][2] == 1 else 0
            if e[idx][2] == -1:
                heapq.heappush(maxHeap, [ -e[idx][1], buildings[e[idx][3]][1] ])

            # process all possible (l/r) edges at the same X pos
            while idx < m:
                
                # only heappush maxHeap for left edges
                if e[idx][2] == -1:
                    max_le = max(max_le, e[idx][1])
                    heapq.heappush(maxHeap, [ -e[idx][1], buildings[e[idx][3]][1] ])

                elif e[idx][2] == 1:
                    max_re = max(max_re, e[idx][1])

                if idx == m-1 or e[idx+1][0] != currX:
                    break

                idx += 1

            # increment idx to move on to the next X pos
            idx += 1

            # a big challenge for this question is: for any edge we process
            # we need to decide if it triggers topLeft/botRight update 
            # or it should be skipped entirely

            # rationale for marking a topLeft point is when we encounter
            # a left edge with height exceeding the max. height before left edges are processed
            if max_le > 0 and max_le > max_h:
                ans.append([currX, max_le])
                # if a topLeft point is added, then there surely would
                # not be any botRight point added for the same X pos
                continue
            
            # rationale for marking a botRight point is when our max. height
            # before processing any left edges is equivalent to the max. right edge height at currX
            if max_re > 0 and max_re == abs(maxHeap[0][0]):
                heapq.heappop(maxHeap)

                # the embedded challenge is to find the reference base height
                # that our botRight point should land on, init. to 0
                next_max_h = 0
                while maxHeap and maxHeap[0][1] <= currX:
                    heapq.heappop(maxHeap)
                # with merging of attached buildings at same heights
                # we would be able to obtain the next max. height (if any) efficiently
                if maxHeap: next_max_h = max(next_max_h, abs(maxHeap[0][0]))
                ans.append([currX, next_max_h])

        return ans
    
buildings = [[0,2,3],[2,5,3]]
buildings = [[2,3,3],[0,2,3],[2,5,3],[1,3,2],[3,4,4]]
buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
buildings = [[2,9,10],[9,12,15]]
buildings = [[1,2,1],[1,2,2],[1,2,3]]

Solution().getSkyline(buildings)
