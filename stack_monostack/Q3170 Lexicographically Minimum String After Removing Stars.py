# stack - medium
class Solution:
    def clearStars(self, s: str) -> str:

        # maintain a hashmap of indices of every char processed
        # and a set storing discarded characters
        h, discard = dict(), set()

        for idx, char in enumerate(s):

            if char != '*':
                if char not in h:
                    h[char] = []
                h[char].append(idx)

            # case of removal
            else:

                # query for the smallest character
                sc = min(h.keys())

                # greedy thinking:
                # there's a greedy thinking embedded in always choosing
                # the last possible smallest character if there are multiple
                # reason being if we choose any earlier smallest char., then
                # our leftover string would be bigger, so if we choose the one
                # at the back, it minimises the impact of revealing a bigger character
                # to the lexigraphical ordering of the leftover string.
                discard.add(h[sc].pop())

                if not h[sc]:
                    del h[sc]

        # based on discarded, construct the leftover string
        ans = []
        for idx, char in enumerate(s):

            if char == '*':
                continue

            if idx not in discard:
                ans.append(char)

        return ''.join(ans)
    
s = "abac*"
s = "aaba*"
s = "abc"

Solution().clearStars(s)