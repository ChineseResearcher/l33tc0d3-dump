# prefix sum - medium
class Solution:
    def splitPainting(self, segments):
        # query the length of painting as it is not given as an input
        range_start, range_end = set([x[0] for x in segments]), set([x[1] for x in segments])

        start_pos, end_pos = min(range_start), max(range_end)
        # let arr be starting from pos 1
        n = end_pos

        # similar to LC 2381 Shifting letters II, we rely on a diff. arr
        # to construct the range updates which is needed for prefix sum
        diff = [0] * (n+1)
        for l, r, v in segments:

            # increment/decrement at the left/right(exclusive) bound
            diff[l] += v
            diff[r] -= v

        pf_sum = 0
        color_sum = [0] * (n+1)
        for i in range(n+1):

            pf_sum += diff[i]
            color_sum[i] = pf_sum

        ans = []
        # our painting starts at idx 1
        l = 1
        for r in range(1, n+1):
            # second cond. checks for 3rd sample TC
            if color_sum[l] != color_sum[r] or \
            (color_sum[l] == color_sum[r] and r in range_start and r != start_pos):
                
                # our painting does not have to start from pos 1
                # since our color_sum arr. is starting from 1, we need to check if
                # the window we are collecting is indeed part of the painting
                # additionally, color_sum[l] = 0 is an invalid EC. 
                if l >= start_pos and color_sum[l] > 0:
                    ans.append([l, r, color_sum[l]])
                    
                # slide window
                l = r

        return ans
    
segments = [[1,4,5],[4,7,7],[1,7,9]]
segments = [[1,4,5],[1,7,7]]
segments = [[1,7,9],[6,8,15],[8,10,7]]
segments = [[1,4,5],[1,4,7],[4,7,1],[4,7,11]]
segments = [[4,5,9],[8,12,5],[4,7,19],[14,15,1],[3,10,8],[17,20,18],[7,19,14],[8,16,6],[14,17,7],[11,13,3]]

Solution().splitPainting(segments)