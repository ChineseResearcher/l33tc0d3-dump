# binary search - hard
from typing import List
class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:

        ref_pos, ref_neg = [], []
        for x in nums1:
            if x >= 0:
                ref_pos.append(x)
            else:
                ref_neg.append(x)

        tar_pos, tar_neg = [], []
        for x in nums2:
            if x >= 0:
                tar_pos.append(x)
            else:
                tar_neg.append(x)

        def cntSmaller(cap:int) -> int:

            cnt = 0
            ## refArr (+ve) w/ targetArr (+ve) ##
            n, m = len(ref_pos), len(tar_pos)
            j = m-1 # R -> L
            for i in range(n):

                if not tar_pos:
                    break
                
                while j > 0 and ref_pos[i] * tar_pos[j] > cap:
                    j -= 1

                cnt += j+1
                if ref_pos[i] * tar_pos[j] > cap:
                    cnt -= 1

            ## refArr (+ve) w/ targetArr (-ve) ##
            n, m = len(ref_pos), len(tar_neg)
            j = 0 # L -> R
            for i in range(n):

                if not tar_neg:
                    break

                j_ = j
                while j_ < m and ref_pos[i] * tar_neg[j_] <= cap:
                    j_ += 1

                j = j_ - 1 if j_ > j else j_

                cnt += j + 1
                if ref_pos[i] * tar_neg[j] > cap:
                    cnt -= 1

            ## refArr (-ve) w/ targetArr (+ve) ##
            n, m = len(ref_neg), len(tar_pos)
            j = 0 # L -> R
            for i in range(n):

                if not tar_pos:
                    break

                while j < m-1 and ref_neg[i] * tar_pos[j] > cap:
                    j += 1

                cnt += m-j
                if ref_neg[i] * tar_pos[j] > cap:
                    cnt -= 1

            ## refArr (-ve) w/ targetArr (-ve) ##
            n, m = len(ref_neg), len(tar_neg)
            j = m-1 # R -> L
            for i in range(n):

                if not tar_neg:
                    break

                j_ = j
                while j_ >= 0 and ref_neg[i] * tar_neg[j_] <= cap:
                    j_ -= 1

                j = j_ + 1 if j_ < j else j_

                cnt += m-j
                if ref_neg[i] * tar_neg[j] > cap:
                    cnt -= 1

            return cnt

        max1, max2 = max(nums1), max(nums2)
        min1, min2 = min(nums1), min(nums2)

        # to determine the proper left/right bound
        if min1 > 0 and min2 > 0:
            l = min1 * min2
        else:
            l = min(min1 * max2, min2 * max1)
            l = min(l, max1 * max2)

        if min1 < 0 and min2 < 0:
            r = max(min1 * min2, max1 * max2)
        else:
            r = max(min1 * max2, min2 * max1)
            r = max(r, max1 * max2)
        
        while l <= r:

            mid = (l + r) // 2

            # it suffices to search in either num1 or nums2
            # as nums1[i] * nums2[j] should not be double-counted
            cap_cnt = cntSmaller(mid)

            if cap_cnt >= k:
                r = mid - 1
            elif cap_cnt < k:
                l = mid + 1
            
        return l
    
nums1, nums2, k = [2,5], [3,4], 2
nums1, nums2, k = [-4,-2,0,3], [2,4], 6
nums1, nums2, k = [-2,-1,0,1,2], [-3,-1,2,4,5], 3

Solution().kthSmallestProduct(nums1, nums2, k)