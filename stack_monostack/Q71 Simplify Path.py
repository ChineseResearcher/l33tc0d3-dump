# stack - medium
class Solution:
    def simplifyPath(self, path: str) -> str:
        
        # key ideas:
        # 1) first sanitize the path by taking care of multiple slashes, and single dots
        # 2) use a stack to address double dots and pop the immediate parent (if any)
        sp = path.split('/')
        sp = [x for x in sp if x and x != '.']

        st = []
        for x in sp:
            if x == '..':
                if st:
                    st.pop()
            else:
                st.append(x)

        return '/' + '/'.join(st)

path = "/../"
path = "/home/"
path = "/home//foo/"
path = "/a/../../b/../c//.//"
path = "/home/user/Documents/../Pictures"

Solution().simplifyPath(path)