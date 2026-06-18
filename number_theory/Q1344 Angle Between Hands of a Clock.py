# number theory - medium
class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        
        # key ideas:
        # 1) map both hour and minute hand positions to be based in floats
        # in range [0, 12) and [1, 13) respectively
        # 2) calculate the angle by mapping the smaller diff. to 360 degress

        h = hour + minutes / 60
        m = minutes / 5

        diff = abs(h-m)
        return min(diff, 12-diff) / 12 * 360
    
hour, minutes = 12, 30
hour, minutes = 3, 30
hour, minutes = 3, 15
hour, minutes = 1, 59

Solution().angleClock(hour, minutes)