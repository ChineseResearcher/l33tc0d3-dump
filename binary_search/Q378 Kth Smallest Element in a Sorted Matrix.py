# binary search - medium
class Solution:
    def kthSmallest(self, matrix, k):
        # we could binary search on the range on the possible values
        # and test in O(n^2) time for a value if its the k-th smallest
        def cntSmallerEqual(target, matrix):
            
            # track the cnt of numbers = target, and <= target
            target_cnt, SoE_cnt = 0, 0
            
            for r in range(len(matrix)):
                # early stop: if the min. of curr. row already exceeds target
                if matrix[r][0] > target:
                    break

                for c in range(len(matrix[0])):
                    
                    if matrix[r][c] == target:
                        target_cnt += 1
                        
                    if matrix[r][c] <= target:
                        SoE_cnt += 1
                        
            return target_cnt, SoE_cnt

        # by observation, our range is bounded by [matrix[0][0], matrix[-1][-1]]
        l, r = matrix[0][0], matrix[-1][-1]

        while l <= r:
            
            target = (l + r) // 2
            target_cnt, SoE_cnt = cntSmallerEqual(target, matrix)
            # handle non-existing element
            if target_cnt == 0:
                if SoE_cnt >= k:
                    r = target - 1
                else:
                    l = target + 1
                continue
            
            # found answer
            if SoE_cnt - target_cnt + 1 <= k <= SoE_cnt:
                return target
            
            # target too small
            elif SoE_cnt < k:
                l = target + 1
            # target too big
            elif SoE_cnt - target_cnt + 1 > k:
                r = target - 1

matrix, k = [[1,5,9],[10,11,13],[12,13,15]], 8
matrix, k = [[-5]], 1

Solution().kthSmallest(matrix, k)