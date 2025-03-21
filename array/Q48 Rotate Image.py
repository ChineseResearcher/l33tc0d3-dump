# array - medium
class Solution:
    def rotate(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        n = len(matrix)
        # a matrix needs to be rotated 90degs clockwise, and in-place
        # the challenge comes from modifying in-place, we have to 
        # derive an algorithm to swap the values correctly

        # maintain a set for already swapped positions
        completed = set()

        for r in range(n):
            for c in range(n):

                if (r, c) not in completed:

                    currVal = matrix[r][c]
                    currR, currC = r, c

                    iteration = 0
                    # if an image is rotated 4 times, it is equivalent
                    # to its original form, i.e. no rotation
                    while iteration < 4:

                        # mark visited
                        completed.add((currR, currC))

                        # algorithm to get next swap pos:
                        # currCol -> nextRow, n-1-currRow -> nextCol
                        nextR, nextC = currC, n-1-currR

                        # perform swapping
                        swapped = matrix[nextR][nextC]
                        matrix[nextR][nextC] = currVal

                        # update currVal. and currR, currC
                        currVal = swapped
                        currR, currC = nextR, nextC

                        iteration += 1

        # debug print
        for r in matrix:
            print(r)

matrix = [[1,2,3],[4,5,6],[7,8,9]]
matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]

Solution().rotate(matrix)