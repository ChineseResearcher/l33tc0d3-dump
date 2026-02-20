# sorting - hard
class Solution:
    def makeLargestSpecial(self, s: str) -> str:

        n = len(s)

        def prefix_cnt_check(s:str) -> bool:

            o = 0
            for i in range(len(s)):
                o += int(s[i])
                if o < i+1-o:
                    return False

            return True

        while True:

            curr_best = s
            for i in range(n):

                # two lists to store the special substrings
                # admissible from s[:i] and s[i+1:] respectively
                before, after = [], []

                # track number of "1"s
                o = 0
                for j in range(i, -1, -1):
                    o += int(s[j])
                    length = i-j+1
                    if length % 2 == 0 and o == length // 2:
                        candidate = s[j:i+1]
                        # validate 2nd property of special substring
                        if prefix_cnt_check(candidate):
                            before.append(candidate)

                o = 0
                for j in range(i+1, n):
                    o += int(s[j])
                    length = j-i
                    if length % 2 == 0 and o == length // 2:
                        candidate = s[i+1:j+1]
                        if prefix_cnt_check(candidate):
                            after.append(candidate)
                
                # invalid split
                if not before or not after:
                    continue

                before.sort()
                after.sort(reverse=True)

                x, y = before[0], after[0]
                candidate = s[:i+1-len(x)] + y + x + s[i+1+len(y):]
                if candidate > curr_best:
                    curr_best = candidate

            # no improvement
            if curr_best == s:
                break

            s = curr_best

        return s

s = "10"
s = "11011000"
s = "101100101100"

Solution().makeLargestSpecial(s)