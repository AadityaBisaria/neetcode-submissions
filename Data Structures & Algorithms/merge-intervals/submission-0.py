class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        arr=[]
        intervals.sort(key=lambda x: x[0])
        prev_start,prev_end=intervals[0][0],intervals[0][1]
        for ind,pair in enumerate(intervals):
            start,end=pair[0],pair[1]
            if start<=prev_end:
                prev_end=max(prev_end,end)
            else:
                arr.append([prev_start,prev_end])
                prev_start=start
                prev_end=end
        arr.append([prev_start,prev_end])
        return arr

