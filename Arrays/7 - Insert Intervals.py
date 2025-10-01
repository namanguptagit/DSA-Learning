from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        newmerged = []
        inserted = False
        for interval in intervals:
            if not inserted and interval[0] > newInterval[0]:
                newmerged.append(newInterval)
                inserted = True
            newmerged.append(interval)

        if not inserted:
            newmerged.append(newInterval)

        merged = [newmerged[0]]
        for i in range(1, len(newmerged)):
            if merged[-1][1] < newmerged[i][0]:
                merged.append(newmerged[i])
            else:
                merged[-1][1] = max(merged[-1][1], newmerged[i][1])

        return merged
