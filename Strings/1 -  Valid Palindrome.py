class Solution(object):
    def isPalindrome(self, s: str) -> bool:
        new = ""
        for i in s:
            if i.isalnum():
                new += i.lower()
        return new == new[::-1]

# Add code below this line to test your solution
if __name__ == "__main__":
    # Example 1
    s1 = "A man, a plan, a canal: Panama"
    solution = Solution()
    result1 = solution.isPalindrome(s1)
    print(f"Example 1: s = \"{s1}\"")
    print(f"Output: {result1}")
    print("-" * 20)

    # Example 2
    s2 = "race a car"
    result2 = solution.isPalindrome(s2)
    print(f"Example 2: s = \"{s2}\"")
    print(f"Output: {result2}")
    print("-" * 20)

    # Example 3
    s3 = " "
    result3 = solution.isPalindrome(s3)
    print(f"Example 3: s = \"{s3}\"")
    print(f"Output: {result3}")
    print("-" * 20)

    # Example 4 (user input)
    print("Testing with user input...")
    try:
        # Take string input
        user_s = input("Enter a string to check if it's a palindrome: ")

        user_result = solution.isPalindrome(user_s)
        print(f"User Input: s = \"{user_s}\"")
        print(f"Output: {user_result}")

    except Exception as e:
        print(f"Error: {e}")