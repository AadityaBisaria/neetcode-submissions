class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left,right=0,len(heights)-1
        total=0
        while(left<right):
            lheight=heights[left]
            rheight=heights[right]
            if total<(right-left)*min(lheight,rheight):
                total =(right-left)*min(lheight,rheight)
            if lheight>rheight:
                right-=1
            else:
                left+=1
        return total
            