# bit manipulation - medium
class Solution:
    def doesValidArrayExist(self, derived) -> bool:
        ori_1, ori_2 = [0], [1]

        for xor_val in derived[:-1]:

            if xor_val == 1:
                if ori_1[-1] == 1:
                    ori_1.append(0)
                else:
                    ori_1.append(1)

                if ori_2[-1] == 1:
                    ori_2.append(0)
                else:
                    ori_2.append(1)

            elif xor_val == 0:
                ori_1.append(ori_1[-1])
                ori_2.append(ori_2[-1])

        if derived[-1] == 1:
            if ori_1[-1] != ori_1[0] or ori_2[-1] != ori_2[0]:
                return True
            
        if derived[-1] == 0:
            if ori_1[-1] == ori_1[0] or ori_2[-1] == ori_2[0]:
                return True
            
        return False
    
derived = [1,1,0]
derived = [1,1]
derived = [1,0]

Solution().doesValidArrayExist(derived)
        