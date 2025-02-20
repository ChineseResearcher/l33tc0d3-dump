# monotonic stack - hard
class Solution:
    def nextSmallerArr(self, direction, numArr):

        n = len(numArr)
        smaller = [i for i in range(n)]
        # use monoStack of indices to find the next smaller/equal element to the right/left
        monoStack = []

        startIdx = 0 if direction == 1 else n-1
        endIdx = n if direction == 1 else -1
        increment = 1 if direction == 1 else -1

        for i in range(startIdx, endIdx, increment):

            if not monoStack:
                monoStack.append(i)
                continue

            while monoStack and numArr[i] < numArr[monoStack[-1]]:

                replaceIdx = monoStack.pop()
                smaller[replaceIdx] = i

            monoStack.append(i)

        return smaller

    def largestRectangleArea(self, heights):
        n = len(heights)

        lm, rm = self.nextSmallerArr(-1, heights), self.nextSmallerArr(1, heights)
        # for bars with no left/right smaller, we know for sure that the
        # left/right boundary can be fixed at 0 and n
        for i in range(n):
            if lm[i] == i: lm[i] = -1
            if rm[i] == i: rm[i] = n

        # the key to solving this is to ask ourselves:
        # taking the perspective of any bar, how far would its leftSmaller or rightSmaller
        # be able to reach without hitting a smaller bar
        # e.g. [1,4,5,2,3]
        # taking the perspective of bar 5, its left smaller 4 would at most end at 4
        # while its right smaller 2 can reach to where bar 3 is

        ans = 0
        for i in range(n):
            
            # edge case 1: treat curr. bar itself as the max area
            ans = max(ans, heights[i])
            # edge case 2: treat curr. bar as the bounding height and
            # compute the max area based on width: [lm[i], .., i, .. rm[i]]
            ans = max(ans, ((i-lm[i]-1) + 1 + (rm[i]-i-1)) * heights[i])

            # handle left bound
            if lm[i] == -1:
                lb = 0
                ans = max(ans, heights[i] * (i - lb + 1))
            else:
                lb = lm[lm[i]] + 1 if lm[i] > lm[lm[i]] else lm[i]
                ans = max(ans, heights[lm[i]] * (i - lb + 1))

            # handle right bound
            if rm[i] == n:
                rb = n-1
                ans = max(ans, heights[i] * (rb - i + 1))
            else:
                rb = rm[rm[i]] - 1 if rm[i] < rm[rm[i]] else rm[i]
                ans = max(ans, heights[rm[i]] * (rb - i + 1))

        return ans
    
# an extremely elegant solution from forum
class Solution:
    def largestRectangleArea(self, heights):

        # in the case of monotonically increasing heights
        # we would never be able to enter while-loop
        # thus we force a min. height of 0 to force entry
        # into while-loop at the rightmost bar
        heights.append(0)

        # a dummy index of -1 indicates left bound (left of first bar)
        # this monoStack would be ascending, and get popped upon smaller
        st = [-1]
        res = 0
        for i in range(len(heights)):
            
            # a key realisation is that once a smaller height
            # is encountered, we greedily pop the monoStack to compute area
            while heights[i] < heights[st[-1]]:
                h = heights[st.pop()]

                # nontrivial insight on width is that if some height at st[i]
                # is to be used as the bounding height, then it is valid all the way
                # till the index/bar @ st[i-1]
                w = i-st[-1]-1
                res = max(res, h*w)
                
            st.append(i)

        return res
    
heights = [2,1,5,6,2,3]
heights = [2,4]
heights = [5,6,11,12,11]
heights = [2,1,2] # ans: 3
heights = [4,2,0,3,2,5] # ans: 6 
heights = [3,6,5,7,4,8,1,0] # ans: 20
heights = [0,2,0] # ans: 2
heights = [999,999,999,999] # ans: 3996
heights = [5,4,4,6,3,2,9,5,4,8,1,0,0,4,7,2] # ans: 20

Solution().largestRectangleArea(heights)