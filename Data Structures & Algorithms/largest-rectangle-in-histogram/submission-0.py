class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea=0
        stack=[]
        for i,height in enumerate(heights):
            start=i
            while(stack and height<=stack[-1][1]):
                index,h=stack.pop()
                area=h*(i-index)
                if(maxArea<area):
                    maxArea=area
                start=index
            stack.append((start,height))

        for i,h in stack:
            area=h*(len(heights)-i)
            if maxArea<area:
                maxArea=area       
        return maxArea
                
                
                

             