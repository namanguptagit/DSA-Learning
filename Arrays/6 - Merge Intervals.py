from typing import List

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

# Add code below this line to test your solution
if __name__ == "__main__":
    # Example 1
    intervals1 = [[1, 3], [2, 6], [8, 10], [15, 18]]
    solution = Solution()
    result1 = solution.merge(intervals1)
    print(f"Example 1: intervals = {intervals1}")
    print(f"Output: {result1}")
    print("-" * 20)

    # Example 2
    intervals2 = [[1, 4], [4, 5]]
    result2 = solution.merge(intervals2)
    print(f"Example 2: intervals = {intervals2}")
    print(f"Output: {result2}")
    print("-" * 20)

    # Example 3 (user input)
    print("Testing with user input...")
    try:
        # Take number of intervals
        n = int(input("Enter number of intervals: "))
        user_intervals = []
        for i in range(n):
            interval_str = input(f"Enter interval {i+1} (format: start end, e.g., 1 3): ")
            start, end = map(int, interval_str.split())
            user_intervals.append([start, end])

        user_result = solution.merge(user_intervals)
        print(f"User Input: intervals = {user_intervals}")
        print(f"Output: {user_result}")

    except ValueError:
        print("Invalid input. Please enter valid numbers.")