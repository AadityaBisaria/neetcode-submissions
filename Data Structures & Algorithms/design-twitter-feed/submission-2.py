import heapq
class Twitter:

    def __init__(self):
        self.Hmap={}
        self.tweet={}
        self.time=0
    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.Hmap:
            self.Hmap[userId]=[userId]
        if userId not in self.tweet:
            self.tweet[userId]=[]
        self.tweet[userId].append((-self.time,tweetId))
        self.time+=1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        heap=[]
        if userId not in self.Hmap:
            return []
        for follower in self.Hmap[userId]:
            for time,tweet in self.tweet.get(follower, []):
                heap.append((time,tweet))
        heapq.heapify(heap)
        ans=[]
        for i in range(10):
            if heap:
                time,tweetid=heapq.heappop(heap)
                ans.append(tweetid)
        return ans

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.Hmap:
            self.Hmap[followerId] = [followerId]
        if followeeId not in self.Hmap[followerId]:
            self.Hmap[followerId].append(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId and followeeId in self.Hmap[followerId]:
            self.Hmap[followerId].remove(followeeId)
        