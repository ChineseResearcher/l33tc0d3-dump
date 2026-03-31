# greedy - hard
class Solution:
    def generateString(self, str1: str, str2: str) -> str:

        n, m = len(str1), len(str2)

        res, F_idx = ["*"] * (n + m - 1), []
        # fill in the fixed part determined by "T"
        for i in range(n):
            if str1[i] == 'T':
                for j in range(i, i + m):
                    if res[j] != "*" and res[j] != str2[j-i]:
                        return ""
                    
                    res[j] = str2[j-i]
            else:
                F_idx.append(i)

        # for each F index, we ensure res[f_i...f_i+m-1] has at least one mismatch
        for i in F_idx:

            satisfied = False
            # track encountered unassigned indices
            st = []
            for j in range(i, i+m):
                # we only could change the unassigned "*"
                if res[j] == "*":
                    st.append(j)
                    res[j] = "a"
                    if res[j] != str2[j-i]:
                        satisfied = True
                        break
                else:
                    if res[j] != str2[j-i]:
                        satisfied = True
                        break

            if satisfied: continue
            # otherwise, we have to change res[last unassigned index] to "b"
            if not st: return ""
            res[st[-1]] = "b"

        return "".join(res).replace("*","a")

str1, str2 = "TFTF", "ab"
str1, str2 = "TFT", "aaa"
str1, str2 = "FTTT", "aa"
str1, str2 = "TFFF", "aa"
str1, str2 = "TFTF", "abc"

Solution().generateString(str1, str2)