# dp - hard
class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:

        # imagine i1 / i2 as the respective indices for the 
        # unpacked str1 / str2, where str1 = s1 * n1
        # and i1 is in range [0, s1*n1 - 1], similarly for i2
        l1, l2, i1, i2 = len(s1), len(s2), 0, 0

        # the key to speeding up the matching is to identify cycles
        # and we identify a cycle by looking at two states
        # 1) the index we are matching in s1, represented by i1 % l1
        # 2) the index we are matching in s2, represented by i2 % l2
        dp = dict()

        L = l1 * n1 # length of str1
        while i1 < L:

            # matched
            if s1[i1 % l1] == s2[i2 % l2]:
                if (i1 % l1, i2 % l2) in dp:
                    
                    # upon locating a cycle we determine the cycle length
                    # by looking at the previous pair of indices
                    prev1, prev2 = dp[(i1 % l1, i2 % l2)]
                    cir1, cir2 = i1 - prev1, i2 - prev2

                    # the no. of cycles we can fast forward is
                    # constrained by the number of indices we are left with 
                    # before hitting L divided by the length of a cycle in s1 
                    count_cir1 = (L - i1) // cir1
                    i1 += count_cir1 * cir1
                    i2 += count_cir1 * cir2
                    if i1 >= L: 
                        break

                else:
                    dp[(i1 % l1, i2 % l2)] = (i1, i2)

                # advance i2 for matching character 
                i2 += 1

            # advance i1 to explore the next to-match character
            i1 += 1

        # one unpacked str2 is of length l2 * n2
        return i2 // (l2 * n2)
    
s1, n1, s2, n2 = "bacaba", 3, "abacab", 1
s1, n1, s2, n2 = "aaa", 20, "aaaaa", 1
s1, n1, s2, n2 = "baba", 11, "baab", 1
s1, n1, s2, n2 = "aaa", 3, "aa", 1
s1, n1, s2, n2 = "acb", 4, "ab", 2
s1, n1, s2, n2 = "acb", 4, "bc", 2
s1, n1, s2, n2 = "ecbafedcba", 4, "abcdef", 1
s1, n1, s2, n2 = "niconiconi", 99981, "nico", 81

Solution().getMaxRepetitions(s1, n1, s2, n2)