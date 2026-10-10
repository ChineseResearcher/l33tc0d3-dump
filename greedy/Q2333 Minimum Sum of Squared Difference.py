# greedy - medium
class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:

        K = k1 + k2
        n = len(nums1)
        fmin = lambda a, b: a if a < b else b
        # key ideas:
        # 1) sorting + greedy assignment of modifications
        # 2) final min. Sum of Squared Difference (ssd) can be computed from modified diff array

        diff, t = [], 0
        for i in range(n):
            d = abs(nums1[i] - nums2[i])
            if d > 0:
                diff.append(d)
                t += pow(d, 2)

        if K >= t: return 0
        diff.append(0) # dummy 0
        diff.sort(reverse=True)

        # we will need a greedy process to reduce our diff array
        # e.g. for diff = [10, 9, 5, 4, 3]
        # we will try to reduce diff[0...0] to diff[1], costing (10 - 9) * 1 mods
        # then we try to reduce diff[0...1] to diff[2], costing (9 - 5) * 2 mods
        # repeat the process until we reach the final diff, which is our dummy 0
        k = K

        ndiff = None
        for i in range(1, len(diff)):
            cost = i * (diff[i - 1] - diff[i])
            nk = k - fmin(k, cost)
            if nk == 0:
                shortfall = cost - k
                a, b = shortfall // i, shortfall % i
                ndiff = [diff[i] + a] * i + diff[i:]
                if b > 0:
                    for j in range(b):
                        ndiff[j] += 1
                break
            # update k
            k = nk

        if ndiff is None: return 0
        ssd = 0
        for x in ndiff:
            ssd += pow(x, 2)
                
        return ssd

nums1, nums2, k1, k2 = [1,2,3], [1,2,3], 1, 1
nums1, nums2, k1, k2 = [1,4,10,12], [5,8,6,9], 1, 1
nums1, nums2, k1, k2 = [1,2,3,4], [2,10,20,19], 0, 0
nums1, nums2, k1, k2 = [10,10,10,11,5], [1,0,6,6,1], 11, 27

Solution().minSumSquareDiff(nums1, nums2, k1, k2)