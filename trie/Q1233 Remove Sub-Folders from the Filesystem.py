# trie - medium
class TrieNode:
    def __init__(self):
        # Each node has a dictionary of children, its folder name
        # and a boolean flag indicating if it's the end of a path.
        self.children = {}
        self.is_end_of_path = False

# string trie
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, path_str):
        current = self.root
        path_folders = path_str.lstrip("/").split("/")
        for folder in path_folders:
            if folder not in current.children:
                current.children[folder] = TrieNode()
            current = current.children[folder]
        current.is_end_of_path = True

class Solution:
    def recursiveTrieVisit(self, currNode, path):
        if path and currNode.is_end_of_path:
            reducedPath = '/'+'/'.join(path)
            self.ans.append(reducedPath)
            return

        for k,v in currNode.children.items():
            self.recursiveTrieVisit(v, path+[k])

    def removeSubfolders(self, folder):
        trie = Trie()
        for f in folder:
            trie.insert(f)

        self.ans = []
        self.recursiveTrieVisit(trie.root, [])
        return self.ans
    
folder = ["/a","/a/b","/c/d","/c/d/e","/c/f"]
folder = ["/a","/a/b/c","/a/b/d"]
folder = ["/a/b/c","/a/b/ca","/a/b/d"]
folder = ["/abc/de","/abc/dee","/abc/def","/abc/def/gh","/abc/def/ghi","/abc/def/ghij","/abc/def/ghijk","/abc/dez"]

Solution().removeSubfolders(folder)