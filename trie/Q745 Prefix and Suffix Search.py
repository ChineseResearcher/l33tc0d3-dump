# trie - hard
from typing import List
from functools import cache
class TrieNode:
    def __init__(self):
        self.children = {}
        self.idx = -1  # >= 0 indicates end of a word

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str, idx: int) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.idx = idx

class WordFilter:

    def __init__(self, words: List[str]):
        n = len(words)
        self.T, self.revT = Trie(), Trie()
        
        unique = dict()
        for i, w in enumerate(words):
            unique[w] = i

        # only insert every unique word with the largest index
        for w in unique:
            i = unique[w]
            self.T.insert(w, i)
            self.revT.insert(w[::-1], i)

    # helper to collect all indices i where words[i] contains a prefix
    def get_idx(self, prefix: str, Tr: Trie) -> set:

        res = set()
        node = Tr.root
        for char in prefix:
            if char not in node.children:
                return res # empty set
            node = node.children[char]

        # if entire prefix has been matched, use a DFS process to collect
        # all child nodes if they have a valid index
        def dfs(node: TrieNode) -> None:

            nonlocal res
            if node.idx != -1:
                res.add(node.idx)

            for next_node in node.children:
                _ = dfs(node.children[next_node])

        _ = dfs(node)
        return res

    @cache
    def f(self, pref: str, suff: str) -> int:
        valid = self.get_idx(pref, self.T) & self.get_idx(suff[::-1], self.revT)
        return max(valid) if valid else -1
    
words, pref, suff = ['apple'], 'a', 'e'
words, pref, suff = ['aabaa'], 'aab', 'baa'

WordFilter(words).f(pref, suff)
