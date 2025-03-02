# two pointers - easy
class Solution:
    def mergeArrays(self, nums1, nums2):
        # O(n) time, O(1) space

        # track two pointers for nums1/nums2 arr.
        p1, p2 = 0, 0

        ans = []
        while True:

            # we are guaranteed that all ids in either nums1 or nums2 are unique
            # and that the ids appear in ascending order
            n1_id, n2_id = nums1[p1][0], nums2[p2][0]

            # process the nums arr with smaller id first
            if n1_id == n2_id:
                ans.append([n1_id, nums1[p1][1] + nums2[p2][1]])
                # both pointers incremented
                p1 += 1
                p2 += 1

            elif n1_id < n2_id:
                ans.append([n1_id, nums1[p1][1]])
                p1 += 1

            elif n2_id < n1_id:
                ans.append([n2_id, nums2[p2][1]])
                p2 += 1

            if p1 == len(nums1) or p2 == len(nums2):
                break

        # collect any leftover ids
        for i in range(p1, len(nums1)):
            ans.append(nums1[i])

        for j in range(p2, len(nums2)):
            ans.append(nums2[j])

        return ans
    
nums1, nums2 = [[1,2],[2,3],[4,5]], [[1,4],[3,2],[4,1]]
nums1, nums2 = [[2,4],[3,6],[5,5]], [[1,3],[4,3]]

Solution().mergeArrays(nums1, nums2)