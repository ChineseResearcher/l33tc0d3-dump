# string - medium
class Solution:
    def doesAliceWin(self, s: str) -> bool:
        
        # core ideas:
        # 1) realise that Alice always wins regardless of odd/even count of vowels
        # 2) Alice only loses strictly when there's no vowels to begin with
        vowels = {'a','e','i','o','u'}

        for char in s:
            if char in vowels:
                return True

        return False
    
s = "leetcoder"
s = "bbcd"

Solution().doesAliceWin(s)