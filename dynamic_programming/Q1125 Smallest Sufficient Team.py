# dp - hard
from functools import cache
class Solution:
    def smallestSufficientTeam(self, req_skills: list[str], people: list[list[str]]) -> list[int]:

        m, n = len(req_skills), len(people)
        # key ideas:
        # 1) classic knapsack DP + bitmask managing acquired skills of the team
        # 2) track the min. size of the team as we process "people"
        # 3) encode each person's skillset using a bitmask with i-th bit set if
        # req_skills[i] is present in the skillset

        skill_code = {req_skills[i]: i for i in range(m)}
        p = []
        for i in range(n):
            b = 0
            for skill in people[i]:
                b |= (1 << skill_code[skill])
            p.append(b)

        # suffix accumulative array on people's skills
        sf_p = [0] * n
        sf_p[-1] = p[-1]
        for i in range(n - 2, -1, -1):
            sf_p[i] = p[i] | sf_p[i + 1]

        # state to indicate all skills attained
        T = pow(2, m) - 1

        # worst answer: use all people
        W = pow(2, n) - 1 

        @cache
        def f(i: int, team_skill: int) -> int:

            if team_skill == T:
                return 0

            # prune early when people[i...n] will not complete the required
            if i == n or (i < n and team_skill | sf_p[i] != T):
                return W

            # knapsack
            skip = f(i + 1, team_skill)
            take = f(i + 1, team_skill | p[i]) | (1 << i)

            # favour smaller team size
            if skip.bit_count() < take.bit_count():
                return skip
            else:
                return take

        ans, team = [], f(0, 0)
        for i in range(team.bit_length()):
            if team & (1 << i):
                ans.append(i)

        return ans

req_skills, people = ["java","nodejs","reactjs"], [["java"],["nodejs"],["nodejs","reactjs"]]

Solution().smallestSufficientTeam(req_skills, people)