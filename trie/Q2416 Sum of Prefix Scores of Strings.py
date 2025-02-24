# trie - hard
class TrieNode:
    def __init__(self):
        # Each node has a dictionary of children
        # and a boolean flag indicating if it's the end of a word.
        self.children = {}
        self.is_end_of_word = False
        self.score = 0

# word trie
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
            current.score += 1
        current.is_end_of_word = True
            
    def get_score(self, word):
        # by design, a word to be scored is definitely in the trie
        current = self.root
        score = 0
        for char in word:
            current = current.children[char]
            score += current.score
        return score

class Solution:
    def sumPrefixScores(self, words):

        wordTrie = Trie()
        for w in words:
            wordTrie.insert(w)
            
        return [wordTrie.get_score(w) for w in words]

words = ["abc","ab","bc","b"]
words = ["abcd"]

Solution().sumPrefixScores(words)