# two pointer - medium
import math
MOD = int(1e9 + 7)
class Solution:
    def threeSumMulti(self, arr: list[int], target: int) -> int:
        
        n = len(arr)
        # key ideas:
        # 1) similar to three-sum, but there can be multiple occurrences
        # of the same answer, so we move pointer to account for those
        arr.sort()

        ans = 0
        # three-sum is about forming triplets
        for i in range(n - 2):

            twoSumTarget = target - arr[i]
            l, r = i + 1, n - 1
            while l < r:

                if arr[l] + arr[r] == twoSumTarget:
                    lo, ro = 1, 1
                    
                    # account for multiplicity
                    while l + 1 < r and arr[l + 1] == arr[l]:
                        lo += 1
                        l += 1
                    
                    while r - 1 > l and arr[r - 1] == arr[r]:
                        ro += 1
                        r -= 1

                    # special case when arr[l] & arr[r] are the same number
                    if arr[l] == arr[r]:
                        ans += math.comb(lo + ro, 2) % MOD
                    else:
                        ans += (lo * ro) % MOD
                    
                    l += 1
                    r -= 1

                elif arr[l] + arr[r] < twoSumTarget:
                    l += 1
                    
                else:
                    r -= 1
                
        return ans % MOD

arr, target = [2,1,3], 6
arr, target = [1,1,2,2,2,2], 5
arr, target = [1,1,2,2,3,3,4,4,5,5], 8

Solution().threeSumMulti(arr, target)