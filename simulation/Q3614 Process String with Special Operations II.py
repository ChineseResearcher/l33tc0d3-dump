# simulation - hard
class Solution:
    def processStr(self, s: str, k: int) -> str:

        # key ideas:
        # 1) forward simulation is not feasible, as final string.length <= 1e15
        # 2) backward simulation by undo-ing all special operators (#, %, *)
        # 3) forward simulation to keep track of the simulated lengths,
        # and also store the form simulated string right before the first operator
        L, sl = [], 0

        firstOp, clean = -1, []
        for i, c in enumerate(s):
            if firstOp < 0 and c in ['#','%'] and clean:
                firstOp = i
            # modify our tracked string
            if firstOp < 0:
                if c.islower():
                    clean.append(c)
                if c == '*' and clean:
                    clean.pop()
            # modify string length
            if c == '#':
                sl *= 2
            elif c == '*':
                sl = max(sl-1, 0)
            elif c.islower():
                sl += 1
            L.append(sl)

        # invalid k
        if k >= L[-1]: return '.'

        for i in range(len(s)-1, firstOp-1, -1):
            c = s[i]
            pl = L[i-1] if i-1 >= 0 else 0
            if c == '#':
                # re-locate our k by using modulo
                k %= pl
            elif c == '%':
                # re-locate our k by doing mirror swap
                k = pl - k - 1
            elif c.islower():
                if k == L[i] - 1:
                    return c

        return clean[k]

s, k = "qe*vkg", 1
s, k = "%#%jv#%", 1
s, k = "qud#y", 6

Solution().processStr(s, k)