# greedy - medium
from typing import List
class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        
        m, n = len(strs[0]), len(strs)
        # key ideas:
        # 1) we need to remove an indice "i" across strs as long as we've 
        # detected one instance where strs[j][i] is smaller than strs[j-1][i]

        # 2) an exception to (1) is that there exists a smaller "i" where for
        # the same "j" we have strs[j][i] > strs[j-1][i], that is in other words, 
        # strs[j] have been proved to be strictly larger than strs[j-1] already

        # maintain an array denoting strictly larger status
        larger = [False] * n

        ans = 0
        for i in range(m):

            # one pass to first detect if this index is needed for removal
            to_del = False
            for j in range(1, n):
                if strs[j][i] < strs[j-1][i] and not larger[j]:
                    to_del = True
                    break

            if to_del:
                ans += 1
                continue
            
            # second pass to update larger status
            for j in range(1, n):
                if strs[j][i] > strs[j-1][i]:
                    larger[j] = True

        return ans

strs = ["ca","bb","ac"]
strs = ["aa","ab","ba"]
strs = ["aa","ab","bb"]
strs = ["xc","yb","za"]
strs = ["zyx","wvu","tsr"]

Solution().minDeletionSize(strs)