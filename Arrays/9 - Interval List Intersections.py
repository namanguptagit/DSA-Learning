from typing import List

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

# Add code below this line to test your solution
if __name__ == "__main__":
    # Example 1
    firstList1 = [[0, 2], [5, 10], [13, 23], [24, 25]]
    secondList1 = [[1, 5], [8, 12], [15, 24], [25, 26]]
    solution = Solution()
    result1 = solution.intervalIntersection(firstList1, secondList1)
    print(f"Example 1: firstList = {firstList1}, secondList = {secondList1}")
    print(f"Output: {result1}")
    print("-" * 20)

    # Example 2
    firstList2 = [[1, 3], [5, 9]]
    secondList2 = []
    result2 = solution.intervalIntersection(firstList2, secondList2)
    print(f"Example 2: firstList = {firstList2}, secondList = {secondList2}")
    print(f"Output: {result2}")
    print("-" * 20)

    # Example 3 (user input)
    print("Testing with user input...")
    try:
        # Take first list
        n1 = int(input("Enter number of intervals in first list: "))
        first_list = []
        for i in range(n1):
            interval_str = input(f"Enter interval {i+1} of first list (format: start end): ")
            start, end = map(int, interval_str.split())
            first_list.append([start, end])
        
        # Take second list
        n2 = int(input("Enter number of intervals in second list: "))
        second_list = []
        for i in range(n2):
            interval_str = input(f"Enter interval {i+1} of second list (format: start end): ")
            start, end = map(int, interval_str.split())
            second_list.append([start, end])

        user_result = solution.intervalIntersection(first_list, second_list)
        print(f"User Input: firstList = {first_list}, secondList = {second_list}")
        print(f"Output: {user_result}")

    except ValueError:
        print("Invalid input. Please enter valid numbers.")