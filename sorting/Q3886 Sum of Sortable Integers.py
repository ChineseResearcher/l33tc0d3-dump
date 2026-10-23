# sorting - hard
class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:

        n = len(nums)
        # key ideas:
        # 1) for any integer n, the count of divisors is bounded by sqrt(n)
        # 2) we can enumerate all possible divisors of the given n, and perform
        # a O(n) check to validate if nums is sortable by that divisor
        # 3) notice for any (sub)array, if we can cyclically rotate the array
        # s.t. it becomes non-decreasing at some point, then it will have maximally
        # 1 instance where arr[i] < arr[i - 1]

        def fac(n: int) -> list[int]:
            res = []
            for k in range(1, int(n ** 0.5) + 1):
                if n % k == 0:
                    res.append(k)
                    if k != n // k:
                        res.append(n // k)
            return res

        def canSort(arr: list[int]) -> bool:
            m, cnt = len(arr), 0
            if m > 1 and arr[0] < arr[-1]:
                cnt += 1
            for i in range(1, m):
                if arr[i] < arr[i - 1]:
                    cnt += 1
                if cnt > 1:
                    return False
            return True

        # get a sorted copy of the original nums
        snums = sorted(nums)

        ans = 0
        for k in fac(n):
            sortable = True
            for i in range(0, n, k):
                subarr = nums[i:i + k]
                # check (1): subarray should respect the bounds in sorted nums
                if max(subarr) != snums[i + k - 1] or min(subarr) != snums[i]:
                    sortable = False
                    break
                # check (2): subarray can be sorted to be non-desc via cyclic shifting
                if not canSort(subarr):
                    sortable = False
                    break
            if sortable:
                ans += k

        return ans

nums = [5,8]
nums = [7,6,5]
nums = [3,1,2]
nums = [12,18,14]

Solution().sortableIntegers(nums)