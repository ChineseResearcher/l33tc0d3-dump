# segment tree - hard
from collections import defaultdict
from typing import List
class SegmentTree:
    def __init__(self, xs):
        self.xs = xs
        self.n = len(xs) - 1
        self.count = [0] * (4 * self.n)
        self.length = [0.0] * (4 * self.n)

    def _update_node(self, v, tl, tr):
        if self.count[v] > 0:
            # If this segment is covered by at least one rectangle
            # Then just return the length of this segment
            self.length[v] = self.xs[tr + 1] - self.xs[tl]
        elif tl != tr:
            # Otherwise, it's the sum of its children
            self.length[v] = self.length[2 * v] + self.length[2 * v + 1]
        else:
            # Leaf node with count == 0
            self.length[v] = 0

    def update(self, v, tl, tr, l, r, add):
        if l > r:
            return
        if l == tl and r == tr:
            self.count[v] += add
        else:
            tm = (tl + tr) // 2
            self.update(2 * v, tl, tm, l, min(r, tm), add)
            self.update(2 * v + 1, tm + 1, tr, max(l, tm + 1), r, add)
        self._update_node(v, tl, tr)

class Solution:
    def separateSquares(self, squares: list[list[int]]) -> float:
        # 1. Coordinate Compression for X
        x_coords = set()
        events = []
        for x, y, l in squares:
            x_coords.add(x)
            x_coords.add(x + l)
            # Event format: (y_coordinate, type, x_start, x_end)
            events.append((y, 1, x, x + l))
            events.append((y + l, -1, x, x + l))
        
        sorted_xs = sorted(list(x_coords))
        x_map = {val: i for i, val in enumerate(sorted_xs)}
        # Sort by y-coordinate
        events.sort() 

        st = SegmentTree(sorted_xs)
        
        # 2. First Pass: Calculate Total Union Area
        total_area = 0.0
        prev_y = events[0][0]
        
        # note: st.update(1, ...) means we are updating the root node
        # which corresponds to the global snapshot of full x-range
        for y, type, x1, x2 in events:
            # Add area of the strip between prev_y and current y
            total_area += st.length[1] * (y - prev_y)
            st.update(1, 0, st.n - 1, x_map[x1], x_map[x2] - 1, type)
            prev_y = y
            
        # 3. Second Pass: Find the y-level that bisects the area
        half_area = total_area / 2.0
        acc_area = 0.0
        
        # Reset Segment Tree for the second sweep
        st = SegmentTree(sorted_xs)
        prev_y = events[0][0]
        
        ans = -1
        for y, type, x1, x2 in events:
            strip_height = y - prev_y
            # get the corresponding combined x-width of the curr. y-event
            # by querying range stored information at the root node (1)
            current_union_width = st.length[1]
            strip_area = current_union_width * strip_height
            
            if acc_area + strip_area >= half_area:
                # The line lies within this strip
                ans = prev_y + (half_area - acc_area) / current_union_width
                break
            
            acc_area += strip_area
            st.update(1, 0, st.n - 1, x_map[x1], x_map[x2] - 1, type)
            prev_y = y
            
        return ans

squares = [[0,0,1],[2,2,1]]
squares = [[0,0,2],[1,1,1]]

Solution().separateSquares(squares)