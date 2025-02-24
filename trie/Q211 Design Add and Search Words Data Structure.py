# trie - medium
class TrieNode:
    def __init__(self):
        # Each node has a dictionary of children
        self.children = {}
        self.is_end_of_word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def _dfs(self, word, matchIdx, currNode):

        if matchIdx == len(word):
            return True if currNode.is_end_of_word else False
               
        toMatch = word[matchIdx]

        # early stop as soon as we fail to match one specific char
        if toMatch not in currNode.children and toMatch != '.':
            return False  

        curr_res = False
        if toMatch in currNode.children:
            curr_res = (curr_res or self._dfs(word, matchIdx+1, currNode.children[toMatch]))

        # only iterate through all children if it's a wildcard
        elif toMatch == '.':
            for char, nextNode in currNode.children.items():
                curr_res = (curr_res or self._dfs(word, matchIdx+1, nextNode))

        return curr_res 
    
    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:

            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]

        curr.is_end_of_word = True

    def search(self, word: str) -> bool:
        # word may contain wildcard characters "."
        # internally call another dfs function to match
        return self._dfs(word, 0, self.root)
    
obj = WordDictionary()

commands = ["addWord","addWord","addWord","search","search","search","search"]
arguments = [["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]

for command, args in zip(commands, arguments):
    # Use getattr to dynamically call the method by its name
    func = getattr(obj, command)
    print('Calling Command: ', command, f' With Arguments: {args}' if args else '')
    print(func(*args))