# backtracking - medium
class Solution:
    def splitString(self, s: str) -> bool:

        def backtrack(startIdx, prevNum):
    
            if startIdx == n:
                return True if prevNum != str_num else False
            
            for i in range(startIdx, n):
                
                res = False
                selection = s[startIdx:i+1].lstrip('0')
                nextNum = int(selection) if selection else 0
                if prevNum < float('inf'):   
                    if nextNum + 1 == prevNum:
                        res = (res or backtrack(i+1, nextNum))
                
                # first number in the desc. series
                else:
                    res = (res or backtrack(i+1, nextNum))
                    
                if res:
                    return res
                    
            return False

        n = len(s)
        str_num = int(s.lstrip('0')) if s.lstrip('0') else 0
        return backtrack(0, float('inf'))
    
s = "00"
s = "1234"
s = "050043"
s = "9080701"
s = "000100098700065"
s = "20191817161514131211"

Solution().splitString(s)