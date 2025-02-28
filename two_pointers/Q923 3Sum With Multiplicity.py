# two pointer - medium
import math
class Solution:
    def threeSumMulti(self, arr, target):
        
        n = len(arr)
        # similar to three-sum, but there can be multiple occurrences
        # of the same answer, so we move pointer to account for those
        arr.sort()

        ans = 0
        # three-sum is about forming triplets
        for i in range(n-3+1):

            twoSumTarget = target - arr[i]
            l, r = i+1, n-1
            # print('testing twoSumTarget', twoSumTarget, "@", i)
            while True:

                if arr[l] + arr[r] == twoSumTarget:
                    # print('found twoSumTarget for', arr[l], arr[r])
                    lo, ro = 1, 1
                    
                    # account for multiplicity
                    while l+1 < r and arr[l+1] == arr[l]:
                        lo += 1
                        l += 1
                    
                    while r-1 > l and arr[r-1] == arr[r]:
                        ro += 1
                        r -= 1

                    # special case when arr[l] & arr[r] are the same number
                    if arr[l] == arr[r]:
                        ans += math.comb(lo+ro, 2) % (1e9 + 7)
                    else:
                        ans += (lo * ro) % (1e9 + 7)
                    
                    l += 1
                    r -= 1
                    # print('incrementing ans to', ans, 'l @', l, 'r @', r)

                elif arr[l] + arr[r] < twoSumTarget:
                    l += 1
                elif arr[l] + arr[r] > twoSumTarget:
                    r -= 1

                if l >= r: break
                
        return int(ans % (1e9 + 7))
    
arr, target = [1,1,2,2,3,3,4,4,5,5], 8
arr, target = [1,1,2,2,2,2], 5
arr, target = [2,1,3], 6

Solution().threeSumMulti(arr, target)