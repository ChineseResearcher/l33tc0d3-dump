# sorting - medium
class Solution:
    def groupAnagrams(self, strs):
        anagram_dict = dict()
        
        # This would make it O(N^2*logN)? It didn't TLE.
        for gram in strs:
            sortedGram = ''.join(sorted(gram)) # O(N*logN)
            
            if anagram_dict.get(sortedGram) is not None:
                anagram_dict[sortedGram].append(gram)
            else:
                anagram_dict[sortedGram] = [gram]

        return [list(v) for _, v in anagram_dict.items()]

strs = [""]
strs = ["a"]
strs = ["eat","tea","tan","ate","nat","bat"]

Solution().groupAnagrams(strs)