# sliding window - medium
class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:

        n = len(answerKey)
        fmax = lambda a, b: a if a > b else b
        fmin = lambda a, b: a if a < b else b
        # key ideas:
        # 1) use a sliding window to capture all subarrays where min(T, F) <= k
        # 2) find the largest length among those valid subarrays

        ans, l, T, F = 0, 0, 0, 0
        for r in range(n):

            if answerKey[r] == 'T':
                T += 1
            else:
                F += 1

            while l < r and fmin(T, F) > k:
                if answerKey[l] == 'T':
                    T -= 1
                else:
                    F -= 1
                l += 1

            if fmin(T, F) <= k:
                ans = fmax(ans, r-l+1)

        return ans
    
answerKey, k = "TFFT", 1
answerKey, k = "TTFTTFTT", 1
answerKey, k = "TTFTTFTT", 1
answerKey, k = "FFTFTTTFFF", 1
answerKey, k = "FFFTTFTTFT", 3

Solution().maxConsecutiveAnswers(answerKey, k)
