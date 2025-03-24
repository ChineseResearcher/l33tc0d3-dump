# sorting - medium
class Solution:
    def countDays(self, days, meetings):
        n = len(meetings)
        # sort meetings & merge overlapped intervals
        meetings.sort()

        temp = [meetings[0]]
        for i in range(1, n):

            # extend right bound after merging
            if meetings[i][0] <= temp[-1][1]:
                temp[-1][1] = max(temp[-1][1], meetings[i][1])
            else:
                temp.append(meetings[i])

        # update meetings
        meetings = temp

        m = len(meetings)
        # init. ans by considering leftmost/rightmost available days
        ans = meetings[0][0] - 1 + max(days - meetings[-1][1], 0)
        for i in range(1, m):

            # for every non-overlap interval, we can calculate the
            # difference between prev. end and next start as the free days
            ans += meetings[i][0] - meetings[i-1][1] - 1

        return ans
    
days, meetings = 10, [[5,7],[1,3],[9,10]]
days, meetings = 5, [[2,4],[1,3]]
days, meetings = 6, [[1,6]]

Solution().countDays(days, meetings)