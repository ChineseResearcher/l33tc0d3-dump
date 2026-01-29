# dp - hard
import heapq
from typing import List
class TrieNode:
    def __init__(self):
        self.children = {}
        self.key = -1  # default

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word, key):
        node = self.root
        for ch in word:
            node = node.children.setdefault(ch, TrieNode())
        node.key = key  # assign key at terminal node

class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:

        n, m = len(source), len(original)
        fmin = lambda a, b: a if a < b else b

        curr = 0
        uid = dict()
        for x in original + changed:
            if x not in uid:
                uid[x] = curr
                curr += 1

        L = len(uid)

        # Build adjacency list (directed)
        adj = [[] for _ in range(L)]
        for i in range(m):
            u, v, w = uid[original[i]], uid[changed[i]], cost[i]
            adj[u].append((v, w))

        def dijkstra(s):
            dist = [float('inf')] * L
            dist[s] = 0
            pq = [(0, s)]
            while pq:
                d, u = heapq.heappop(pq)
                if d != dist[u]:
                    continue
                for v, w in adj[u]:
                    nd = d + w
                    if nd < dist[v]:
                        dist[v] = nd
                        heapq.heappush(pq, (nd, v))
            return dist

        # L x L distance matrix
        dist = [dijkstra(s) for s in range(L)]

        T = Trie()
        for ustr, key in uid.items():
            T.insert(ustr[::-1], key)

        dp = [float('inf')] * n
        for i in range(n):
            
            j = i

            bestCost = float('inf')
            # define a boolean to track if source[j...i] already matches target[j...i]
            stillMatch = (source[j] == target[j])
            while stillMatch:
                bestCost = fmin(bestCost, dp[j-1] if j-1 >= 0 else 0)
                if j - 1 < 0:
                    break
                j -= 1
                stillMatch &= (source[j] == target[j]) 

            # re-start search (from j=i) using pattern in Trie
            j, n1, n2 = i, T.root, T.root
            # note: we need two nodes for traversal in tandem
            # as we are matching source & target arrays index by index
            while source[j] in n1.children and target[j] in n2.children:
                n1, n2 = n1.children[source[j]], n2.children[target[j]]
                if n1.key != -1 and n2.key != -1:
                    bestCost = fmin(bestCost, (dp[j-1] if j-1 >= 0 else 0) + \
                                               dist[n1.key][n2.key])
                if j - 1 < 0:
                    break
                j -= 1

            dp[i] = bestCost

        return dp[-1] if dp[-1] < float('inf') else -1

source, target = "abcd", "acbe"
original, changed, cost = ["a","b","c","c","e","d"], ["b","c","b","e","b","e"], [2,5,5,1,2,20]

source, target = "abcdefgh", "acdeeghh"
original, changed, cost = ["bcd","fgh","thh"], ["cde","thh","ghh"], [1,3,5]

source, target = "abcdefgh", "addddddd"
original, changed, cost = ["bcd","defgh"], ["ddd","ddddd"], [100,1578]

Solution().minimumCost(source, target, original, changed, cost)