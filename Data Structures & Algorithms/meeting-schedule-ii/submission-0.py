"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start,end=[],[]

        for i in intervals:
            s,e=i.start,i.end
            start.append(s)
            end.append(e)
        
        start.sort()
        end.sort()

        l=r=meet=total=0

        while(l<len(intervals)):
            if start[l]<end[r]:
                meet+=1
                l+=1
            else:
                meet-=1
                r+=1
            total=max(total,meet)
        return total