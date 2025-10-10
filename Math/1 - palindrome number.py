class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        rev = 0
        num = x
        
        while num != 0:
            rev = rev * 10 + num % 10
            num = num // 10
        
        return rev == x
# Add code below this line to test your solution
if __name__ == "__main__":
    solution = Solution()

    # Example 1
    x1 = 121
    print(f"Example 1: x = {x1}")
    print(f"Output: {solution.isPalindrome(x1)}")
    print("-" * 30)

    # Example 2 (negative number)
    x2 = -121
    print(f"Example 2: x = {x2}")
    print(f"Output: {solution.isPalindrome(x2)}")
    print("-" * 30)

    # Example 3 (not a palindrome due to trailing zero)
    x3 = 10
    print(f"Example 3: x = {x3}")
    print(f"Output: {solution.isPalindrome(x3)}")
    print("-" * 30)

    # Example 4 (single digit)
    x4 = 0
    print(f"Example 4: x = {x4}")
    print(f"Output: {solution.isPalindrome(x4)}")
    print("-" * 30)

    # Example 5 (even-length palindrome)
    x5 = 1221
    print(f"Example 5: x = {x5}")
    print(f"Output: {solution.isPalindrome(x5)}")
    print("-" * 30)

    # Example (user input)
    print("Testing with user input...")
    try:
        user_x_str = input("Enter an integer: ")
        user_x = int(user_x_str)
        print(f"User Input: x = {user_x}")
        print(f"Output: {solution.isPalindrome(user_x)}")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")