from typing import List
import heapq

# Define Interval class for the first approach
class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

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

# Add code below this line to test your solution
if __name__ == "__main__":
    # Example 1 - Two Pointer Approach
    intervals1 = [Interval(0, 30), Interval(5, 10), Interval(15, 20)]
    solution1 = Solution()
    result1 = solution1.minMeetingRooms(intervals1)
    print(f"Example 1 (Two Pointer): intervals = [[0,30], [5,10], [15,20]]")
    print(f"Output: {result1}")
    print("-" * 20)

    # Example 2 - Two Pointer Approach
    intervals2 = [Interval(7, 10), Interval(2, 4)]
    result2 = solution1.minMeetingRooms(intervals2)
    print(f"Example 2 (Two Pointer): intervals = [[7,10], [2,4]]")
    print(f"Output: {result2}")
    print("-" * 20)

    # Example 1 - Heap Approach
    nums1 = [[0, 30], [5, 10], [15, 20]]
    solution2 = Solution()
    result3 = solution2.meetingRoomsIi(nums1, 0)  # k parameter not used in this implementation
    print(f"Example 1 (Heap): intervals = {nums1}")
    print(f"Output: {result3}")
    print("-" * 20)

    # Example 2 - Heap Approach
    nums2 = [[7, 10], [2, 4]]
    result4 = solution2.meetingRoomsIi(nums2, 0)  # k parameter not used in this implementation
    print(f"Example 2 (Heap): intervals = {nums2}")
    print(f"Output: {result4}")
    print("-" * 20)

    # Example 3 (user input)
    print("Testing with user input...")
    try:
        # Take number of meetings
        n = int(input("Enter number of meetings: "))
        user_intervals = []
        for i in range(n):
            interval_str = input(f"Enter meeting {i+1} (format: start end, e.g., 0 30): ")
            start, end = map(int, interval_str.split())
            user_intervals.append(Interval(start, end))

        user_result = solution1.minMeetingRooms(user_intervals)
        print(f"User Input: intervals = [[{', '.join([f'{i.start},{i.end}' for i in user_intervals])}]]")
        print(f"Output: {user_result}")

    except ValueError:
        print("Invalid input. Please enter valid numbers.")
