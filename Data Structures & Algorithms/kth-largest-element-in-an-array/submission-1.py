class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k=len(nums)-k

        def partition(nums: List[int], left: int, right: int)->int:
            pivot,i=nums[right],left
            for j in range(left,right):

                if(nums[j]<pivot):
                    nums[j],nums[i]=nums[i],nums[j]
                    i+=1
            nums[right],nums[i]=nums[i],nums[right]
            return i

        left,right=0,len(nums)-1

        while(True):
            pivot=partition(nums,left,right)
            if(k>pivot):
               left=pivot+1
            elif(k<pivot):
                right=pivot-1
            else:
                return nums[k]
        
      

    

              