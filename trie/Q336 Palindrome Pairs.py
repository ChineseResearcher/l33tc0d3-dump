# trie - hard
from typing import List
def is_palindrome(substr: str) -> bool:
    if not substr: return False
    k = len(substr)
    return substr[:k//2] == substr[(k//2)+(1 if k % 2 == 1 else 0):][::-1]

class TrieNode:
    def __init__(self):
        self.children = {}     
        self.is_end = False
        self.idx = -1
        self.trail_palin = set()    

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str, idx:int, prefix_palin_state: List[bool]) -> None:
        node = self.root

        k = len(word)
        # reverse insertion from index k-1
        for i in range(k-1, -1, -1):
            ch = word[i]
            if ch not in node.children:
                node.children[ch] = TrieNode()
            # mark increment if prefix word[:i-1] is a palindrome
            if i-1 >= 0 and prefix_palin_state[i-1]: 
                node.children[ch].trail_palin.add(idx)
            # move to child
            node = node.children[ch]

        node.is_end = True
        node.idx = idx

    def match(self, word: str) -> int:
        node = self.root

        palin_idx = set()
        for idx, ch in enumerate(word):
            if ch not in node.children:
                return palin_idx
            
            node = node.children[ch]
            if node.is_end and is_palindrome(word[idx+1:]):
                palin_idx.add(node.idx)

        # case of exact mirrored match: e.g. "ab" + "ba"
        if node.is_end:
            palin_idx.add(node.idx)

        # also consider trailing palindromes
        # e.g. "(X..some palindrome...X)ab" + "ba" where "ba" is the word input
        palin_idx |= node.trail_palin
        return palin_idx

class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        
        T = Trie()
        # edge case:
        # suppose there's an empty word, then every unique non-empty word
        # that's a palindrome itself could form 2 palindromes w/ the empty word
        empty_idx, self_palin = -1, []

        # first pass to build each unique word and their trailing palindrome count
        for idx, w in enumerate(words):

            if not w:
                empty_idx = idx
                continue

            k = len(w)
            prefix_palin_state = [is_palindrome(w[:i+1]) for i in range(k)]
            T.insert(w, idx, prefix_palin_state)

            # a palindrome itself
            if prefix_palin_state[-1]:
                self_palin.append(idx)

        ans = []
        if empty_idx != -1:
            for idx in self_palin:
                ans.append([idx, empty_idx])
                ans.append([empty_idx, idx])

        # second pass to find out palindrome pairs
        for idx, w in enumerate(words):
            res = T.match(w)
            # discount by 1 if w itself is already a palindrome
            if is_palindrome(w):
                res.discard(idx)

            for j in res:
                ans.append([idx, j])

        return ans

words = ["a",""]
words = ["bat","tab","cat"]
words = ["abcd","dcba","lls","s","sssll"]
words = ["a","b","c","ab","ac","aa"]

Solution().palindromePairs(words)