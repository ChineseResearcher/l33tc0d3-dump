# two pointers - medium
class Solution:
    def reverseWords(self, s: str) -> str:
        
        # key ideas:
        # 1) assume string "s" is mutable by converting it to List[str]
        # 2) O(1) space solution can be achieved by two-pointer

        s = s.lstrip(' ').rstrip(' ').split(' ')
        # clean our List[str] by only keeping alphanumeric components
        clean = []
        for x in s:
            if x.isalnum():
                clean.append(x)

        n = len(clean)
        l, r = 0, n-1
        while l < r:
            # in-place swap
            clean[l], clean[r] = clean[r], clean[l]
            # shift pointers
            l += 1
            r -= 1

        return ' '.join(clean)
    
s = "EPY2giL"
s = "the sky is blue"
s = "  hello world  "
s = "a good   example"

Solution().reverseWords(s)