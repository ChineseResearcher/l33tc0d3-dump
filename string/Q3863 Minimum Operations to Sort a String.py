# string - medium
class Solution:
    def minOperations(self, s: str) -> int:

        n = len(s)
        # key ideas:
        # 1) we enumerate the possible cases by observing the min. / max. char
        # and the last char. in the original string s
        # 2) sorting logic for diff. cases:
        # (a) if last char. is already the largest char. or that the first char. is already
        # the smallest char., we just need to sort the complement
        # (b) if smallest char. is not the first and largest is not he last, then we can surely
        # obtain sorted by sorting s[:-1] -> s[1:] (or s[1:] -> s[:-1])
        # (c) excluding the above, it can only be up to 3 operations (e.g. 'edc')
        sortStr = lambda s: ''.join(sorted(s))

        ss = sortStr(s)
        if s == ss: return 0
        if n == 2: return -1

        minn, maxx = ss[0], ss[-1]
        if s[-1] == maxx:
            return 1
        else:
            if s[0] == minn:
                return 1
            elif s[-1] == minn:
                # try sort s[1:] first
                cs, cnt = s, 0
                ns = cs[0] + sortStr(cs[1:])
                if ns != cs:
                    cnt += 1
                cs = ns
                # if last char. is already maxed, just sort s[:-1]
                if cs[-1] == maxx:
                    return cnt + 1
                # try sort s[:-1] first
                cs, cnt = s, 0
                ns = sortStr(cs[:-1]) + cs[-1]
                if ns != cs:
                    cnt += 1
                cs = ns
                # if first char. is already minnimized, just sort s[1:]
                if cs[0] == minn:
                   return cnt + 1
                # worst case
                return 3
            else:
                return 2
            
s = "gf"
s = "cab"
s = "dog"
s = "gjg"
s = "jgg"
s = "card"
s = "onon"
s = "obmk"

Solution().minOperations(s)