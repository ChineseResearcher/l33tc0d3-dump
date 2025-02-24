# graph - hard
from collections import deque
class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        
        # as pointed out in sample TC, if endWord not in wordList, return 0
        if endWord not in wordList: return 0

        # it is possible to construct "word edges" by mutating each word given

        # first prepare the letters that appear in beginWord & wordList
        letters = set(''.join(wordList + ['beginWord']))

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

        # initiate our bfs_queue with the beginWord, with steps init. to 0
        bfs_queue = deque([[beginWord, 1]])

        # maintain visited
        visited = set([beginWord])

        ans = float('inf')
        while bfs_queue:

            currWord, currSteps = bfs_queue.popleft()
            if currWord == endWord:
                ans = min(ans, currSteps)

            for neighbour in wordEdge[currWord]:

                if neighbour not in visited:
                    bfs_queue.append([neighbour, currSteps+1])
                    visited.add(neighbour)

        return ans if ans < float('inf') else 0
    
beginWord, endWord, wordList = "hit", "cog", ["hot","dot","dog","lot","log","cog"]
beginWord, endWord, wordList = "hit", "cog", ["hot","dot","dog","lot","log"]

Solution().ladderLength(beginWord, endWord, wordList)