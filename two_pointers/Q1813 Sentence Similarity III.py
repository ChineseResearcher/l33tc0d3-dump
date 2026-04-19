# two pointers - medium
class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:

        if len(sentence1) > len(sentence2):
            sentence1, sentence2 = sentence2, sentence1

        s1, s2 = sentence1.split(' '), sentence2.split(' ')
        m, n = len(s1), len(s2)
        # key ideas:
        # 1) assign the shorter sentence to sentence1, the longer to sentence2
        # 2) match as far as possible from left end, followed by from right end
        # 3) if all words in sentence1 can be matched, it is possible to match after insertion
        i, j, matchCnt = 0, m-1, 0

        while i < m:
            if s1[i] != s2[i]:
                break
            matchCnt += 1
            i += 1

        while j >= i:
            if s1[j] != s2[-(m-j)]:
                break
            matchCnt += 1
            j -= 1

        return matchCnt == m

sentence1, sentence2 = "A", "a A b A"
sentence1, sentence2 = "pp ZM ZJ lE B", "ZM"
sentence1, sentence2 = "of", "A lot of words"
sentence1, sentence2 = "Eating right now", "Eating"
sentence1, sentence2 = "My name is Haley", "My Haley"
sentence1, sentence2 = "eTUny i b R UFKQJ EZx JBJ Q xXz", "eTUny i R EZx JBJ xXz"

Solution().areSentencesSimilar(sentence1, sentence2)