# Two Pointer Approach
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])

        res = count = 0
        s = e = 0
        while s < len(intervals):
            if start[s] < end[e]:
                s += 1
                count += 1
            else:
                e += 1
                count -= 1
            res = max(res, count)
        return res
# Heap Approach

import heapq

class Solution:
    def meetingRoomsIi(self, nums, k):
        n=len(nums)
        nums.sort()
        hp = [nums[ 0 ][ 1 ]]
        heapq.heapify( hp )
        for i in range ( 1 , n ):
            if ( nums[i][0] > hp[0] ):
                heapq.heappop(hp)
                heapq.heappush( hp , nums[i][1] )
            else :
                heapq.heappush( hp , nums[i][1] )
        return len(hp)
