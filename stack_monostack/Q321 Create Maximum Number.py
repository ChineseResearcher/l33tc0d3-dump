# monotonic stack - hard
from typing import List
class Solution:
    # TC is O(k^3) where k is up to (m+n), i.e k = 1000
    # surprisingly this gets accepted as cubic runtime is usually efficient up to 100
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        # first sub-task is to figure out given just ONE arr,
        # how do we find the largest number of length k from the digits?
        def largestNum(digits, k):

            n = len(digits)
            # maintain a monotonically descending stack
            st = [digits[0]]

            for i in range(1, n):
                
                # note: because we want length-k largest number
                # there's additional check on whether st[-1] can be popped
                while st and digits[i] > st[-1] and len(st) + (n-i-1) >= k:
                    st.pop()

                # append the larger number
                st.append(digits[i])

            # trim off additional digits
            while len(st) > k:
                st.pop()

            return st

        # learnt something new...
        # did not know that we can take max op on two lists directly
        def merge(arr1, arr2):
            return [max(arr1, arr2).pop(0) for _ in range(len(arr1) + len(arr2))]

        # with the sub-task helper, we can explore different combinations 
        # arising from choosing length i from nums1, and length (k-i) from nums2
        # note: we can choose length 0 from one digits arr
        best = [-1] * k
        for i in range(k + 1):

            if i <= len(nums1) and k-i <= len(nums2):

                st1, st2 = largestNum(nums1, i), largestNum(nums2, k-i)
                curr_ans = merge(st1, st2)

                # compare curr to best
                better = True
                for j in range(k):
                    if curr_ans[j] < best[j]:
                        better = False
                        break
                    if curr_ans[j] > best[j]:
                        break

                if better:
                    best = curr_ans

        return best
    
nums1, nums2, k = [3,4,6,5], [9,1,2,5,8,3], 5
nums1, nums2, k = [6,7], [6,0,4], 5
nums1, nums2, k = [3,9], [8,9], 3
nums1, nums2, k = [8,6,9], [1,7,5], 3

# holy fk, very painful to debug
nums1 = [5,0,2,1,0,1,0,3,9,1,2,8,0,9,8,1,4,7,3]
nums2 = [7,6,7,1,0,1,0,5,6,0,5,0]
k = 31

nums1 = [9,5,6,2,4,3,6,2]
nums2 = [5,7,6,2,2,1,3,0,2,8,9,7,7,3,2,2,9,4,5,1]
k = 28

print(Solution().maxNumber(nums1, nums2, k))