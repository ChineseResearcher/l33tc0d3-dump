# backtracking - medium
from typing import List
from functools import cache
class Solution:
    def maxLength(self, arr: List[str]) -> int:

        n = len(arr)

        def encode(s):
            mask = 0
            for char in s:
                bit = 1 << (ord(char) - ord("a"))
                if mask & bit:
                    # duplicate character found
                    return -1
                mask |= bit

            return mask

        def cnt_set_bit(mask):
            return bin(mask).count('1')
        
        @cache
        def backtrack(pattern, idx):

            # as input is small, we can just exhaust
            # all possible valid concatenations and track the longest
            if idx == n:
                self.ans = max(self.ans, cnt_set_bit(pattern))
                return
            
            # can always skip curr. string
            backtrack(pattern, idx + 1)
            for i in range(idx, n):
                new_mask = encode(arr[i])

                # only include curr. string if it is valid
                if new_mask > 0 and not (pattern & new_mask):

                    pattern |= new_mask
                    backtrack(pattern, i + 1)
                    pattern ^= new_mask # backtrack

        self.ans = 0
        _ = backtrack(0, 0)
        return self.ans
    
arr = ["un","iq","ue"]
arr = ["cha","r","act","ers"]
arr = ["abcdefghijklmnopqrstuvwxyz"]
arr = ["jnfbyktlrqumowxd","mvhgcpxnjzrdei"]
arr = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p"]

Solution().maxLength(arr)