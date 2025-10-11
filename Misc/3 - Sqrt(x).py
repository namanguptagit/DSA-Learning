class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        first, last = 1, x
        while first <= last:
            mid = first + (last - first) // 2
            if mid == x // mid:
                return mid
            elif mid > x // mid:
                last = mid - 1
            else:
                first = mid + 1
        return last

# Add code below this line to test your solution
if __name__ == "__main__":
    solution = Solution()

    # Example 1
    x1 = 4
    print(f"Example 1: x = {x1}")
    print(f"Output: {solution.mySqrt(x1)}")
    print("-" * 30)

    # Example 2
    x2 = 8
    print(f"Example 2: x = {x2}")
    print(f"Output: {solution.mySqrt(x2)}")
    print("-" * 30)

    # Example 3 (perfect square)
    x3 = 16
    print(f"Example 3: x = {x3}")
    print(f"Output: {solution.mySqrt(x3)}")
    print("-" * 30)

    # Example 4 (zero)
    x4 = 0
    print(f"Example 4: x = {x4}")
    print(f"Output: {solution.mySqrt(x4)}")
    print("-" * 30)

    # Example 5 (large number)
    x5 = 1000000
    print(f"Example 5: x = {x5}")
    print(f"Output: {solution.mySqrt(x5)}")
    print("-" * 30)

    # Example (user input)
    print("Testing with user input...")
    try:
        user_x_str = input("Enter a non-negative integer: ")
        user_x = int(user_x_str)
        if user_x < 0:
            print("Please enter a non-negative integer.")
        else:
            print(f"User Input: x = {user_x}")
            print(f"Output: {solution.mySqrt(user_x)}")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")