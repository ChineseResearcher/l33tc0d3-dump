# string - medium
class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends == 1:
            return word

        n = len(word)
        # notice that for k friends Alice hosts, the max. length
        # of a single partition can be at most n-k+1
        # think of a fixed size sliding window and we try to find the best string
        l = n-numFriends+1

        ans = word[:l]
        for i in range(1, n):
            
            if word[i:i+l] > ans:
                ans = word[i:i+l]

        return ans
    
word, numFriends = "dbca", 2
word, numFriends = "gggg", 4
word, numFriends = "aann", 2
word, numFriends = "gh", 1

Solution().answerString(word, numFriends)