# sorting - medium
class Solution:
    def checkValidCuts(self, n, rectangles):
        
        # first parse the input into [start, end] format for x-/y-axis respectively
        rec_x, rec_y = [], []

        for x_start, y_start, x_end, y_end in rectangles:
            rec_x.append([x_start, x_end])
            rec_y.append([y_start, y_end])

        # sort both arrays
        rec_x.sort()
        rec_y.sort()

        # merge overlapped dimensions along x-/y-axis respectively
        temp_x, temp_y = [rec_x[0]], [rec_y[0]]

        for i in range(1, len(rec_x)):

            if rec_x[i][0] < temp_x[-1][1]:
                temp_x[-1][1] = max(rec_x[i][1], temp_x[-1][1])
            else:
                temp_x.append(rec_x[i])

        for j in range(1, len(rec_y)):

            if rec_y[j][0] < temp_y[-1][1]:
                temp_y[-1][1] = max(rec_y[j][1], temp_y[-1][1])
            else:
                temp_y.append(rec_y[j])

        # reassign
        rec_x, rec_y = temp_x, temp_y

        # we need to validate if we could make two horizontal
        # or vertical cuts without crossing overlapped regions
        cnt = 0
        for i in range(1, len(rec_x)):

            if rec_x[i][0] >= rec_x[i-1][1]:
                cnt += 1
            if cnt == 2: return True

        cnt = 0
        for j in range(1, len(rec_y)):

            if rec_y[j][0] >= rec_y[j-1][1]:
                cnt += 1
            if cnt == 2: return True

        return False

n, rectangles = 5, [[1,0,5,2],[0,2,2,4],[3,2,5,3],[0,4,4,5]]

Solution().checkValidCuts(n, rectangles)