class Solution:
    def getSum(self, a: int, b: int) -> int:
        while(b != 0):
            temp=(a^b) & 0xFFFFFFFF
            b=( (a&b)<<1) & 0xFFFFFFFF
            a=temp
        return a if a<= 0x7FFFFFFF else ~(a^0xFFFFFFFF)
