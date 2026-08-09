class Solution:
    def trap(self, height: List[int]) -> int:
        left,right=0,len(height)-1
        i,j=left,right
        water=0
        while(i<j):
            if(height[left]<height[right]):
                i+=1
                if(height[i]<height[left]):
                    water+=height[left]-height[i]
                else:
                    left=i
                
            else:
                j-=1
                if(height[j]<height[right]):
                    water+=height[right]-height[j]
                else:
                    right=j
        return water
