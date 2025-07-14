# greedy - hard
class Solution:
    def minimumBoxes(self, n: int) -> int:

        # the sample testcases already illustrate the "greedy"
        # way of maximising the utility of every floored box (fb)
        # the thinking is to build a cornered pyramid as much as possible

        # incre = curr. side length of the floor rim of our cornered pyramid
        # from a top-down perspective, the floored boxes grow like
        #  - - - - - (wall)      - - - - - - - - 
        # | * * *               | * * * *
        # | * *              -> | * * *     
        # | *                   | * *
        # |                     | *
        # where our incre changes from 3 to 4

        # for a "perfect" cornered pyramid:
        # suppose our floor base = 1 + 2 + 3 + 4 = 10 boxes
        # then this could support (1 + 2 + 3) + (1 + 2) + (1) = 6 + 3 + 1 = 10 boxes above it

        k, incre, fb = 0, 1, 0
        while k < n:

            fb += incre
            k += (1 + incre) * incre // 2
            incre += 1

        if k == n:
            return fb

        # otherwise we are guaranteed k > n, which means
        # n boxes cannot be constructed as a perfect cornered pyramid
        incre -= 1
        fb -= incre
        k -= (1 + incre) * incre // 2

        # we then use the remaining (n-k) boxes available to optimally
        # build sub-pyramids as much as possible
        incre2 = 1
        while (1 + incre2) * incre2 // 2 < n - k:
            incre2 += 1

        return fb + incre2
    
n = 3
n = 4
n = 10
n = int(1e9) # constraint

Solution().minimumBoxes(n)