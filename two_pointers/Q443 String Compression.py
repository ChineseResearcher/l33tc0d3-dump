# two pointers - medium
class Solution:
    def compress(self, chars):
        n = len(chars)

        # maintain two pointers
        # 1) curr_cnt to track the length of curr. running character seq.
        # 2) fill_pos 
        curr_cnt, fill_pos = 1, 0

        # result is supposed to be modified in-place
        for i in range(1, n):

            if chars[i] != chars[i-1]:
                chars[fill_pos] = chars[i-1]
                fill_pos += 1

                if curr_cnt > 1:
                    for digit in str(curr_cnt):
                        chars[fill_pos] = digit
                        fill_pos += 1

                # reset
                curr_cnt = 1

            else:
                curr_cnt += 1

        # collect last
        chars[fill_pos] = chars[-1]
        fill_pos += 1

        if curr_cnt > 1:
            for digit in str(curr_cnt):
                chars[fill_pos] = digit
                fill_pos += 1

        return fill_pos
    
chars = ["a"]
chars = ["a","a","b","b","c","c","c"]
chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
chars = ["a","a","a","b","b","a","a"]
chars = ["a","b","c"]
chars = ["a","a","a","a","a","b"]

Solution().compress(chars)