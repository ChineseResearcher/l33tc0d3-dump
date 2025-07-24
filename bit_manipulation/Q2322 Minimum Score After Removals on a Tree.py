# bit manipulation - hard
from typing import List
import functools
import operator
from collections import defaultdict
class Solution:
    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int: 

        g = defaultdict(set)
        for u, v in edges:
            g[u].add(v)
            g[v].add(u)

        totalXOR = functools.reduce(operator.xor, nums)

        # core idea: leverage the cancellation property of XOR (i.e. a ^ b ^ a = b)
        # then for every edge (u, v), pre-compute the XOR of two subtrees assuming u - v is broken
        def dfs(treeNode, parent, mem_dict):

            mem_dict.add(treeNode)
            curr_res = nums[treeNode]
            for neighbour in g[treeNode]:
                if neighbour != parent:
                    curr_res ^= dfs(neighbour, treeNode, mem_dict)

            return curr_res

        subtree_XOR = dict()
        subtree_reg = dict()

        for u, v in edges:

            # break u-v
            g[u].discard(v)
            g[v].discard(u)

            # key init
            k = str(u) + '-' + str(v)

            # construct member dict
            subtree_reg[k] = dict()
            subtree_reg[k][u] = set()
            subtree_reg[k][v] = set()

            subtree_XOR[k] = dict()

            # dfs for pre-compute
            subtree_XOR[k][u] = dfs(u, -1, subtree_reg[k][u])
            subtree_XOR[k][v] = dfs(v, -1, subtree_reg[k][v])

            # rollback edge deletion
            g[u].add(v)
            g[v].add(u)

        # there are n-1 edges
        m = len(edges)

        ans = float('inf')
        # explore deletion pairs
        for i in range(m-1):
            for j in range(i+1, m):
                
                u, v = edges[i]
                x, y = edges[j]
                
                # create access keys
                k_uv = str(u) + '-' + str(v)
                k_xy = str(x) + '-' + str(y)

                # there could be four pairs of access points
                # namely, (u, x), (u, y), (v, x), (v, y)
                # we need to find a pair s.t. both of them do not appear
                # in the counterpart's subtree member dict
                for p1, p2 in [(u, x), (u, y), (v, x), (v, y)]:
                    if p1 not in subtree_reg[k_xy][p2] and p2 not in subtree_reg[k_uv][p1]:

                        # compute the XOR of third component
                        xor1 = subtree_XOR[k_uv][p1]
                        xor2 = subtree_XOR[k_xy][p2]
                        xor3 = totalXOR ^ xor1 ^ xor2

                        maxXOR = max(xor1, max(xor2, xor3))
                        minXOR = min(xor1, min(xor2, xor3))

                        ans = min(ans, maxXOR - minXOR)

                        break # only one pair is valid

        return ans
    
nums, edges = [1,5,5,4,11], [[0,1],[1,2],[1,3],[3,4]]
nums, edges = [5,5,2,4,4,2], [[0,1],[1,2],[5,2],[4,3],[1,3]]

Solution().minimumScore(nums, edges)