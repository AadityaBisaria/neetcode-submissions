class Solution:
    def trap(self, height: List[int]) -> int:
        l,r=0,len(height)-1
        left_max,right_max=height[l],height[r]
        water=0
        while l<r:
            if height[l]>height[r]:
               water+= min(left_max,right_max)-height[r] 
               r-=1
               right_max=max(right_max,height[r])
            elif height[l]<=height[r]:
               water+=min(left_max,right_max)-height[l] 
               l+=1
               left_max=max(left_max,height[l])
        return water            


