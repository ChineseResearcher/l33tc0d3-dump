# heap - medium
from typing import List
import heapq
class Twitter:

    def __init__(self):
        # <userId, tweets posted by this user>
        self.feed = dict()
        # <userId, users followed by userId>
        self.following = dict()
        # since not sure if tweetId is generated in increasing order
        # maintain a tweetOrder variable
        self.tweetOrder = 1

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.feed:
            self.feed[userId] = []

        # make sure a new userId follows himself
        if userId not in self.following:
            self.following[userId] = set([userId])
        
        # invert tweetOrder for maxheap later
        self.feed[userId].append([-self.tweetOrder, tweetId])
        self.tweetOrder += 1
        return

    def getNewsFeed(self, userId: int) -> List[int]:
        # a user never seen before would not have any feed
        if userId not in self.following: return []

        # for all the following users of this userId, build a max-heap
        # to retrieve 10 recent tweets supposedly appearing in feed
        maxheap = []
        for followee in self.following[userId]:
            # the followee might not have posted
            if followee in self.feed:
                maxheap.extend(self.feed[followee])

        # max-heapify based on self.tweetOrder
        heapq.heapify(maxheap)

        feed = []
        while maxheap:

            _, tweetId = heapq.heappop(maxheap)
            feed.append(tweetId)
            # only load 10 recent
            if len(feed) == 10: break

        return feed
        
    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.following:
            # a user must follow himself
            self.following[followerId] = set([followerId])

        # a new user's feed is initiated to empty
        if followerId not in self.feed:
            self.feed[followerId] = []

        self.following[followerId].add(followeeId)
        return

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # no action done if a person has not followed anyone
        if followerId not in self.following:
            return
        
        self.following[followerId].discard(followeeId)
        return
    
obj = Twitter()

commands = ["postTweet", "getNewsFeed", "follow", "postTweet", "getNewsFeed", "unfollow", "getNewsFeed"]
arguments = [[1, 5], [1], [1, 2], [2, 6], [1], [1, 2], [1]]

commands = ["postTweet","getNewsFeed","follow","getNewsFeed","unfollow","getNewsFeed"]
arguments = [1,1],[1],[2,1],[2],[2,1],[2]

commands = ["postTweet","follow","follow","getNewsFeed","postTweet","getNewsFeed","getNewsFeed", \
            "unfollow","getNewsFeed","getNewsFeed","unfollow","getNewsFeed","getNewsFeed"]
arguments = [[1,5],[1,2],[2,1],[2],[2,6],[1],[2],[2,1],[1],[2],[1,2],[1],[2]]

for command, args in zip(commands, arguments):
    # Use getattr to dynamically call the method by its name
    func = getattr(obj, command)
    print('Calling Command:', '<', command, '>', f'With Arguments: {args}' if args else '')
    print('Output:', func(*args))