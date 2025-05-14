# prefix sum - medium
class Solution:
    def vowelStrings(self, words, queries):
        n = len(words)

        vowel_str_cnt = 0
        # initialize a prefix sum array storing the count of vowel strings
        pf_sum = [] 
        for i in range(n):

            word = words[i]
            # check if a string starts and ends with a vowel
            if word[0] in 'aeiou' and word[-1] in 'aeiou':
                vowel_str_cnt += 1

            pf_sum.append(vowel_str_cnt)


        ans = []
        for i, j in queries:

            if i == j:
                res = 1 if words[i][0] in 'aeiou' and words[i][-1] in 'aeiou' else 0
            
            # j > i
            else:
                res = pf_sum[j] - pf_sum[i-1] if i > 0 else pf_sum[j]

            ans.append(res)

        return ans
    
words, queries = ["aba","bcb","ece","aa","e"], [[0,2],[1,4],[1,1]]
words, queries = ["a","e","i"], [[0,2],[0,1],[2,2]]

Solution().vowelStrings(words, queries)