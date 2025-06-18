# number theory - hard
class Solution:
    def kMirror(self, k: int, n: int) -> int:

        def rebase(num:int, k:int):

            res = []
            # given a 10-based number, convert it to k-based
            curr = num

            while curr > 0:

                res.append(str(curr % k))
                curr //= k

            return ''.join(res[::-1])

        def isPalindrome(numStr:str):
            return (numStr == numStr[::-1])

        # while loop to generate ordered palidromes until 
        # first n k-mirror numbers are found
        i, pLen, ans = 0, 1, 0
        while i < n:

            if pLen == 1:
                for num in range(1, 10):
                    
                    pld_k = rebase(num, k)
                    if isPalindrome(pld_k):
                        ans += num
                        i += 1
                    if i >= n:
                        break

                pLen += 1

            else:
                
                # construct baseStr
                bs = str(1) + (pLen // 2 - 1 if pLen % 2 == 0 else pLen // 2) * '0' # consider parity

                cap, num = int('9' * len(bs)), int(bs)
                while num <= cap:
                    
                    ns = str(num)
                    # get mirrored length & generate palindrome
                    ml = len(ns) if pLen % 2 == 0 else len(ns) - 1
                    pld = int(ns[:ml] + ns[ml:] + ns[:ml][::-1])

                    # get k-based palindrome
                    pld_k = rebase(pld, k)
                    if isPalindrome(pld_k):
                        ans += pld
                        i += 1
                    if i >= n:
                        break

                    num += 1    

                pLen += 1

        return ans
    
k, n = 2, 5
k, n = 3, 7
k, n = 7, 17
k, n = 7, 30

Solution().kMirror(k, n)