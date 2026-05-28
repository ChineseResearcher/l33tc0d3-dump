# greedy - medium
class Solution:
    def minimumCost(self, s: str, t: str, flipCost: int, swapCost: int, crossCost: int) -> int:

        n = len(s)
        # key ideas:
        # 1) count the two types of mismatches: 
        # (s[i]='0' and t[i]='1') OR (s[i]='1' and t[i]='0')

        # 2) every pair of '01' and '10' mismatch can be optimally
        # resolved by performing a swap or two flips

        # 3) among the remaining purely '01' or '10' mismatches, every pair
        # can be again optimally resolved by performing a cross-swap + swap or two flips

        # 4) if there's a leftover unpaired mismatch, we perform a flip to resolve

        mc_01, mc_10 = 0, 0
        for i in range(n):
            if s[i] == '0' and t[i] == '1':
                mc_01 += 1
            if s[i] == '1' and t[i] == '0':
                mc_10 += 1

        ans = 0
        swapCnt = min(mc_01, mc_10)
        ans += swapCnt * min(swapCost, 2 * flipCost)

        mc_01 -= swapCnt
        mc_10 -= swapCnt

        rem = max(mc_01, mc_10)
        if rem > 0:
            ans += (rem // 2) * min(swapCost + crossCost, 2 * flipCost)
            if rem % 2 == 1:
                ans += flipCost

        return ans
    
s, t, flipCost, swapCost, crossCost = "101", "001", 1, 1, 4
s, t, flipCost, swapCost, crossCost = "001", "010", 3, 3, 5
s, t, flipCost, swapCost, crossCost = "1010", "1010", 5, 5, 5
s, t, flipCost, swapCost, crossCost = "001", "110", 2, 100, 100
s, t, flipCost, swapCost, crossCost = "01000", "10111", 10, 2, 2
s, t, flipCost, swapCost, crossCost = "00100", "11001", 3, 2, 3

Solution().minimumCost(s, t, flipCost, swapCost, crossCost)