# sliding window - hard
from itertools import combinations
from typing import List
class Solution:
    def maxDifference(self, s: str, k: int) -> int:
        n = len(s)
        digits = set(s)
        # create pfSum for each possible digits in range [0,4]
        pfSum = [ [0] * n for _ in range(5) ]
        for d in digits:

            rSum = 0
            for i in range(n):
                rSum += 1 if s[i] == d else 0
                pfSum[int(d)][i] = rSum

        def parityEncode(a:int, b:int) -> str:

            # for the counts of two given digits
            # encode the parity for each digit's count
            aOdd, bOdd = a % 2, b % 2
            return str(aOdd) + str(bOdd)

        def pfCheck(x:str, i:int, j:int, pfSum:List[List[int]]) -> bool:
            if i < 0:
                return (pfSum[int(x)][j] > 0)
            else:
                return (pfSum[int(x)][j] - pfSum[int(x)][i] > 0)

        # the desired complementary mapping states for a substring s[0...j]
        # i.e. for some i < j-k+1, we would need substring s[0...i] to be of
        # certain parity states s.t. s[i+1...j] can be a valid substring
        cmap = {'11':'01', '00':'10', '01':'11', '10':'00'} 

        # create our combinations
        pairs = []
        for a, b in combinations(['0','1','2','3','4'], 2):
            pairs.append((a,b))
            pairs.append((b,a))

        ans = float('-inf')
        # the enumeration part comes in as we want to fix onto two digits at any time
        for a, b in pairs:
            
            # validate if a combination exists
            if a not in digits or b not in digits:
                continue
            
            # for the valid comb. (a,b), treat:
            # "a" as the target odd freq. digit
            # "b" as the target even freq. digit

            # a crucial mathematical insight here is that
            # suppose we define a substring s[i+1...j] as a valid candidate
            # s.t. len(s[i+1...j]) >= k and freq[a] being odd and freq[b] being even
            # we could use idea of prefix-sum to represent:
            # freq[a] as: count(a, j) - count(a, i)
            # freq[b] as: count(b, j) - count(b, i)
            
            # in order to MAXIMISE freq[a] - freq[b], which is our answer,
            # it is equivalent to maximising:
            # count(a, j) - count(a, i) - (count(b, j) - count(b, i))
            # rearranging, we have
            # (count(a, j) - count(b, j)) - (count(a, i) - count(b, i))
            # and thus our goal is to find the MINIMUM (count(a, i) - count(b, i))
            # corresponding to our current j

            # w/ the above context, we init. the best (min.) "count(a, i) - count(b, i)"" values
            # for all four different states possible
            i_min = {'10':float('inf'), '11':float('inf'), '00':float('inf'), '01':float('inf')}

            # perform a linear pass sliding window here
            i = 0
            ai, bi, aj, bj = 0, 0, 0, 0 # counts of a or b at index i or j
            for j in range(n):
                
                # update count
                if s[j] == a:
                    aj += 1
                if s[j] == b:
                    bj += 1

                if j + 1 < k:
                    continue
                
                # explore all admissible i s.t. s[i+1...j].length >= k
                while i < j-k+1 and pfCheck(a,i,j,pfSum) and pfCheck(b,i,j,pfSum):
                    if s[i] == a:
                        ai += 1
                    if s[i] == b:
                        bi += 1

                    key = parityEncode(ai, bi)
                    i_min[key] = min(i_min[key], ai - bi)
                    i += 1 # shrink window

                # note that after the above sliding (if any)
                # we are guaranteed that s[l..r] respects:
                # 1) min. length of k
                # 2) min. 1 occurrence for "a" & "b" each

                # access the complementary parity state if necessary
                key = parityEncode(aj, bj)
                if key == '10':
                    # for s[0...j] w/ parity state '10', it's already in the
                    # desired form: "a" has odd cnt, "b" has even cnt
                    # we can always just take the diff of "a" & "b" and see if it improves ans 
                    if aj > 0 and bj > 0:
                        ans = max(ans, aj - bj)
                
                if pfCheck(a,i-1,j,pfSum) and pfCheck(b,i-1,j,pfSum):
                    ans = max(ans, aj - bj - i_min[cmap[key]]) # complementary

        return ans
    
s, k = "12233", 4
s, k = "1122211", 3
s, k = "110", 3
s, k = "2421", 1
s, k = "300", 2
s, k = "2222130", 2
s, k = "44114402", 7
s, k = "2400030144", 2

Solution().maxDifference(s, k)