# backtracking - medium
class Solution:
    def recursive_prod_sum(self, int_str, start_idx, partition):

        if start_idx == len(int_str):
            if sum([int(x) for x in partition]) == int(int(int_str) ** 0.5):
                return True
            else:
                return False

        currRes = False
        for i in range(start_idx, len(int_str)):

            currNum = int_str[start_idx:(i+1)]
            partition.append(currNum)
            currRes = (currRes or self.recursive_prod_sum(int_str, i+1, partition))
            partition.pop() # backtracking
        
        return currRes

    def punishmentNumber(self, n: int) -> int:
        candidates = []
        for num in range(1, n+1):

            # it turns out that there's a mathematical optimisation trick to this
            if num % 9 == 0 or num % 9 == 1:
            
                if self.recursive_prod_sum(str(num ** 2), 0, []):
                    candidates.append(num ** 2)

        return sum(candidates)
    
n = 10
n = 37

Solution().punishmentNumber(n)