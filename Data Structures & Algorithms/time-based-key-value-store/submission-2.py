from sortedcontainers import SortedDict
class TimeMap:

    def __init__(self):
        self.hmap=defaultdict(SortedDict)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hmap[key][timestamp]=value

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hmap:
            return ""
        
        keys=list(self.hmap[key].keys())
        l,r=0,len(keys)-1
        res=""
        while l<=r:
            m=(l+r)//2
            if keys[m]>timestamp:
                r=m-1
            else:
                l=m+1
                res=keys[m]
        return self.hmap[key][res] if res else ""