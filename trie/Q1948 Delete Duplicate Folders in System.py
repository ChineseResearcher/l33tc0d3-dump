# trie - hard
from typing import List
from collections import defaultdict
class TrieNode:
    def __init__(self):
        self.children = {}
        # we would construct signature for every node's
        # subtree so that we could identify nodes' w/ identical subtrees for removals
        self.sig = None

class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.sig_cnt = defaultdict(int)
    
    def insert(self, path) -> None:
        node = self.root
        for folder in path:
            if folder not in node.children:
                node.children[folder] = TrieNode()
            node = node.children[folder]

    def build_sig(self) -> None:
        
        def dfs(node):

            if not node.children:
                node.sig = '_' # custom attribute for TrieNode class
                return
            
            # name, child_signature pairs
            res = []
            for name, child in node.children.items():
                dfs(child)
                res.append([name, '#', child.sig])

            # it is important to sort the pairs because we need to
            # ensure consistent hashing behaviour for identical subtrees.
            res.sort()
            res2 = []
            for pair in res:
                res2.append(''.join(pair))

            node.sig = '(' + ''.join(res2) + ')'
            # increment the count of subtree signature
            self.sig_cnt[node.sig] += 1
            return node.sig
        
        _ = dfs(self.root)

    def prune(self) -> None:

        def dfs(node):

            if self.sig_cnt[node.sig] > 1:
                return True
            
            for_del = []
            for name, child in node.children.items():
                if dfs(child):
                    for_del.append(name)

            for name in for_del:
                del node.children[name]

            return False
        
        _ = dfs(self.root)
    
    def collect_words(self) -> List[List[str]]:

        res = []
        def dfs(node, path):

            # for non-empty path, collect as one valid path
            if path:
                res.append(path[:])
            for ch, child in node.children.items():
                path.append(ch)
                dfs(child, path)
                path.pop()
        
        dfs(self.root, [])
        return res

class Solution:
    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        t = Trie()
        for path in paths:
            t.insert(path)

        t.build_sig()
        t.prune()
        return t.collect_words()
    
paths = [["a"],["c"],["d"],["a","b"],["c","b"],["d","a"]]
paths = [["a"],["c"],["a","b"],["c","b"],["a","b","x"],["a","b","x","y"],["w"],["w","y"]]
paths = [["a","b"],["c","d"],["c"],["a"]]

Solution().deleteDuplicateFolder(paths)