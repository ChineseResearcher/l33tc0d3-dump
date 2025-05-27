# simulation - medium
from typing import List
class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:

        # define event type 0 as "OFFLINE", event type 1 as "MESSAGE"
        events = [[1 if x[0] == "MESSAGE" else 0, int(x[1]), x[2]] for x in events]

        # sort by timestamps, followed by event order
        events.sort(key = lambda x: (x[1], x[0]))

        # maintain a dict storing the timestamps up to which each user is offline
        olt = {i:0 for i in range(numberOfUsers)}

        ans, all_cnt = [0] * numberOfUsers, 0
        for type, ts, info in events:

            if type == 0:

                u = int(info)
                olt[u] = ts + 60

            elif type == 1:

                if info == "ALL":
                    all_cnt += 1

                elif info == "HERE":
                    for u in range(numberOfUsers):

                        if ts >= olt[u]:
                            ans[u] += 1

                # mention by specific users
                else:
                    # parse mention string
                    l = [s.lstrip("id") for s in info.split(" ")]
                    for u in l:
                        ans[int(u)] += 1


        # process "ALL" mentions
        for u in range(numberOfUsers):
            ans[u] += all_cnt

        return ans
    
numberOfUsers = 2
events = [["MESSAGE","10","id1 id0"],["OFFLINE","10","0"],["MESSAGE","12","ALL"]]

numberOfUsers = 2
events = [["MESSAGE","10","id1 id0"],["OFFLINE","11","0"],["MESSAGE","71","HERE"]]

numberOfUsers = 2
events = [["OFFLINE","10","0"],["MESSAGE","12","HERE"]]

numberOfUsers = 3
events = [["MESSAGE","5","HERE"],["OFFLINE","10","0"],["MESSAGE","15","HERE"],["OFFLINE","18","2"],["MESSAGE","20","HERE"]]

Solution().countMentions(numberOfUsers, events)