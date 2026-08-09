class Solution:
    def checkValidString(self, s: str) -> bool:
        count=0
        left=[]
        star=[]

        for i,ch in enumerate(s):
            if ch=="(":
                left.append(i)
            elif ch=="*":
                star.append(i)
            else:
                if not left and not star:
                    return False
                else:
                    if left:
                        left.pop()
                    else:
                        star.pop()
            
        while left and star:
            if left.pop()>star.pop():
                return False
        return not left
    

            
               
        

        