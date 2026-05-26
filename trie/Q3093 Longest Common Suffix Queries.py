# trie - hard
from typing import List
class TrieNode:
    def __init__(self):
        self.children = {}   # maps char -> TrieNode
        self.pi = -1         # parent index of the suffix

# suffix Trie
class Trie:
    def __init__(self, wordsContainer: List[str]):
        self.root = TrieNode()
        self.wordsContainer = wordsContainer

    def insert(self, word: str, pi: int, l: int) -> None:
        node = self.root
        word = word[::-1] # insert suffix

        for ch in [''] + list(word):
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]

            if node.pi == -1:
                node.pi = pi
            else:
                # replace curr. parent string if more optimal
                cpi = node.pi
                if l < len(self.wordsContainer[cpi]):
                    node.pi = pi

    def query(self, suffix: str) -> int:
        node = self.root
        suffix = suffix[::-1]

        curr_ans = None
        for ch in [''] + list(suffix):
            # maximum suffix matched
            if ch not in node.children:
                break
            node = node.children[ch]
            if node.pi != -1:
                curr_ans = node.pi

        return curr_ans

class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:

        # key ideas:
        # 1) sum of lengths of all words in wordsContainer <= 5 * 1e5
        # 2) we can exploit the constraint in (1) and enumerate all suffixes
        # that can be generated, and use a hash table to maintain the optimal index
        # 3) hash table will MLE, optimise by using a word Trie
        T = Trie(wordsContainer)

        for i, w in enumerate(wordsContainer):
            T.insert(w, i, len(w))

        ans = []
        for q in wordsQuery:
            ans.append(T.query(q))

        return ans
    
wordsContainer, wordsQuery = ["abcd","bcd","xbcd"], ["cd","bcd","xyz"]
wordsContainer, wordsQuery = ["abcdefgh","poiuygh","ghghgh"], ["gh","acbfgh","acbfegh"]

Solution().stringIndices(wordsContainer, wordsQuery)