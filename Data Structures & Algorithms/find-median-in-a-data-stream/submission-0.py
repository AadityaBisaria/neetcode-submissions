class MedianFinder:

    def __init__(self):
        self.array=[]
        self.length=0

    def addNum(self, num: int) -> None:
        left,right=0,self.length
        while left<right:
            mid=left+(right-left)//2
            if self.array[mid]<num:
                left=mid+1
            else:
                right=mid
        self.array.insert(left, num)
            #self.array=self.array[left:]+[num]+self.array[:left]
        self.length+=1

    def findMedian(self) -> float:
        if self.length%2==0:
            return (self.array[self.length//2]+self.array[(self.length//2)-1])/2
        else:
            return self.array[(self.length//2)]