class Solution:
    def canJump(self, nums: List[int]) -> bool:
        deque=collections.deque()
        deque.append([0,nums[0]])
        visited=set()
        visited.add(0)
        while(deque):
            index,leap=deque.pop()
            if index+leap>=len(nums)-1:
                return True
            for i in range(index+1,index+leap+1):
                if i not in visited:
                    deque.append([i,nums[i]])
                    visited.add(0)
        return False