# stack - medium
class Solution:
    def checkValidString(self, s: str) -> bool:
        
        # key ideas:
        # 1) first use a stack to annihilate all unclosed left brackets
        # w/ found right brackets in "s" as much as possible
        # 2) in the updated stack w/ only "(" and "*" (if any), traverse backwards
        # to validate if at any point all left brackets can be sufficiently annihilated
        # by wildcards to the right

        st1 = []
        for char in s:
            if char == ")":
                # store all wildcards popped
                st2 = [] 
                # find nearest left bracket to the left
                while st1 and st1[-1] != "(":
                    st2.append(st1.pop())
                if not st1:
                    # no wildcard
                    if not st2: return False
                    # use a wildcard
                    st2.pop()
                else:
                    # address the unclosed left bracket
                    st1.pop()
                st1.extend(st2)    
            else:
                st1.append(char)

        wildcard, unclosed = 0, 0
        for char in st1[::-1]: 
            if char == "(":
                unclosed += 1
            if char == "*":
                wildcard += 1
            if unclosed > wildcard:
                return False

        return True

s = "()"
s = "(*)"
s = "(*))"

Solution().checkValidString(s)