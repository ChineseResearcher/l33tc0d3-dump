# array - medium
class Solution:
    def minOperations(self, nums: list[int]) -> int:
        
        n = len(nums)
        # key ideas:
        # 1) observe that the array has to be monotonically ascending / descending
        # at any point onwards for a full cycle for it to have an answer
        # 2) enumerate the diff. possible arrangements for a valid monotonic array
        mn, mx = 0, n - 1
        mn_i, mx_i = nums.index(mn), nums.index(mx)

        # test for monotonic ascending
        isAsc, k, i = True, n - 1, mn_i
        while k > 0:
            j = (i + 1 + n) % n
            if nums[j] < nums[i]:
                isAsc = False
                break
            i = j
            k -= 1
        if isAsc:
            # op1: left shift min. element to the 1st
            op1 = mn_i
            # op2: reverse + left shift max. element to the 1st + reverse
            op2 = 1 + (n - mx_i - 1) + 1
            return min(op1, op2)

        # test for monotonic descending
        isDesc, k, i = True, n - 1, mx_i
        while k > 0:
            j = (i + 1 + n) % n
            if nums[j] > nums[i]:
                isDesc = False
                break
            i = j
            k -= 1
        if isDesc:
            # op1: reverse + left shift min. element to the 1st
            op1 = 1 + (n - mn_i - 1)
            # op2: left shift max. element to the 1st + reverse
            op2 = mx_i + 1
            return min(op1, op2)

        return -1

nums = [0,2,1]
nums = [1,0,2]
nums = [2,0,1,3]

Solution().minOperations(nums)