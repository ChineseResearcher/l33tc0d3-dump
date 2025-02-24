# trie - medium
class TrieNode:
    def __init__(self):
        # Each node has a dictionary of children
        # and a boolean flag indicating if it's the end of a word.
        self.children = {}
        self.is_end_of_word = False

# numerical trie
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, number):
        current = self.root
        for str_digit in str(number):
            if str_digit not in current.children:
                current.children[str_digit] = TrieNode()
            current = current.children[str_digit]
        current.is_end_of_word = True

    def lcp_length(self, number):
        current = self.root
        for i, str_digit in enumerate(str(number)):
            if str_digit not in current.children:
                return i
            current = current.children[str_digit]
        return len(str(number))

class Solution:
    def longestCommonPrefix(self, arr1, arr2):
        trie = Trie()
        for num in arr1:
            trie.insert(num)

        lcp = 0 # longest common prefix
        for num in arr2:
            lcp = max(lcp, trie.lcp_length(num))

        return lcp
    
arr1, arr2 = [1,10,100], [1000]
arr1, arr2 = [1,2,3], [4,4,4]
arr1, arr2 = [1,26], [22,2]

Solution().longestCommonPrefix(arr1, arr2)