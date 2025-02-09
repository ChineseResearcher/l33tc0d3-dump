# counting - medium
class Solution:
    def countBadPairs(self, nums) -> int:
        n = len(nums)
        # qn wants to find # of bad pairs where j-i != nums[j] - nums[i]
        # that inequality is equivalent to nums[j] - j != nums[i] - i

        # conversely, to find the # of good pairs
        # we look for cases where nums[j] - j == nums[i] - i
        # with the help of a dict that's updated along the iteration
        diff_dict = dict()

        good_pairs = 0
        for j in range(n):

            diff = nums[j] - j
            if diff not in diff_dict: 
                diff_dict[diff] = 1
                continue

            # if diff as a key does already exists, we can obtain the good pairs
            # w.r.t to nums[j] by querying for the count 
            good_pairs += diff_dict[diff]
            diff_dict[diff] += 1

        # the total number of pairs of size n nums
        # is (n-1) + (n-2) + ... + 1 = (n-1+1)*(n-1)/2
        return int(n*(n-1)/2 - good_pairs)
    
nums = [4,1,3,3]
nums = [1,2,3,4,5]

Solution().countBadPairs(nums)