# two pointers - medium
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:

        v1 = version1.split('.')
        v2 = version2.split('.')

        # get the longer length
        n = max(len(v1), len(v2))

        # match longer revision length
        if len(v1) < n:
            v1.extend(['0'] * (n-len(v1)))

        if len(v2) < n:
            v2.extend(['0'] * (n-len(v2)))

        for i in range(n):
            if int(v1[i]) < int(v2[i]):
                return -1
            elif int(v1[i]) > int(v2[i]):
                return 1

        return 0
    
version1, version2 = "1.2", "1.010"
version1, version2 = "1.01", "1.001"
version1, version2 = "1.0", "1.0.0.0"

Solution().compareVersion(version1, version2)