# two pointers - medium
class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:

        n = len(people)
        # key ideas:
        # 1) sorting + two pointers + greedy
        # 2) if we load two persons with total weight << limit, we under-utilise
        # the boat, or conversely, if the total weight >> limit, we give up on both persons
        # where in reality one of them might still be suitably paired with a small weight
        # 3) we then search from both min. and max. weight, to maximise the utilisation of 
        # every boat, so the combined weight is greedily close to limit 

        people.sort()
        
        l, r, ans = 0, n - 1, 0
        while True:
            
            if l >= r:
                ans += 1 if l == r else 0
                break
            
            if people[l] + people[r] <= limit:
                ans += 1
                l += 1
                r -= 1
            
            else:
                ans += 1
                r -= 1

        return ans

people, limit = [1,2], 3
people, limit = [3,5,3,4], 5
people, limit = [3,2,2,1], 3

Solution().numRescueBoats(people, limit)