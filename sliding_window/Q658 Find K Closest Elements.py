# sliding window - medium
class Solution:
    def findClosestElements(self, arr, k, x):
        n = len(arr)
        # the arr given is already sorted, we make use of this
        # property by applying a fixed length sliding window
        window_diff_sum = sum([abs(y-x) for y in arr[:k]])
        best_sum = window_diff_sum
        best_l, best_r = 0, k-1

        for r in range(k, n):
            window_diff_sum += abs(arr[r] - x)
            window_diff_sum -= abs(arr[r-k] - x)

            if window_diff_sum < best_sum:
                best_l, best_r = r-k+1, r
                best_sum = window_diff_sum

        return arr[best_l:best_r + 1]
    
arr, k, x = [1,2,3,4,5], 4, 3
arr, k, x = [1,1,2,3,4,5], 4, -1

Solution().findClosestElements(arr, k, x)