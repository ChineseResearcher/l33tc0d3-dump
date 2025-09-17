# heap - medium
from typing import List
from collections import defaultdict
import heapq
class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        
        n = len(foods)
        self.cuisine_best = defaultdict(list)
        self.curr_ratings = defaultdict(int)
        self.cuisine_cat = dict()
        for i in range(n):

            food, cuisine, rating = foods[i], cuisines[i], ratings[i]
            self.cuisine_cat[food] = cuisine
            # maxheap
            heapq.heappush(self.cuisine_best[cuisine], (-rating, food))
            self.curr_ratings[food] = rating

    def changeRating(self, food: str, newRating: int) -> None:
        self.curr_ratings[food] = newRating
        # mark update to maxheap
        heapq.heappush(self.cuisine_best[self.cuisine_cat[food]], (-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        # lazy-deletion whenever curr. ratings do not match w/ heap
        while True:

            best_rating = abs(self.cuisine_best[cuisine][0][0])
            best_food = self.cuisine_best[cuisine][0][1]

            if self.curr_ratings[best_food] == best_rating:
                break

            # otherwise, perform deletion of the expired rating
            heapq.heappop(self.cuisine_best[cuisine])

        return best_food
    
obj = FoodRatings(["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"],
                  ["korean", "japanese", "japanese", "greek", "japanese", "korean"],
                  [9, 12, 8, 15, 14, 7])

commands = ["highestRated", "highestRated", "changeRating", "highestRated", "changeRating", "highestRated"]
arguments = [["korean"], ["japanese"], ["sushi", 16], ["japanese"], ["ramen", 16], ["japanese"]]

for command, args in zip(commands, arguments):
    # Use getattr to dynamically call the method by its name
    func = getattr(obj, command)
    print('Calling Command:', '<', command, '>', f'With Arguments: {args}' if args else '')
    print('Output:', func(*args))