# trie - hard
class Solution:
    def findNextNode(self, digit_lvl, curr_k, path):
        
        str_n = str(self.n)
        curr_k_hist = []
        
        if digit_lvl == 0:
            start_i = 1
        else:
            start_i = 0

        isSubPath = (''.join([str(p) for p in path]) == str_n[:digit_lvl])
            
        for i in range(start_i, 10):
            curr_k_hist.append(curr_k)
            if curr_k <= 0:
                nextNode = i - 1
                return nextNode, curr_k_hist[-2]
                    
            if digit_lvl == 0 or isSubPath:
                if i < int(str_n[digit_lvl]):
                    curr_k -= int('1'*(self.digit_len-digit_lvl)) 
                elif i == int(str_n[digit_lvl]):
                    k1 = int(str_n[digit_lvl:])-int(str(i)+'0'*(self.digit_len-digit_lvl-1))
                    k2 = 1
                    k3 = int('1'*(self.digit_len-digit_lvl-1))
                    curr_k -= (k1+k2+k3)
                else:
                    curr_k -= int('1'*(self.digit_len-digit_lvl-1))
                    
            elif digit_lvl > 0 and not isSubPath:
                curr_k -= int('1'*(self.digit_len-digit_lvl)) 
                
        return i, curr_k_hist[-1]

    def recursiveTrieSearch(self, digit_lvl, curr_k, path):
        
        if digit_lvl == self.digit_len - 1:
            if self.digit_len == 1:
                path.append(curr_k)
            else:
                path.append(curr_k-1)
            return path
        
        nextNode, nextNodeK = self.findNextNode(digit_lvl, curr_k, path)
        path.append(nextNode)
        
        if nextNodeK == 1:
            return path
        
        if digit_lvl == 0 and path[0] > int(str(self.n)[0]):
            digit_lvl += 2
        else:
            digit_lvl += 1
            
        # print(f'moving to digit lvl: {digit_lvl} at node: {nextNode} for {nextNodeK-1}-th element')
        # call to next digit level with updated k
        return self.recursiveTrieSearch(digit_lvl, nextNodeK-1, path)

    def findKthNumber(self, n: int, k: int) -> int:
        # concept used is a trie to organise lexicographical numbers
        # but no trie class was constructed

        self.n = n
        self.digit_len = len(str(n))

        answer = self.recursiveTrieSearch(0, k, [])
        return int(''.join([str(x) for x in answer]))
    
n, k = 13, 2
n, k = 1, 1
n, k = 2, 1
n, k = 2, 2
n, k = 10000, 10000
n, k = 4897764, 3510563
n, k = 4089173, 3098723

Solution().findKthNumber(n, k)