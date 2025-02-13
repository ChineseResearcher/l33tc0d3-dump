# binary search - medium
import bisect
class Solution:
    def can_reach_all_hse(self, radius):

        for x in self.houses:
            l = min(bisect.bisect_left(self.heaters, x), len(self.heaters) - 1)
            # if there's a heater potentially strictly to the left of where house x is
            # the l pointer should be decremented
            if l > 0 and x > self.heaters[l-1]: l -= 1

            r = min(l + 1, len(self.heaters) - 1)

            if abs(x-self.heaters[l]) > radius and abs(x-self.heaters[r]) > radius:
                return False
            
        return True

    def findRadius(self, houses, heaters):
        self.houses, self.heaters = houses, heaters
        # standard problem to binary search on the ans
        self.houses.sort()
        self.heaters.sort()

        ans = float('inf')

        rMin = 0
        rMax = max(heaters[-1]-heaters[0] \
                  ,max(abs(heaters[-1]-houses[0]), abs(houses[-1]-heaters[0])))

        while rMin <= rMax:

            mid = (rMin + rMax) // 2
            if self.can_reach_all_hse(mid):
                ans = min(ans, mid)
                rMax = mid - 1
            else:
                rMin = mid + 1

        return ans
    
houses, heaters = [1,2,3,4], [1,4]
houses, heaters = [1,5], [2]
houses, heaters = [1,5], [10]

Solution().findRadius(houses, heaters)