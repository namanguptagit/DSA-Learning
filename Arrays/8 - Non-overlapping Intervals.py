from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        n = len(intervals)

        prev = 0
        count = 1

        for i in range(1, n):
            if intervals[i][0] >= intervals[prev][1]:
                prev = i
                count += 1

        return n - count

# Add code below this line to test your solution
if __name__ == "__main__":
    # Example 1
    intervals1 = [[1, 2], [2, 3], [3, 4], [1, 3]]
    solution = Solution()
    result1 = solution.eraseOverlapIntervals(intervals1)
    print(f"Example 1: intervals = {intervals1}")
    print(f"Output: {result1}")
    print("-" * 20)

    # Example 2
    intervals2 = [[1, 2], [1, 2], [1, 2]]
    result2 = solution.eraseOverlapIntervals(intervals2)
    print(f"Example 2: intervals = {intervals2}")
    print(f"Output: {result2}")
    print("-" * 20)

    # Example 3
    intervals3 = [[1, 2], [2, 3]]
    result3 = solution.eraseOverlapIntervals(intervals3)
    print(f"Example 3: intervals = {intervals3}")
    print(f"Output: {result3}")
    print("-" * 20)

    # Example 4 (user input)
    print("Testing with user input...")
    try:
        # Take number of intervals
        n = int(input("Enter number of intervals: "))
        user_intervals = []
        for i in range(n):
            interval_str = input(f"Enter interval {i+1} (format: start end, e.g., 1 3): ")
            start, end = map(int, interval_str.split())
            user_intervals.append([start, end])

        user_result = solution.eraseOverlapIntervals(user_intervals)
        print(f"User Input: intervals = {user_intervals}")
        print(f"Output: {user_result}")

    except ValueError:
        print("Invalid input. Please enter valid numbers.")