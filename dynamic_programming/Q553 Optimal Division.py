# dp - medium
class Solution:
    def recursive_optim_div(self, s_idx, e_idx):
        # given the sub-problem defined by start idx & end idx
        # compute the optimal (max) division result

        if s_idx == e_idx:
            return self.nums[s_idx]
        
        # case where a sub-problem only contains two nums
        # it has to return the division of it
        if e_idx - s_idx == 1:
            return self.nums[s_idx] / self.nums[e_idx]
        
        if (s_idx, e_idx) in self.dp: return self.dp[(s_idx, e_idx)]
        
        # otherwise we explore diff. possible splits
        currRes = 0 if s_idx == 0 else float('inf')
        currSplit = None
        for i in range(s_idx, e_idx):
            splitRes = self.recursive_optim_div(s_idx, i) / self.recursive_optim_div(i+1, e_idx)
            # one of the non-trivial realisation is that if we are to maximise
            # division of [a,b,c,d], then we want to minimize division of [b,c,d]
            if s_idx > 0:
                if splitRes < currRes:
                    currSplit = i
                    currRes = splitRes

            elif s_idx == 0:
                if splitRes > currRes:
                    currSplit = i
                    currRes = splitRes

        self.dp[(s_idx, e_idx)] = currRes
        self.dp_split[(s_idx, e_idx)] = currSplit
        return currRes

    def build_div_str(self, s_idx, e_idx, splits):

        if e_idx == s_idx + 1:
            return str(self.nums[s_idx]) + '/' + str(self.nums[e_idx])

        currSplit = splits[(s_idx, e_idx)]

        if currSplit == e_idx - 1:
            return self.build_div_str(s_idx, currSplit, splits) + '/' + str(self.nums[e_idx])
        
        if currSplit == s_idx:
            return str(self.nums[s_idx]) + '/' + '(' + self.build_div_str(currSplit+1, e_idx, splits) + ")"

    def optimalDivision(self, nums):
        # edge case
        if len(nums) == 1: return str(nums[0])

        self.nums = nums

        self.dp = dict()
        self.dp_split = dict()

        _ = self.recursive_optim_div(0, len(self.nums)-1)
        # it turns out that the answer is always to split at 0
        # for any num. arr [a,b,c,...,x,z] -> a / (b/c/d/../z) is the optimal
        # this is verified by the splits decisions recorded for each sub-problem
        return self.build_div_str(0, len(self.nums)-1, self.dp_split)
    
nums = [2,3,4]
nums = [1,2]
nums = [1000,100,10,2]
nums = [1,500,34,56,189,67,98,11,10]

Solution().optimalDivision(nums)