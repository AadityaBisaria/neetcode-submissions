from collections import Counter
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
            counter=Counter(tasks)
            time=0
            temp_q={}
            heap=[(-count,key) for key, count in counter.items()]
            heapq.heapify(heap)
            while heap or temp_q:
                time+=1
                if heap:
                    count,key=heapq.heappop(heap)
                
                    count+=1
                    if count!=0:
                        temp_q[time+n]=(count,key)
                if time in temp_q:
                    temp_count,key=temp_q[time]
                    temp_q.pop(time)
                    heapq.heappush(heap,(temp_count,key))
                    
            return time

