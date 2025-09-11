# two pointers - medium
from collections import defaultdict
class Solution:
    def sortVowels(self, s: str) -> str:
        
        vowels = {'a','e','i','o','u','A','E','I','O','U'}

        ans, placeholder, v = [], [], defaultdict(int)
        for idx, char in enumerate(s):
            if char in vowels:
                ans.append('')
                placeholder.append(idx)
                v[char] += 1

            else:
                ans.append(char)

        ascii_order, j = 'AEIOUaeiou', 0
        for i in placeholder:
            while v[ascii_order[j]] == 0:
                j += 1

            ans[i] = ascii_order[j]
            v[ascii_order[j]] -= 1

        return ''.join(ans)
    
s = "lEetcOde"
s = "lYmpH"

Solution().sortVowels(s)