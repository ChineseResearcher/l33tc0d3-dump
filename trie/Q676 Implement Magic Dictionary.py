# trie - medium
class TrieNode:
    def __init__(self):
        # Each node has a dictionary of children
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def _dfs_check(self, currNode, diff_cnt, match_idx, newWord):

        if diff_cnt > 1:
            return False
        
        # must be exactly differ by 1 char and of the same length
        if currNode.is_end_of_word and match_idx == len(newWord):
            return True if diff_cnt == 1 else False

        # curr. trie word not exhausted but newWord has been exhausted (i.e. diff in length)
        if currNode.children and match_idx == len(newWord):
            return False
        
        res = False
        for child in currNode.children:
            if newWord[match_idx] == child:
                res = (res or self._dfs_check(currNode.children[child], diff_cnt, match_idx+1, newWord))
            else:
                res = (res or self._dfs_check(currNode.children[child], diff_cnt+1, match_idx+1, newWord))

        return res

    def insert(self, word):
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]

        curr.is_end_of_word = True

    def canReplace(self, newWord):
        # check if the new word differs from any current words in Trie by exactly only one character
        return self._dfs_check(self.root, 0, 0, newWord)

class MagicDictionary:

    def __init__(self):
        self.t = Trie()
        
    def buildDict(self, dictionary) -> None:
        for word in dictionary:
            self.t.insert(word)

    def search(self, searchWord: str) -> bool:
        return self.t.canReplace(searchWord)
    
obj = MagicDictionary()

commands = ["buildDict", "search", "search", "search", "search"]
arguments = [[["hello", "leetcode"]], ["hello"], ["hhllo"], ["hell"], ["leetcoded"]]

commands = ["buildDict", "search", "search", "search", "search", "search", "search", "search", "search"]
arguments = [[["a","b"]], ["a"], ["b"], ["c"], ["d"], ["e"], ["f"], ["ab"], ["ba"]]

commands = ["buildDict", "search", "search", "search", "search", "search", "search", "search", "search", "search"]
arguments = [[["a","b","ab"]], ["a"], ["b"], ["c"], ["d"], ["e"], ["f"], ["ab"], ["ba"], ["abc"]]

for command, args in zip(commands, arguments):
    # Use getattr to dynamically call the method by its name
    func = getattr(obj, command)
    print('Calling Command: ', command, f' With Arguments: {args}' if args else '')
    print(func(*args))