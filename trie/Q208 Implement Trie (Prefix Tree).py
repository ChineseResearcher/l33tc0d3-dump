# trie - medium
class TrieNode:
    def __init__(self):
        # Each node has a dictionary of children
        self.children = {}
        self.is_end_of_word = False

class Trie:

    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]

        curr.is_end_of_word = True

    def search(self, word: str) -> bool:
        curr = self.root
        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        
        return True if curr.is_end_of_word else False

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for char in prefix:
            if char not in curr.children:
                return False
            curr = curr.children[char]

        return True
    
obj = Trie()

commands = ["insert", "search", "search", "startsWith", "insert", "search"]
arguments = [["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]

for command, args in zip(commands, arguments):
    # Use getattr to dynamically call the method by its name
    func = getattr(obj, command)
    print('Calling Command: ', command, f' With Arguments: {args}' if args else '')
    print(func(*args))