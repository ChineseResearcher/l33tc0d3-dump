# counting - medium
from collections import Counter
class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        # perform a freq. count of alphabets in s
        freq_d = Counter(s)

        # greedily assigns the odd-count alphabet as palindromes first
        # if there are any even-count alphabet, we can always form any
        # combinations to satisfy the k remaining 
        odd_freq_cnt = len([alphabet for alphabet, freq in freq_d.items() if freq % 2 == 1])
        even_freq_cnt = len(freq_d) - odd_freq_cnt

        # overloading
        if odd_freq_cnt > k:
            return False

        # note that if odd_freq_cnt == k is always valid
        # e.g. s = "messi", k = 3
        # after odd-cnt palindromes "m", "e", "i" formed, 
        # the remaining even-cnt palindrome "ss" can be bound to any above

        # e.g. s = 'cr', k = 7 -> insufficient even-cnt palindromes 
        if odd_freq_cnt < k and even_freq_cnt < k-odd_freq_cnt:

            for alphabet, freq in freq_d.items():
                # for both odd-/even-cnt alphabet, it can be broken down into
                # length-1 palindromes according to its freq
                if freq % 2 == 1:
                    odd_freq_cnt += freq
                    odd_freq_cnt -= 1
                
                if freq % 2 == 0:
                    odd_freq_cnt += freq
                    even_freq_cnt -= 1

                if odd_freq_cnt + even_freq_cnt >= k:
                    return True

            return False

        return True
    
s, k = "annabelle", 2
s, k = "leetcode", 3
s, k = "qlkzenwmmnpkopu", 15
s, k = "putmeinatrouble", 16
s, k = "jsautfnlcmwqpzycehdulmdencthhlzsnijd", 35
s, k = 'aaa', 2

Solution().canConstruct(s, k)