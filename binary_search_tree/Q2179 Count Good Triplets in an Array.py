from sortedcontainers import SortedList
class Solution:
    def goodTriplets(self, nums1, nums2) -> int:

        # our nums1, nums2 arrs. are both of length n
        # and both contain numbers going from 0 to n-1
        n = len(nums1)

        # to locate a good triplet (x, y, z) where x, y, z
        # are in the same relative increasing order in both arrs.
        # we can focus on the middle number y, and transform this question into:
        # for every possible 0 <= y <= n-1, what are the numbers
        # in COMMON to the left/right in both arrs.?

        # record the indices (i.e pos) of a number y in nums2
        pos = [0] * n
        for idx, num in enumerate(nums2):
            pos[num] = idx
            
        # first part: find common count of numbers to left

        # Note:
        # pre_y[i] stores the count of common numbers to the left of nums1[i]
        # in both nums1 and nums2, and inserted stores the indices (in nums2)
        # of the scanned nums1 elements
        pre_y, inserted = [0], SortedList([pos[nums1[0]]])
        for i in range(1, n):
            
            # get the index of nums1[i] in nums2
            searchIdx = pos[nums1[i]]
            # search the insert pos. of this index in the SortedList in O(logN) time
            j = inserted.bisect_left(searchIdx)
            
            pre_y.append(min(i, j))
            # insert the searchIdx
            inserted.add(searchIdx)
            
        # second part: find common count of numbers to right
        post_y, inserted = [0], SortedList([pos[nums1[-1]]])
        for i in range(n-2, -1, -1):
            
            searchIdx = pos[nums1[i]]
            j = inserted.bisect_left(searchIdx)
            
            post_y.append(min(n-i-1, len(inserted) - j))
            inserted.add(searchIdx)
            
        post_y = post_y[::-1]

        ans = 0
        # our answer can be tabulated as pre_y[i] * post_y[i] for all i
        for i in range(n):
            ans += pre_y[i] * post_y[i]
            
        return ans
    
nums1, nums2 = [2,0,1,3], [0,1,2,3]
nums1, nums2 = [4,0,1,3,2], [4,1,0,2,3]

Solution().goodTriplets(nums1, nums2)