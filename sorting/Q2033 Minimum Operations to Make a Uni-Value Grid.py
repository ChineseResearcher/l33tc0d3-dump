# sorting - medium
class Solution:
    def minOperations(self, grid, x):

        m, n = len(grid), len(grid[0])
        # flatten the array and sort the values
        arr = []
        for r in range(m):
            for c in range(n):
                arr.append(grid[r][c])
        arr.sort()

        def calc_ops(arr, benchmark_idx, x):

            # calculate the number of ops required to make
            # uni-value arr. if arr[benchmark_idx] is used
            bm = arr[benchmark_idx]
            ops = 0
            for num in arr:

                if abs(num - bm) % x != 0:
                    return -1
                
                ops += abs(num - bm) // x

            return ops

        return calc_ops(arr, len(arr) // 2, x)
    
grid, x = [[2,4],[6,8]], 2
grid, x = [[1,5],[2,3]], 1
grid, x = [[1,2],[3,4]], 2

Solution().minOperations(grid, x)