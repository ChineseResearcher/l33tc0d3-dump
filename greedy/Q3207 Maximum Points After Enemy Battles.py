# greedy - medium
class Solution:
    def maximumPoints(self, enemyEnergies, currentEnergy):
        # the greedy strategy is to always perform op1 on the enemy
        # w/ the lowest energy and get points while our energy could last

        # whenever our energy runs out to even op1 on the min. enemy
        # we would start marking (op2) on other enemies to gain energy
        minEnemy = min(enemyEnergies)
        enemyEnergies.remove(minEnemy)

        # edge case: our energy is smaller than the min. enemy to begin
        if currentEnergy < minEnemy: return 0

        idx, e, p = 0, currentEnergy, 0
        while idx < len(enemyEnergies):

            # exhaust op1 on min. enemy
            op1_cnt = e // minEnemy
            p += op1_cnt
            e -= op1_cnt * minEnemy

            e += enemyEnergies[idx]
            # we move the idx to indicate enemy has been used (marked)
            idx += 1

        # use up all remaining energy
        p += e // minEnemy
        return p
    
enemyEnergies, currentEnergy = [3,2,2], 2
enemyEnergies, currentEnergy = [5,2], 2

Solution().maximumPoints(enemyEnergies, currentEnergy)