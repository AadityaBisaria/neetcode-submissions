class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        #[1,2,-3,4]
        mincurr,maxcurr=1,1
        res=nums[0]
        for n in nums:
            temp=maxcurr*n
            maxcurr=max(maxcurr*n,mincurr*n,n)
            mincurr=min(temp, mincurr*n,n)
            res=max(res,maxcurr)
        return res
        