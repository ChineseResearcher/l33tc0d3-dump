# sliding window - hard
from collections import Counter, deque, defaultdict
class Solution:
    def merger(self, words):

        freq = defaultdict(int)
        for w in words:

            # we want to identify word string made up of one single char.
            if len(set(w)) == 1:
                freq[w[0]] += len(w)

        # e.g. 'a','aa','aaa' gets merged into one word string 'aaaaaa'
        return [char * length for char, length in freq.items()]

    def findSubstring(self, s: str, words):

        # words that are made up of purely one single char.
        # e.g. ['a','aa','aaa'] can be merged into just one single string
        if len(set(''.join(words))) == 1:
            words = self.merger(words)

        n, m = len(s), len(words)
        # a concatenated string is defined as the combination of
        # all words available in any permuatation, note that the words
        # may not be unique, and it's given they are all of same length

        word_freq = Counter(words)
        # an observation is that for a substr. to be validated as
        # a concatenated string, it must be of length: word_length x number of words

        # define word length, constant throughout
        wl = len(words[0])

        # here we define a qualifying length (ql) of any concatenated string
        ql = m * wl

        # handle edge case where it's impossible to have a concatenated substring
        if ql > n: return []

        # define an auxliary cache arr. that stores unjoined
        # characters read in, its size is capped at len(words[0])
        window = deque([])

        # we need to keep track of words and their freq. in the slided window
        window_freq = {k: 0 for k, _ in word_freq.items()}

        cache, ans = [], []
        # this O(n*m) construction actually gets AC, albeit super slow...
        for r in range(n):

            window.append(s[r])
            if len(window) == ql:

                for char in window:
                    cache.append(char)
                    # process the cache whenever it reaches word length
                    if len(cache) == wl:
                        currWord = ''.join(cache)
                        if currWord in word_freq:
                            window_freq[currWord] += 1
                        cache = []

                # validate if the curr. window is a concatenated string
                valid = True
                for k, v in window_freq.items():
                    # check against original freq.
                    if v != word_freq[k]:
                        valid = False
                        break

                if valid: ans.append(r-(ql-1))
                # reset frequencies to 0
                for k in window_freq.keys():
                    window_freq[k] = 0

                # discard left item
                window.popleft()

        return ans
    
s, words = "barfoothefoobarman", ["foo","bar"]
s, words = "barfoobarfoobar", ["foo","bar"]
s, words = "wordgoodgoodgoodbestword", ["word","good","best","word"]
s, words = "lingmindraboofooowingdingbarrwingmonkeypoundcake", ["fooo","barr","wing","ding","wing"]
s, words = "aaaaaaaaaaaaaa", ["aa","aa"]
s, words = "ababaab", ["ab","ba","ba"]

Solution().findSubstring(s, words)