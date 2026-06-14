# string - medium
from typing import List
class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        
        # key ideas:
        # 1) enumerate all possible prefixes of words in sentences
        # 2) check membership by referencing hashset of dictionary
        d = set(dictionary)
        
        # get the max. length of dictionary roots
        L = max([len(x) for x in dictionary])

        ans = []
        for x in sentence.split(' '):
            hasRoot = False
            for i in range(1, min(L, len(x))+1):
                pf = x[:i]
                if pf in d:
                    ans.append(pf)
                    hasRoot = True
                    break
            if not hasRoot: ans.append(x)

        return ' '.join(ans)

dictionary, sentence = ["a","b","c"], "aadsfasf absbs bbab cadsfafs"
dictionary, sentence = ["cat","bat","rat"], "the cattle was rattled by the battery"

Solution().replaceWords(dictionary, sentence)