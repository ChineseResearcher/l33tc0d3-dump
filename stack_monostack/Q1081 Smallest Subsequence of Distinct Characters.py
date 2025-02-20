# monotonic stack - medium
class Solution:
    def smallestSubsequence(self, s: str) -> str:
        # final subseq. should have length equal to count of distinct chars
        n = len(set(s))

        unique_left = [None] * len(s)

        unique_set = set()
        for i in range(len(s)-1, -1, -1):
            unique_set.add(s[i])
            unique_left[i] = unique_set.copy()

        # construct a monoAsc stack, which gets popped when a new
        # element that is of smaller alphabetical order is encountered
        monoAscStack = []

        ans = None
        for idx, char in enumerate(s):

            if char in monoAscStack:
                continue

            if len(monoAscStack) + 1 == n:
                ans = ''.join(monoAscStack) + char

            while monoAscStack and char < monoAscStack[-1]:
                popped = monoAscStack.pop()

                # if after popping, the count of unique elements
                # from monoStack and the unprocessed portion is less than n
                # we need to abort the greedy while loop to find smaller element
                if len(set(monoAscStack) | unique_left[idx]) < n:
                    monoAscStack.append(popped)
                    break

            monoAscStack.append(char)

        return ans
    
s = "bcabc"
s = "cbacdcbc"
s = "cdadabcc"
s = "ecbacba"

Solution().smallestSubsequence(s)