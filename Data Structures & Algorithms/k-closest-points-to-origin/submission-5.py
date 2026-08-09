class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(point:List[int])->int:
            x,y=point
            return x**2 +y**2

        def partition(low,high):
            i,pivot=low,distance(points[high])
            for j in range(low,high):            
                if(distance(points[j])<pivot):
                    points[j],points[i]=points[i],points[j]
                    i+=1
            points[i],points[high]=points[high],points[i]
            return i   
    
        left,right=0,len(points)-1
        while left<=right:
            pivot=partition(left,right)
            if(pivot<k):
                left=pivot+1
            elif(pivot>k):
                right=pivot-1
            else:
                return points[:k]
        return points[:k]