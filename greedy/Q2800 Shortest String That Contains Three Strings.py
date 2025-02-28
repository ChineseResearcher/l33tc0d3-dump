# greedy - medium
class Solution:
    def generate_shortest(self, a, b, c):
        # find the shortest super string if we are to
        # process in the order a -> b -> c

        # special cases...
        if b in a: b = ''
        if c in b: c = ''

        # detect if some beginning part of b is some tail part of a
        for i in range(len(a)):
            if a[i:] == b[:(len(a)-i)]: 
                break

            if i == len(a)-1: i += 1

        a_b = a[:i] + a[i:] + b[(len(a)-i):]

        # detect if some beginning part of c is some tail part of a_b
        for j in range(len(a_b)):
            if a_b[j:] == c[:(len(a_b)-j)]:
                break

            if j == len(a_b)-1: j += 1

        a_b_c = a_b[:j] + a_b[j:] + c[(len(a_b)-j):]
        return a_b_c

    def minimumString(self, a: str, b: str, c: str) -> str:
        ans = None

        # special cases
        if b in a and c in a: return a
        if a in b and c in b: return b
        if a in c and b in c: return c

        # given three strings a,b,c
        # there are in total six ways of permuting the processing order:
        # 1) with "a" as head, a -> b -> c, a -> c -> b
        # 2) with "b" as head, b -> a -> c, b -> c -> a
        # 3) with "c" as head, c -> a -> b, c -> b -> a

        permutations = [(a,b,c),(a,c,b),(b,a,c),(b,c,a),(c,a,b),(c,b,a)]
        for a, b, c in permutations:
            res = self.generate_shortest(a, b, c)
            if ans == None:
                ans = res
                continue

            if len(res) < len(ans):
                ans = res

            elif len(res) == len(ans):
                ans = min(ans, res)

        return ans
    
a, b, c = "abc", "bca", "aaa"
a, b, c = "ab", "ba", "aba"
a, b, c = "aba", "c", "b"
a, b, c = "cac", "b", "a"

Solution().minimumString(a, b, c)