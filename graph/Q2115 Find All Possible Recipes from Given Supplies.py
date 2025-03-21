# graph - medium
from collections import defaultdict, deque
class Solution:
    def findAllRecipes(self, recipes, ingredients, supplies):

        n = len(recipes)
        # constraints info:
        # recipes.length, ingredients.length, supplies.length <= 100
        # each ingredients[i].length <= 100, and recipes/ingredients has same length

        # take note:
        # 1) recipies items can be an ingredient
        # 2) a recipe is mapped onto a unique set of ingredient(s), which means
        # the same set of ingredient(s) would not map to another recipe

        # we can tackle this problem as a directed graph problem, and
        # it is naturally solved by topological sorting
        neighbours = defaultdict(list)
        in_deg = defaultdict(int)

        for i in range(n):

            r, ing = recipes[i], ingredients[i]
            in_deg[r] += len(ing)

            for x in ing:
                neighbours[x].append(r)

        bfs_queue = deque([x for x in supplies if in_deg[x] == 0])

        # make recipes a set for quick lookup
        recipes = set(recipes)

        ans = []
        while bfs_queue:

            curr = bfs_queue.popleft()
            if curr in recipes:
                ans.append(curr)

            for x in neighbours[curr]:
                in_deg[x] -= 1
                # cond. to append to bfs_queue
                if in_deg[x] == 0:
                    bfs_queue.append(x)

        return ans
    
recipes = ["bread","sandwich","burger"]
ingredients = [["yeast","flour"],["bread","meat"],["sandwich","meat","bread"]]
supplies = ["yeast","flour","meat"]

# this is a malformed "cyclic" recipe construction
# notice the result does not contain A nor B, showing it's handled correctly
recipes = ['A', 'B']
ingredients = [['B'], ['A']]
supplies = ['A', 'B']

Solution().findAllRecipes(recipes, ingredients, supplies)