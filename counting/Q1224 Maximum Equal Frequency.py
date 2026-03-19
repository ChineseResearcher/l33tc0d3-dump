# counting - hard
from typing import List
from collections import defaultdict
class Solution:
    def maxEqualFreq(self, nums: List[int]) -> int:

        # key ideas:
        # 1) init. two hashmaps, where cnt_num stores <cnt: set of numbers>
        # and num_cnt stores <number: cnt>
        # 2) a valid prefix is identified iff there exists the size of cnt_num
        # is either 1 OR 2
        cnt_num, num_cnt = dict(), defaultdict(int)

        ans = 0
        for idx, x in enumerate(nums):

            # making updates to two hashmaps
            prev_cnt = num_cnt[x]
            new_cnt = prev_cnt + 1

            if prev_cnt in cnt_num:
                cnt_num[prev_cnt].discard(x)
                if not cnt_num[prev_cnt]:
                    del cnt_num[prev_cnt]

            if new_cnt not in cnt_num:
                cnt_num[new_cnt] = set()
            cnt_num[new_cnt].add(x)

            num_cnt[x] += 1
            
            # judge prefix
            if len(cnt_num) == 1:
                k = list(cnt_num.keys())[0]

                # case 1: every element so far only appears once
                # e.g. [1,2,3,4], by deleting any element, the remaining
                # still satisfies equivalent frequencies
                if k == 1:
                    ans = idx + 1

                # case 2: there is only 1 unique number for that 1 frequency
                # e.g. [2,2,2], removing any 2 is satisfactory
                if len(cnt_num[k]) == 1:
                    ans = idx + 1

            if len(cnt_num) == 2:

                sk = sorted(cnt_num.keys())
                k1, k2 = sk[0], sk[1]

                # case 1: k2 is larger than k1 by exactly 1
                # and there is only one member in cnt_num[k2]
                if k2 == k1 + 1:
                    if len(cnt_num[k2]) == 1:
                        ans = idx + 1

                # case 2: k1 is equal to 1, and there is only
                # one member in cnt_num[1]
                if k1 == 1:
                    if len(cnt_num[1]) == 1:
                        ans = idx + 1

        return ans

nums = [1,1]
nums = [1,2]
nums = [2,2,1,1,5,3,3,5]
nums = [1,1,1,2,2,2,3,3,3,4,4,4,5]

Solution().maxEqualFreq(nums)