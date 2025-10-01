class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n=len(intervals)
        intervals.sort(key=lambda x: x[0])
        merged = [intervals[0]]
        j=0
        for i in range(1,n):
            if merged[j][1] < intervals[i][0]:
                merged.append(intervals[i])
                j+=1
            else:
                merged[j][1]=max(intervals[i][1],merged[j][1])

        return merged