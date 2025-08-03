# sliding window - medium
class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        
        n = len(answerKey)
        # define a helper function maxWindow that calculates the maximum number of consecutive
        # answers for a given character c ('T' or 'F')
        def maxWindow(c):

            ans = 0
            replaced = 0 # keep track of number of replacements operated
            left = 0
            for right in range(n):
                if answerKey[right] != c: 
                    replaced += 1
                
                # if k replacements have been exceeded, we want to shift the sliding window
                # such that the left is to the right of the first replacement
                if replaced > k:  
                    while answerKey[left] == c:  
                        left += 1
                    left += 1  
                    replaced -= 1  

                # ans gets updated regardless of exceeding k replacements or not
                ans = max(ans, right - left + 1) 

            return ans
        
        return max(maxWindow('T'), maxWindow('F'))
    
answerKey, k = "TTFTTFTT", 1
answerKey, k =  "TFFT", 1
answerKey, k = "TTFTTFTT", 1
answerKey, k = "FFTFTTTFFF", 1
answerKey, k = "FFFTTFTTFT", 3

Solution().maxConsecutiveAnswers(answerKey, k)
