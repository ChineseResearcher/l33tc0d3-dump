# sliding window - hard
import heapq
class Solution:
    def countNonDecreasingSubarrays(self, nums: list[int], k: int) -> int:

        n = len(nums)
        fmin = lambda a, b: a if a < b else b
        # key ideas:
        # 1) every newly added window element x contributes max(window) - x to the
        # window operations, and this can be accessed via maxheap (sliding window maximum)

        # 2) when window operations exceeds k, we need to shrink left end, and we need
        # to discount operations associated with all monotonically increasing
        # heights within [l + 1, r - 1], and thus we require a pre-computed next greater array

        # 3) once the proper window is attained, every subarray ending at the right end
        # of the window is a valid answer

        # monotonic stack to pre-compute next greater / equal
        ge, st = [n] * n, []
        for i in range(n):
            while st and nums[i] >= nums[st[-1]]:
                ge[st.pop()] = i
            st.append(i)

        maxh, ans, l, c = [], 0, 0, 0
        for r in range(n):

            # lazy-del expired heights
            while maxh and maxh[0][1] < l:
                heapq.heappop(maxh)

            # add cost due to new element
            heapq.heappush(maxh, (-nums[r], r))
            c += abs(maxh[0][0]) - nums[r]

            # shrink window when window cost > k
            while c > k:
                p, p_end, bh = l + 1, fmin(ge[l], r + 1), nums[l]
                # by removing nums[l], we potentially reduce window cost
                while p < p_end:
                    np = fmin(ge[p], r + 1)
                    c -= (np - p) * (bh - nums[p])
                    p = np
                l += 1

            ans += (r - l + 1)

        return ans

nums, k = [6,3,1,3,6], 4
nums, k = [6,3,1,2,4,4], 7
nums, k = [25,2,1,24,15], 4

Solution().countNonDecreasingSubarrays(nums, k)