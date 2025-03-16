# binary search - medium
class Solution:
    def canRepair(self, target, ranks, n):
        # given a targeted max. time allowed, check if we can
        # indeed repair n cars by utilising all mechanics available
        # Note: mechanics are able to work at the same time

        cnt = 0
        for rank in ranks:
            # since the formula to compute the time needed for a
            # mechanic with some rank r to repair m cars is r * m^2
            # we would allow it to repair floor(sqrt(target/r)) cars
            cnt += int((target/rank) ** 0.5)

        return True if cnt >= n else False

    def repairCars(self, ranks, cars):

        # init. the max. explorable target time based on max(ranks)
        l, r = 1, max(ranks) * cars**2
        ans = r

        while l <= r:

            mid = (l+r) // 2
            if self.canRepair(mid, ranks, cars):
                ans = min(ans, mid)
                r = mid - 1
            else:
                l = mid + 1

        return ans
    
ranks, cars = [4,2,3,1], 10
ranks, cars = [5,1,8], 6

Solution().repairCars(ranks, cars)