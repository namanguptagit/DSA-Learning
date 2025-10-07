class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
       return haystack.find(needle)

# Add code below this line to test your solution
if __name__ == "__main__":
    # Example 1
    haystack1 = "sadbutsad"
    needle1 = "sad"
    solution = Solution()
    result1 = solution.strStr(haystack1, needle1)
    print(f"Example 1: haystack = \"{haystack1}\", needle = \"{needle1}\"")
    print(f"Output: {result1}")
    print("-" * 20)

    # Example 2
    haystack2 = "leetcode"
    needle2 = "leeto"
    result2 = solution.strStr(haystack2, needle2)
    print(f"Example 2: haystack = \"{haystack2}\", needle = \"{needle2}\"")
    print(f"Output: {result2}")
    print("-" * 20)

    # Example 3
    haystack3 = "hello"
    needle3 = "ll"
    result3 = solution.strStr(haystack3, needle3)
    print(f"Example 3: haystack = \"{haystack3}\", needle = \"{needle3}\"")
    print(f"Output: {result3}")
    print("-" * 20)

    # Example 4
    haystack4 = "aaaaa"
    needle4 = "bba"
    result4 = solution.strStr(haystack4, needle4)
    print(f"Example 4: haystack = \"{haystack4}\", needle = \"{needle4}\"")
    print(f"Output: {result4}")
    print("-" * 20)

    # Example 5 (user input)
    print("Testing with user input...")
    try:
        # Take haystack input
        user_haystack = input("Enter the haystack string: ")
        
        # Take needle input
        user_needle = input("Enter the needle string: ")

        user_result = solution.strStr(user_haystack, user_needle)
        print(f"User Input: haystack = \"{user_haystack}\", needle = \"{user_needle}\"")
        print(f"Output: {user_result}")

    except Exception as e:
        print(f"Error: {e}")