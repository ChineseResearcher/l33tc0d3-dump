# simulation - hard
class Solution:
    def fullJustify(self, words, maxWidth):
        # our ans would be storing a series of line strings
        ans = []

        # maintain a pointer to the words
        idx = 0
        while idx < len(words):

            # for every new line processed, we have deductable spaces reset
            spaces = maxWidth

            # curr. line would occupy a nested arr.
            curr = []

            wordsLength = 0
            while True:

                curr.append(words[idx])
                # for every word, we need at least one space
                spaces -= len(words[idx]) + 1
                wordsLength += len(words[idx])

                # 1) if there's a next word and that it causes overflow
                # 2) or if we are at the last word
                # we would stop the curr. line 
                if (idx+1 < len(words) and len(words[idx+1]) > spaces) or \
                    idx == len(words) - 1:
                    break

                idx += 1

            # we are at the last line, just single spaces between words
            if idx+1 == len(words):
                # there can be tail spaces after stipulating one space 
                # between each char. for the last line
                tail_spaces = maxWidth - wordsLength - (len(curr)-1)
                res = ' '.join(curr) + tail_spaces * ' '
                ans.append(res)

            # for all lines before, spaces that cannot be evenly distributed
            # must be loaded more towards the left
            # e.g., if we have 7 spaces to be assigned for 2 breaks
            # the first break is assigned 4 spaces, followed by 3 spaces
            else:

                breaks = len(curr) - 1
                spaces = maxWidth - wordsLength
                # there's the edge case where curr. line only contains one word
                # i.e. we don't need to handle the spaces assignment between words
                if breaks == 0:
                    res = curr[0] + ' ' * spaces 
                else:
                    res = ''
                    for i, w in enumerate(curr):
                        res += w
                        # the spaces to be assigned to each break needs to be 
                        # computed dynamically depending on the # of breaks left (bl)
                        bl = len(curr)-i-1
                        if bl > 0:
                            if spaces % bl == 0:
                                res += ' ' * (spaces // bl)
                                spaces -= spaces // bl
                            else:
                                res += ' ' * (int(spaces / bl) + 1)
                                spaces -= (int(spaces / bl) + 1)

                ans.append(res)

            idx += 1

        return ans
    
words, maxWidth = ["This", "is", "an", "example", "of", "text", "justification."], 16
words, maxWidth = ["What","must","be","acknowledgment","shall","be"], 16
words, maxWidth = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], 20
words, maxWidth = ["ask","not","what","your","country","can","do","for","you","ask","what","you","can","do","for","your","country"], 16
words, maxWidth = ["Give","me","my","Romeo;","and,","when","he","shall","die,","Take","him","and","cut","him","out","in","little","stars,","And","he","will","make","the","face","of","heaven","so","fine","That","all","the","world","will","be","in","love","with","night","And","pay","no","worship","to","the","garish","sun."], 25

Solution().fullJustify(words, maxWidth)