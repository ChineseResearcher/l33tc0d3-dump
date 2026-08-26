# sliding window - medium
class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:

        n = len(s)
        # key ideas:
        # 1) use a sliding window and track the smallest window(s) that satisfy
        # the condition that the number of "1"s is exactly k
        # 2) record all candidate(s) having the smallest window, and sort to get answer

        smallest, o, l = [], 0, 0
        for r in range(n):
            if s[r] == '1':
                o += 1

            while o > k:
                if s[l] == '1':
                    o -= 1
                l += 1

            while l < r and s[l] == '0':
                l += 1

            winLen = r - l + 1
            if o == k:
                substr = s[l:r+1]
                if smallest:
                    if winLen < len(smallest[-1]):
                        smallest = [substr] # reset
                    elif winLen == len(smallest[-1]):
                        smallest.append(substr)
                else:
                    smallest.append(substr)

        smallest.sort()
        return smallest[0] if smallest else ''

s, k = "000", 1
s, k = "1011", 2
s, k = "100011001", 3

Solution().shortestBeautifulSubstring(s, k)