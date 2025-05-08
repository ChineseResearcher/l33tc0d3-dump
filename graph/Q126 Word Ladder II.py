# graph - hard
from typing import List
from collections import deque
class Solution:
    # track formation seq. and the set of elements in formation
    def backtrack(self, fm):
        # with the pruned graph after the modified BFS
        # our traversal from endWord to beginWord is shortest and acyclic

        if fm[-1] == self.beginWord:
            # reverse as we are starting from endWord
            self.ans.append(fm[::-1])
            return
        
        for p in self.parents[fm[-1]]:
                
            fm.append(p)    
            self.backtrack(fm)
            # backtrack
            fm.pop()
    

    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        # word ladder II is an extension of I as it asks for all possible
        # shortest transformation(s) if any exists at all, we can use the solution
        # of word ladder I to first check if there's a transformation then proceed to backtrack

        # as pointed out in sample TC, if endWord not in wordList, return 0
        if endWord not in wordList: return []

        # it is possible to construct "word edges" by mutating each word given
        # first prepare the universe of relevant letters that appear in beginWord & wordList
        letters = set(''.join(wordList + [beginWord]))

        # create a set copy of wordList for efficient lookup
        wordSet = set(wordList + [beginWord])
        wordEdge = {w:set() for w in wordSet}

        # process each word in wordSet and mutate it
        for w in wordSet:
            # single word is maximally 10 char. long, ~ O(1)
            for idx, char in enumerate(w):
                # maximally 26 alphabets, ~ O(1)
                for alphabet in letters:

                    if alphabet != char:
                        new_word = w[:idx] + alphabet + w[(idx+1):]
                        if new_word in wordSet:
                            wordEdge[w].add(new_word)
                            wordEdge[new_word].add(w)

        distance = {w: float('inf') for w in wordSet}
        parents = {w: set() for w in wordSet}

        # init. distance of beginWord to 0
        distance[beginWord] = 0

        # modified BFS that relies on distance checking instead of visited set
        # initiate our bfs_queue with the beginWord, with distance init. to 0
        bfs_queue = deque([[beginWord, 0]])
        while bfs_queue:

            currWord, currDist = bfs_queue.popleft()
            for neighbour in wordEdge[currWord]:

                if currDist + 1 < distance[neighbour]:
                    distance[neighbour] = currDist + 1
                    parents[neighbour] = set([currWord])
                    
                    bfs_queue.append([neighbour, currDist + 1])
                    
                elif currDist + 1 == distance[neighbour]:
                    if currWord not in parents[neighbour]:
                        parents[neighbour].add(currWord)
                        bfs_queue.append([neighbour, currDist + 1])
   
        # if no transformation found, stop
        if not parents[endWord]:
            return []

        self.beginWord, self.parents = beginWord, parents
        self.ans = []

        self.backtrack([endWord])
        return self.ans
    
# Wrong submissions are all TLE cases, too long to include
beginWord, endWord, wordList = "hit", "cog", ["hot","dot","dog","lot","log","cog"]

Solution().findLadders(beginWord, endWord, wordList)