# trie - medium
from collections import deque
from typing import List
# numTrie is here to assist us count number of distinct
# subarrays that have at most k elements divisible by p
class NumTrieNode:
    def __init__(self):
        self.children = {}  # key: int, value: NumTrieNode

class NumTrie:
    def __init__(self):
        self.root = NumTrieNode()
        self.count = 0

    # the use of Trie is very elegant here,
    # it allows us to keep growing our answers while it lasts
    # otherwise we have to first use O(n^2) to generate all subarrays
    # then use additional O(n) to verify if it is a duplicate
    def insert(self, num_list, k, p):

        divCnt, curr = 0, self.root
        # insert continues as long as divCnt do not exceed k
        for x in num_list:

            if x % p == 0:
                divCnt += 1

            if divCnt > k:
                break
                
            if x not in curr.children:
                curr.children[x] = NumTrieNode()
                self.count += 1
            curr = curr.children[x]

class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:

        tr = NumTrie()
        subarr = deque(nums)

        # enumerate all possible starting indices
        while subarr:

            tr.insert(subarr, k, p)
            subarr.popleft()

        return tr.count
    
nums, k, p = [2,3,3,2,2], 2, 2
nums, k, p = [1,2,3,4], 4, 1

Solution().countDistinct(nums, k, p)