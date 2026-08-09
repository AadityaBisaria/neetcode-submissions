class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        cur=[0,0,0]
        for trip in triplets:
            count=0
            if max(cur[0],trip[0])<=target[0]:
                count+=1
            if max(cur[1],trip[1])<=target[1]:
                count+=1
            if max(cur[2],trip[2])<=target[2]:
                count+=1
            if count==3:
                cur=[max(cur[0],trip[0]),max(cur[1],trip[1]),max(cur[2],trip[2])]
            if cur==target:
                return True
        return False