# heap - hard
from typing import List
import heapq
class MovieRentingSystem:

    def __init__(self, n: int, entries: List[List[int]]):
        self.search_heap = dict() # unrented
        self.shop_price = dict()
        for shop_id, movie_id, price in entries:
            
            # record the selling price of a movie at a shop
            self.shop_price[(shop_id, movie_id)] = price

            if movie_id not in self.search_heap:
                self.search_heap[movie_id] = []
            # minheap maintained by <price, shop>
            heapq.heappush(self.search_heap[movie_id], (price, shop_id))

        self.report_heap = [] # rented
        # keep track of rent status
        self.usage = set()

    def search(self, movie: int) -> List[int]:
        
        res = []
        if movie not in self.search_heap:
            return res

        searched = set()
        while self.search_heap[movie] and len(res) < 5:
            price, shop_id = heapq.heappop(self.search_heap[movie])
            if (shop_id, movie) in self.usage:
                continue
            if (shop_id, movie) in searched:
                continue

            res.append((price, shop_id))
            # flag searched
            searched.add((shop_id, movie))

        # push back the 5 (or fewer) cheapest shops unrented for the given movie
        for price, shop_id in res:
            heapq.heappush(self.search_heap[movie], (price, shop_id))
        return [x[1] for x in res]

    def rent(self, shop: int, movie: int) -> None:
        self.usage.add((shop, movie))

        price = self.shop_price[(shop, movie)]
        # also push to report_heap as it's now rented
        heapq.heappush(self.report_heap, (price, shop, movie))
        return

    def drop(self, shop: int, movie: int) -> None:
        self.usage.discard((shop, movie))

        # also push to search_heap as it's now unrented
        price = self.shop_price[(shop, movie)]
        heapq.heappush(self.search_heap[movie], (price, shop))
        return

    def report(self) -> List[List[int]]:
        
        res, reported = [], set()
        while self.report_heap and len(res) < 5:
            price, shop_id, movie_id = heapq.heappop(self.report_heap)
            if (shop_id, movie_id) not in self.usage:
                continue
            if (shop_id, movie_id) in reported:
                continue

            res.append((price, shop_id, movie_id))
            # flag reported
            reported.add((shop_id, movie_id))

        # push back the 5 (or fewer) cheapest movies rented
        for price, shop_id, movie_id in res:
            heapq.heappush(self.report_heap, (price, shop_id, movie_id))
        return [[x[1], x[2]] for x in res]
    
obj = MovieRentingSystem(3, [[0,1,5],[0,2,6],[0,3,7],[1,1,4],[1,2,7],[2,1,5]])

commands = ["search", "rent", "rent", "report", "drop", "search"]
arguments = [[1], [0, 1], [1, 2], [], [1, 2], [2]]

obj= MovieRentingSystem(10, [[0,418,3],[9,5144,46],[2,8986,29],[6,1446,28],[3,8215,97],
                            [7,9105,34],[6,9105,30],[5,1722,94],[9,528,40],[3,850,77],
                            [3,7069,40],[8,1997,42],[0,8215,28],[7,4050,80],[4,7100,97],
                            [4,9686,32],[4,2566,93],[2,8320,12],[2,5495,56]])

commands = ["search","search","rent","search","search","report","search","drop"]
arguments = [[7837],[5495],[4,7100],[9105],[1446],[],[9869],[4,7100]]

for command, args in zip(commands, arguments):
    # Use getattr to dynamically call the method by its name
    func = getattr(obj, command)
    print('Calling Command:', '<', command, '>', f'With Arguments: {args}' if args else '')
    print('Output:', func(*args))