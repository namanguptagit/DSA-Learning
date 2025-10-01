class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        n = len(firstList)
        m = len(secondList)
        ans = []
        
        for i in range(n):
            for j in range(m):
                # Compute intersection of [a1, b1] and [a2, b2]
                start = max(firstList[i][0], secondList[j][0])
                end = min(firstList[i][1], secondList[j][1])
                
                if start <= end:
                    ans.append([start, end])
        
        return ans
# Another Approach Better Time Complexity
class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        ans = []
        i, j = 0, 0
        while i < len(firstList) and j < len(secondList):
            # Find overlap
            start = max(firstList[i][0], secondList[j][0])
            end = min(firstList[i][1], secondList[j][1])
            
            if start <= end:
                ans.append([start, end])
            
            # Move the pointer with smaller endpoint
            if firstList[i][1] < secondList[j][1]:
                i += 1
            else:
                j += 1
        return ans