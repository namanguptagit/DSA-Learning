from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        max_freq = 0
        l = 0
        res = 0

        for r in range(len(s)):
            count[s[r]] += 1
            max_freq = max(max_freq, count[s[r]])

            # If replacements needed > k, shrink window
            while (r - l + 1) - max_freq > k:
                count[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)

        return res

# Add code below this line to test your solution
if __name__ == "__main__":
    # Example 1
    s1 = "ABAB"
    k1 = 2
    solution = Solution()
    result1 = solution.characterReplacement(s1, k1)
    print(f"Example 1: s = \"{s1}\", k = {k1}")
    print(f"Output: {result1}")
    print("-" * 20)

    # Example 2
    s2 = "AABABBA"
    k2 = 1
    result2 = solution.characterReplacement(s2, k2)
    print(f"Example 2: s = \"{s2}\", k = {k2}")
    print(f"Output: {result2}")
    print("-" * 20)

    # Example 3
    s3 = "ABCDEF"
    k3 = 1
    result3 = solution.characterReplacement(s3, k3)
    print(f"Example 3: s = \"{s3}\", k = {k3}")
    print(f"Output: {result3}")
    print("-" * 20)

    # Example 4
    s4 = "AAAA"
    k4 = 2
    result4 = solution.characterReplacement(s4, k4)
    print(f"Example 4: s = \"{s4}\", k = {k4}")
    print(f"Output: {result4}")
    print("-" * 20)

    # Example 5 (user input)
    print("Testing with user input...")
    try:
        # Take string input
        user_s = input("Enter a string: ")
        
        # Take k input
        user_k = int(input("Enter the number of character replacements allowed: "))

        user_result = solution.characterReplacement(user_s, user_k)
        print(f"User Input: s = \"{user_s}\", k = {user_k}")
        print(f"Output: {user_result}")

    except ValueError:
        print("Invalid input. Please enter valid values.")
    except Exception as e:
        print(f"Error: {e}")