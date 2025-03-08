# greedy - medium
class Solution:
    def advantageCount(self, nums1, nums2):
        n = len(nums1)

        nums1.sort()
        nums2 = sorted([[val, idx] for idx, val in enumerate(nums2)])

        # attempt to locate the first index where nums1[i] > nums2[i]
        j = n
        for i in range(n):
            if nums1[i] > nums2[0][0]:
                j = i
                break

        ans = [None] * n
        # we assign the advantaged number from nums1 by greedily
        # choosing the smallest valid nums1[i] for every nums2[i]

        # idx for sorted nums1 & matched advantage idx in sorted nums2
        idx, adv_idx, usedIdx = j, 0, set()
        while True:

            # keep incrementing idx until next nums1[idx] has an advantage
            while idx < n and nums1[idx] <= nums2[adv_idx][0]:
                idx += 1

            if idx == n: break
            # otherwise we assign the advantaged number from nums1
            ans[nums2[adv_idx][1]] = nums1[idx]

            # mark idx as used
            usedIdx.add(idx)
            idx += 1

            # move to next number in nums2
            adv_idx += 1

        if adv_idx == n: return ans

        # for all nums2[j] which has no advantaged counterpart in nums1[i]
        # it is alright for us to assign the unused nums1[i] in any order
        for i in range(n):
            if i not in usedIdx:
                ans[nums2[adv_idx][1]] = nums1[i]
                adv_idx += 1

        return ans
    
nums1, nums2 = [12,24,8,32], [13,25,32,11]
nums1, nums2 = [8,12,24,32], [11,25,27,32]
nums1, nums2 = [8,10,24,32], [11,13,25,32]
nums1, nums2 = [2,7,11,15], [1,10,4,11]
nums1, nums2 = [15777,7355,6475,15448,18412], [986,13574,14234,18412,19893] 

Solution().advantageCount(nums1, nums2)