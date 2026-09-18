# greedy - hard
class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:

        n = len(s)
        fmax = lambda a, b: a if a > b else b
        # key ideas:
        # 1) pre-process the string to denote the first and last appearing index
        # of every distinct letter in the string
        # 2) iterate through all appearing letters so as to record all valid
        # substring ranges (possibly expanded) s.t. it satisifes both stated conditions
        # 3) perform sorting by right end of ranges in ASC order and pick
        # the solution set greedily

        F, L = dict(), dict()
        for i in range(n):
            c = s[i]
            if c not in F:
                F[c] = i
            L[c] = i

        validRanges = []
        for c in F.keys():
            lb, rb = F[c], L[c]
            # greedy process to expand the range (lb, rb) to cover
            # ranges associated w/ all letters in s[lb: rb + 1]
            i = lb
            while i < rb:
                rb = fmax(rb, L[s[i]])
                if F[s[i]] < lb:
                    lb = F[s[i]]
                    i = lb
                else:
                    i += 1

            validRanges.append((lb, rb))

        validRanges.sort(key=lambda x: x[1])

        picked, pr = [], -1
        for l, r in validRanges:
            if l > pr:
                picked.append((l, r))
                pr = r

        return [s[l: r + 1] for l, r in picked]

s = "abab"
s = "abbaccd"
s = "bdacaccdb"
s = "adefaddaccc"
s = "dzdabazbbccd"
s = "abaabbcaaabbbccd"

Solution().maxNumOfSubstrings(s)