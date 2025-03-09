# sliding window - medium
class Solution:
    def numberOfAlternatingGroups(self, colors, k):
        n = len(colors)
        # init. color mapping
        CM = {0:'R', 1:'B'}

        # specify a dict to keep track of the # of B/R 
        # on Even/Odd indices within the window respectively
        window = {'Even': {'B':0, 'R':0}, 'Odd': {'B':0, 'R':0}}

        # initiate window dict count with the first window
        indices = [i for i in range(1-k+n, n)] + [0]
        cnt = 0
        for idx in indices:
            if cnt % 2 == 0:
                window['Even'][CM[colors[idx]]] += 1
            else:
                window['Odd'][CM[colors[idx]]] += 1
            cnt += 1

        def isAlternating(window):
            # check if the current window is a k-size alternating group
            if (window['Odd']['B'] + window['Even']['R'] == k) or \
            (window['Odd']['R'] + window['Even']['B'] == k):
                return True
            
            return False

        # handling a fixed window of length k
        ans = 1 if isAlternating(window) else 0
        for idx in range(1, n):

            # we would need decrement the last element
            # since it's the 0-th element, it always belongs to Even
            window['Even'][CM[colors[(idx-k+n) % n]]] -= 1

            # we need to rotate the info on Even/Odd for each iteration
            window['Even'], window['Odd'] = window['Odd'], window['Even']

            # ingest the new element at colors[idx]
            if k % 2 == 0:
                # e.g. a length 6 window would ingest up to 5-th element (odd)
                window['Odd'][CM[colors[idx]]] += 1
            else:
                window['Even'][CM[colors[idx]]] += 1

            ans += 1 if isAlternating(window) else 0

        return ans
    
colors, k = [0,1,0,0,1,0,1], 6
colors, k = [0,1,0,1,0], 3
colors, k = [1,1,0,1], 4

Solution().numberOfAlternatingGroups(colors, k)