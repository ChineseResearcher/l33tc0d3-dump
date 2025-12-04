class Solution:
    def countCollisions(self, directions: str) -> int:

        # key ideas:
        # 1) we process collisions whenever we are at 'S' or 'L' directions
        # 2) for 'S', we would collide w/ all 'R's in the stack,
        #    for 'L', we would collide w/ prev. immediate 'S' or all 'R's in the stack

        ans, activeR, seenS = 0, 0, False
        for char in directions:
            
            if char == 'R':
                activeR += 1

            elif char == 'S':
                ans += activeR
                seenS = True
                activeR = 0 # reset

            elif char == 'L':
                if activeR > 0:
                    # two-way collision
                    ans += 2
                    # activeR reduce by 1 due to turning 'S'
                    activeR -= 1
                    ans += activeR
                    activeR = 0 # reset
                    seenS = True

                else:
                    if seenS:
                        ans += 1

        return ans

directions = "RLRSLL"
directions = "LLRR"

Solution().countCollisions(directions)