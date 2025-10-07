class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        arr = [False] * 128
        l = r = 0
        max_len = 0

        while r < len(s):
            if not arr[ord(s[r])]:
                arr[ord(s[r])] = True
                max_len = max(max_len, r - l + 1)
                r += 1
            else:
                arr[ord(s[l])] = False
                l += 1
        return max_len

# Add code below this line to test your solution
if __name__ == "__main__":
    # Example 1
    s1 = "abcabcbb"
    solution = Solution()
    result1 = solution.lengthOfLongestSubstring(s1)
    print(f"Example 1: s = \"{s1}\"")
    print(f"Output: {result1}")
    print("-" * 20)

    # Example 2
    s2 = "bbbbb"
    result2 = solution.lengthOfLongestSubstring(s2)
    print(f"Example 2: s = \"{s2}\"")
    print(f"Output: {result2}")
    print("-" * 20)

    # Example 3
    s3 = "pwwkew"
    result3 = solution.lengthOfLongestSubstring(s3)
    print(f"Example 3: s = \"{s3}\"")
    print(f"Output: {result3}")
    print("-" * 20)

    # Example 4
    s4 = "dvdf"
    result4 = solution.lengthOfLongestSubstring(s4)
    print(f"Example 4: s = \"{s4}\"")
    print(f"Output: {result4}")
    print("-" * 20)

    # Example 5 (user input)
    print("Testing with user input...")
    try:
        # Take string input
        user_s = input("Enter a string to find longest substring without repeating characters: ")

        user_result = solution.lengthOfLongestSubstring(user_s)
        print(f"User Input: s = \"{user_s}\"")
        print(f"Output: {user_result}")

    except Exception as e:
        print(f"Error: {e}")