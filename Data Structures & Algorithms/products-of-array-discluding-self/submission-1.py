class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftside,rightside=[0]*len(nums),[0]*len(nums)
        leftside[0]=1
        for i in range(1,len(nums)):
            leftside[i]=leftside[i-1]*nums[i-1]
        
        rightside[-1]=1
        for i in range(len(nums)-2,-1,-1):
            rightside[i]=rightside[i+1]*nums[i+1]
        
       # [1,1,2,8]
       # [48,24,6,1]
        res=[]
        for i in range(len(nums)):
            res.append(leftside[i]*rightside[i])
        return res