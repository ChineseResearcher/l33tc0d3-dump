# trie - hard
class TrieNode:
    def __init__(self):
        # Each node has a dictionary of children
        self.children = {}
        self.is_end_of_word = False

class Trie:

    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]

        curr.is_end_of_word = True

    def search(self, word) -> bool:
        curr = self.root
        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        
        return True if curr.is_end_of_word else False

    def startsWith(self, prefix) -> bool:
        curr = self.root
        for char in prefix:
            if char not in curr.children:
                return False
            curr = curr.children[char]

        return True

    def remove(self, word) -> bool:
        # guaranteed a word to be removed exists in the first place

        def _remove(node, word, depth):
            if depth == len(word):
                node.is_end_of_word = False
                return len(node.children) == 0  # If no children, signal deletion
            
            char = word[depth]
            if _remove(node.children[char], word, depth + 1):
                del node.children[char]
                # we don't want to remove the node entirely if there's some other
                # shorter words in the path: e.g. remove 'oaa' when 'oa' is present
                return len(node.children) == 0 and not node.is_end_of_word
        
        return _remove(self.root, word, 0)

class Solution:
    def recursive_word_form(self, seq, visited, r, c):

        if self.desiredWords.search(seq):
            # a desired word can be formed thru. multiple board routes
            self.ans.add(''.join(seq))
            # a critical operation to optimise to remove this desired word
            # once it has been confirmed to form-able
            self.desiredWords.remove(seq)

        # any desired words would have at most length 10
        if len(seq) >= 10: return
        
        # explore cardinal directions
        # Note: as we traverse the board, ensure we do early stopping
        # if the curr. word seq is not the prefix of any desired words

        # east
        if c+1 < self.n and (r, c+1) not in visited:
            seq.append(self.board[r][c+1])
            if self.desiredWords.startsWith(seq):
                visited.add((r,c+1))
                self.recursive_word_form(seq, visited, r, c+1)
                visited.discard((r,c+1))
            seq.pop()

        # west
        if c-1 >= 0 and (r, c-1) not in visited:
            seq.append(self.board[r][c-1])
            if self.desiredWords.startsWith(seq):
                visited.add((r,c-1))
                self.recursive_word_form(seq, visited, r, c-1)
                visited.discard((r,c-1))
            seq.pop()

        # north
        if r-1 >= 0 and (r-1, c) not in visited:
            seq.append(self.board[r-1][c])
            if self.desiredWords.startsWith(seq):
                visited.add((r-1,c))
                self.recursive_word_form(seq, visited, r-1, c)
                visited.discard((r-1,c))
            seq.pop()

        # south
        if r+1 < self.m and (r+1, c) not in visited:
            seq.append(self.board[r+1][c])
            if self.desiredWords.startsWith(seq):
                visited.add((r+1,c))
                self.recursive_word_form(seq, visited, r+1, c)
                visited.discard((r+1,c))
            seq.pop()

    def findWords(self, board, words):
        self.desiredWords = Trie()
        for w in words:
            self.desiredWords.insert(w)

        self.ans = set()
        self.m, self.n = len(board), len(board[0])
        self.board = board

        # traverse the board and call recursive_word_form from every cell
        for r in range(self.m):
            for c in range(self.n):
                self.recursive_word_form([self.board[r][c]], set(((r,c),)), r, c)

        return list(self.ans)
    
board, words = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], ["oath","pea","eat","rain"]
board, words = [["a","b"],["c","d"]], ["abcb"]
board, words = [["a"]], ["a"]
board, words = [["o","a","b","n"],["o","t","a","e"],["a","h","k","r"],["a","f","l","v"]], ["oa","oaa"]

Solution().findWords(board, words)