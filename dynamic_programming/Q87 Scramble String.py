# dp - hard
class Solution:
    def recursive_scramble(self, s1, s2):

        if s1 == s2:
            return True
        
        # if s1/s2 are length-1 string and they don't match
        # we need to terminate as we can't split them any further 
        if len(s1) == 1 and len(s2) == 1:
            return False
        
        if (s1, s2) in self.dp: 
            return self.dp[(s1, s2)]

        currAns = False
        # the splits available s.t. s[:i] and s[i:] are both not empty
        # note that it's guaranteed s1.length = s2.length
        for idx in range(1, len(s1)):

            # op1: no swapping
            # both subproblems must return True for curr. split to work
            noSwap = self.recursive_scramble(s1[:idx], s2[:idx]) and \
                     self.recursive_scramble(s1[idx:], s2[idx:])
            
            # op2: swapped
            # e.g. for s1 = 'abc', s2 = 'xyz', splitting at idx 1
            # would mean checking 'bc' against 'xy' and 'a' against 'z'
            swap = self.recursive_scramble(s1[:idx], s2[-idx:]) and \
                   self.recursive_scramble(s1[idx:], s2[:-idx])
            
            currAns = currAns or (noSwap or swap)
            # as long as we found one valid split, we early stop
            if currAns:
                break

        self.dp[(s1, s2)] = currAns
        return currAns

    def isScramble(self, s1: str, s2: str) -> bool:
        self.dp = dict()
        return self.recursive_scramble(s1, s2)
    
s1, s2 = "great", "rgeat"
s1, s2 = "abcde", "caebd"
s1, s2 = "a", "a"
# string is at most length 30
s1, s2 = "aaaaaaaaaabbbbbbbbbbcccccccccc", "abbbbbbbbbbccccccccccaaaaaaaaa"

Solution().isScramble(s1, s2)