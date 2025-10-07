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

# Add code below this line to test your solution
if __name__ == "__main__":
    # Example 1
    intervals1 = [[1, 3], [6, 9]]
    newInterval1 = [2, 5]
    solution = Solution()
    result1 = solution.insert(intervals1, newInterval1)
    print(f"Example 1: intervals = {intervals1}, newInterval = {newInterval1}")
    print(f"Output: {result1}")
    print("-" * 20)

    # Example 2
    intervals2 = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
    newInterval2 = [4, 8]
    result2 = solution.insert(intervals2, newInterval2)
    print(f"Example 2: intervals = {intervals2}, newInterval = {newInterval2}")
    print(f"Output: {result2}")
    print("-" * 20)

    # Example 3 (user input)
    print("Testing with user input...")
    try:
        # Take number of intervals
        n = int(input("Enter number of existing intervals: "))
        user_intervals = []
        for i in range(n):
            interval_str = input(f"Enter interval {i+1} (format: start end, e.g., 1 3): ")
            start, end = map(int, interval_str.split())
            user_intervals.append([start, end])
        
        # Take new interval
        new_interval_str = input("Enter new interval (format: start end, e.g., 2 5): ")
        new_start, new_end = map(int, new_interval_str.split())
        new_interval = [new_start, new_end]

        user_result = solution.insert(user_intervals, new_interval)
        print(f"User Input: intervals = {user_intervals}, newInterval = {new_interval}")
        print(f"Output: {user_result}")

    except ValueError:
        print("Invalid input. Please enter valid numbers.")