# dp - medium
class Solution:
    def recursive_cut(self, first_v, last_v):
    
        # if we encounter the minimal polygon (triangle)
        if last_v - first_v == 2:
            return self.values[first_v] * self.values[first_v+1] * self.values[last_v]
        
        if (first_v, last_v) in self.dp: return self.dp[(first_v, last_v)]
        
        # it is a big challenge to realise that in order
        # to achieve optimal time complexity we have need to always
        # assume first & last vertice are involved in the same triangle
        currAns, fixedTrig = float('inf'), self.values[first_v] * self.values[last_v]
        # then we explore the possible third vertice
        for idx in range(first_v+1, last_v):
            
            # no left problem
            if idx == first_v + 1:
                currAns = min(currAns, fixedTrig * self.values[idx] + self.recursive_cut(idx, last_v))
            
            elif first_v + 1 < idx < last_v - 1:
                currAns = min(currAns, fixedTrig * self.values[idx] + \
                            self.recursive_cut(first_v, idx) + self.recursive_cut(idx, last_v))
            
            # no right problem
            elif idx == last_v - 1:
                currAns = min(currAns, fixedTrig * self.values[idx] + self.recursive_cut(first_v, idx))
                
        self.dp[(first_v, last_v)] = currAns
        return currAns

    def minScoreTriangulation(self, values):
        self.values = values
        # our dp stores 2-D states: <start_vertice, end_vertice>
        # in clockwise fashion, e.g. <0,5> implies the subproblem concerning
        # polygon with vertices going from v0 to v5
        self.dp = dict()

        return self.recursive_cut(0, len(self.values)-1)
    
values = [1,2,3]
values = [3,7,4,5]
values = [1,3,1,4,1,5]

Solution().minScoreTriangulation(values)