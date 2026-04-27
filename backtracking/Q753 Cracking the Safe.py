# backtracking - hard
class Solution:
    def crackSafe(self, n: int, k: int) -> str:

        # our visited states need to hit M to represent all-exploration
        M = pow(k, n)

        # our possible selection at each recursive step
        choice = list(map(str, [i for i in range(0, k)]))

        # visited = tried passwords of length n
        visited = set()

        ans = None
        def f(currStr:str) -> None:

            nonlocal visited, ans
            if len(visited) == M:
                ans = currStr

            for d in choice:
                if len(currStr) < n - 1:
                    _ = f(currStr + d)
                else:
                    pw = currStr[-(n-1):] + d if n - 1 > 0 else d
                    # the min. length str would not waste time going to visited
                    if pw not in visited:
                        visited.add(pw)
                        _ = f(currStr + d)

                # we only need to find one such min. length str.
                if ans != None:
                    return

            # roll-back visited status
            visited.discard(currStr[-n:])
            return

        _ = f('')
        return ans

n, k = 1, 2
n, k = 2, 2
n, k = 4, 6

Solution().crackSafe(n, k)