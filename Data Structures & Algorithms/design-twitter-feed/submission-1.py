import heapq
from collections import defaultdict

class Twitter:

    def __init__(self):
        self.count=0
        self.Follower_map=defaultdict(set)
        self.Tweet_map=defaultdict(list) 

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.Tweet_map[userId].append([self.count,tweetId]) 
        self.count-=1

    def getNewsFeed(self, userId: int) -> List[int]:
        self.Follower_map[userId].add(userId)
        res=[]
        minHeap=[]

        for follower in self.Follower_map[userId]:
            if self.Tweet_map[follower]:
                index=len(self.Tweet_map[follower])-1
                count,tweetId=self.Tweet_map[follower][index]   
                heapq.heappush(minHeap,[count,tweetId,follower,index-1])
                
        while(minHeap) and len(res)<10:
            count,tweetId,follower,index=heapq.heappop(minHeap)
            res.append(tweetId)

            if index>=0:
                count,tweetId=self.Tweet_map[follower][index]
                heapq.heappush(minHeap,[count,tweetId,follower,index-1])
        return res    
            
    def follow(self, followerId: int, followeeId: int) -> None:
        self.Follower_map[followerId].add(followeeId)       

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.Follower_map[followerId].discard(followeeId)
        
