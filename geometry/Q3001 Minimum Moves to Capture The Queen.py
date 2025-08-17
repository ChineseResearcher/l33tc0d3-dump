# geometry - medium
class Solution:
    def minMovesToCaptureTheQueen(self, a: int, b: int, c: int, d: int, e: int, f: int) -> int:
        
        ## check if we can achieve one move ##
        # case 1) 
        # queen is on diagonal path of white bishop w/ no obstruction
        if abs(c - e) == abs(d - f):
            x_delta = (e-c) // abs(e-c)
            y_delta = (f-d) // abs(f-d)

            # form the path from bishop to queen
            cx, cy = c, d
            while (cx, cy) != (a, b):
                
                if (cx, cy) == (e, f):
                    return 1

                cx += x_delta
                cy += y_delta

        # case 2)
        # queen is on the same row or col as white rook w/ no obstruction
        if a == e:
            y_delta = (f-b) // abs(f-b)

            # form the colwise path from rook to queen
            cx, cy = a, b
            while (cx, cy) != (c, d):

                if (cx, cy) == (e, f):
                    return 1
                
                cy += y_delta

        if b == f:
            x_delta = (e-a) // abs(e-a)

            # form the rowwise path rook to queen
            cx, cy = a, b
            while (cx, cy) != (c, d):

                if (cx, cy) == (e, f):
                    return 1
                
                cx += x_delta

        # otherwise, we can always achieve capture in 2 moves 
        return 2
    
a, b, c, d, e, f = 1, 1, 8, 8, 2, 3
a, b, c, d, e, f = 5, 3, 3, 4, 5, 2
a, b, c, d, e, f = 1, 1, 1, 2, 1, 3

Solution().minMovesToCaptureTheQueen(a, b, c, d, e, f)