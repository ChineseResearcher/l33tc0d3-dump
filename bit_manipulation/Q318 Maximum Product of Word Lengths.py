# bit manipulation - medium
import string
class Solution:
    def maxProduct(self, words):
        
        n = len(words)
        # we could encode all the alphabets as bits according to
        # its position in the alphabetical order
        alpha_bit = {char: idx for idx, char in enumerate(string.ascii_lowercase)}

        bw = []
        for idx, w in enumerate(words):

            bitWord = 0
            for char in w:
                if bitWord & (1 << alpha_bit[char]) == 0:
                    bitWord |= (1 << alpha_bit[char])

            bw.append(bitWord)

        # input of words of at most 1000, we can find the max. product wordLen in O(n^2) time
        ans = 0
        for i in range(n-1):
            for j in range(i+1, n):
                # the key to validate if two words share common letters
                # from a bit perspective is to compare its OR and XOR
                if bw[i] | bw[j] == bw[i] ^ bw[j]:
                    ans = max(ans, len(words[i]) * len(words[j]))

        return ans
    
words = ["abcw","baz","foo","bar","xtfn","abcdef"]
words = ["a","ab","abc","d","cd","bcd","abcd"]
words = ["a","aa","aaa","aaaa"]

Solution().maxProduct(words)