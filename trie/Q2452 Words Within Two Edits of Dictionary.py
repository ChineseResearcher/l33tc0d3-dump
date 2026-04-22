# trie - medium
from typing import List
class TrieNode:
    def __init__(self):
        self.children = {}  
        self.is_word = False 

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_word = True

    def search(self, word: str) -> bool:
        self.word = word
        # allow up to 2 character differences
        return self._dfs(0, self.root, 2) 
        
    def _dfs(self, idx: int, node: TrieNode, tol: int) -> bool:
        
        if idx == len(self.word):
            return True if tol >= 0 else False

        if tol < 0: return False

        res = False
        for ch in node.children:
            res |= self._dfs(idx+1, node.children[ch], 
                             tol if self.word[idx] == ch else tol - 1)
            if res: return res

        return res

class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:

        T = Trie()
        for w in dictionary:
            T.insert(w)

        ans = []
        for w in queries:
            if T.search(w):
                ans.append(w)

        return ans

queries, dictionary = ["yes"], ["not"]
queries, dictionary = ["word","note","ants","wood"], ["wood","joke","moat"]

Solution().twoEditWords(queries, dictionary)