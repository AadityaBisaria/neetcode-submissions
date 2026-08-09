class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        
        N=len(nums)
        def func(i):
            if i==N:
                res.append(nums[:])
                return
            for j in range(i,len(nums)):
                nums[i],nums[j]=nums[j],nums[i]
                func(i+1)
                nums[i],nums[j]=nums[j],nums[i]
        func(0)
        return res