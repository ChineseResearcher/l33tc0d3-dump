# dp - hard
class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        
        def recursive_drop(egg, nf):

            # egg: number of eggs left
            # nf: number of floors involved

            # there's significance of egg = 1 being the terminal cond. 
            # when we have only 1 egg, we can't afford to test at different mid-points
            # and dfs down further to compare b/w op1 and op2
            # so in this case, we are essentially performing a linear scan
            if egg == 1:
                return nf
            
            if nf == 0:
                return 0
            
            if (egg, nf) in dp:
                return dp[(egg, nf)]
            
            # question asks for min. number of moves to be certain of "f"
            # this is asking for the mini-max, so we take max of options available
            mid = nf // 2

            # optimisation: because of the fact that the fall-and-break is monotonic
            # we can optmise using binary-search and mid-point

            curr_res = float('inf')
            l, r = 1, nf
            while l <= r:

                mid = (l + r) // 2
                # op1: egg breaks in the lower halve
                op1 = recursive_drop(egg-1, mid-1)

                # op2: egg did not break in the lower halve, so we need to test upper halve
                op2 = recursive_drop(egg, nf-mid)

                # note that we add 1 because we need 1 move to test @ mid-point
                # also note that we are minimising curr_res over the max of (op1, op2) -> mini-max
                if op1 > op2:
                    curr_res = min(curr_res, op1 + 1)
                    r = mid - 1
                elif op1 < op2:
                    curr_res = min(curr_res, op2 + 1)
                    l = mid + 1
                # if op1, op2 equal in costs, we have reached an optimum, stop
                else:
                    curr_res = min(curr_res, op1 + 1)
                    break

            dp[(egg, nf)] = curr_res
            return curr_res

        dp = dict()
        return recursive_drop(k, n)
    
k, n = 1, 2
k, n = 2, 6
k, n = 3, 14
k, n = 2, 2
k, n = 2, 4
k, n = 2, 9
k, n = 2, 10
# constraints
k, n = 100, int(1e4)

Solution().superEggDrop(k, n)