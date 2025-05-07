from collections import defaultdict
from typing import List
import heapq

class Twitter:
    def __init__(self):
        self.following_db = defaultdict(set)
        self.tweets = defaultdict(list)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time -= 1
    
    def getNewsFeed(self, userId: int) -> List[int]:
        #we have the list of people userId follows
        res = []
        minHeap = []

        for followeeId in self.following_db[userId]:
            if followeeId in self.tweets:
                index = len(self.tweets[followeeId]) - 1
                count, tweetId = self.tweets[followeeId][index]
                minHeap.append((count, tweetId, followeeId, index))

        if userId in self.tweets:
            index = len(self.tweets[userId]) - 1
            count, tweetId = self.tweets[userId][index]
            minHeap.append((count, tweetId, userId, index))
        
        heapq.heapify(minHeap)
        
        while minHeap and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop(minHeap)
            res.append(tweetId)

            if index - 1 >= 0:
                curr_count, curr_tweetId = self.tweets[followeeId][index-1]
                heapq.heappush(minHeap, (curr_count, curr_tweetId, followeeId, index - 1))
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following_db[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following_db[followerId]:
            self.following_db[followerId].remove(followeeId)

if __name__ == "__main__":
    twitter = Twitter()
    actions = ["postTweet","getNewsFeed","follow","postTweet","getNewsFeed","unfollow","getNewsFeed"]
    values = [[1,5],[1],[1,2],[2,6],[1],[1,2],[1]]

    for action, value in zip(actions, values):
        if action == "postTweet":
            twitter.postTweet(value[0], value[1])
        elif action == "getNewsFeed":
            print(twitter.getNewsFeed(value[0]))
        elif action == "follow":
            twitter.follow(value[0], value[1])
        elif action == "unfollow":
            twitter.unfollow(value[0], value[1])
        else:
            print("action not allowed. Please make sure inputs are correct")
    
# TC: O(1) follow, unfollow, and postTweet, O(nlogn), where n is the number of followee's a particular user has, for getNewsFeed
# SC: O(T + U + R), where T is the number of tweets total (in our tweets map), R is the number of relationships between users (ie. followee counts in our following map), and U is the total number of users
