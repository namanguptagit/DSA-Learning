from collections import Counter

class Solution:
    def longestKSubstr(self, s, k):
        i, j = 0, 0
        count = 0
        S = len(s)
        mx = -1   # use -1 if no valid substring exists
        lookup = Counter()

        while j < S:
            # add current character
            lookup[s[j]] += 1
            # if it's a new character, increment distinct count
            if lookup[s[j]] == 1:
                count += 1

            # if distinct characters exceed k, shrink from left
            while count > k:
                lookup[s[i]] -= 1
                if lookup[s[i]] == 0:
                    del lookup[s[i]]
                    count -= 1
                i += 1

            # if window has exactly k distinct characters
            if count == k:
                mx = max(mx, j - i + 1)

            j += 1

        return mx

# Add code below this line to test your solution
if __name__ == "__main__":
    # Example 1
    s1 = "aabacbebebe"
    k1 = 3
    solution = Solution()
    result1 = solution.longestKSubstr(s1, k1)
    print(f"Example 1: s = \"{s1}\", k = {k1}")
    print(f"Output: {result1}")
    print("-" * 20)

    # Example 2
    s2 = "aaaa"
    k2 = 2
    result2 = solution.longestKSubstr(s2, k2)
    print(f"Example 2: s = \"{s2}\", k = {k2}")
    print(f"Output: {result2}")
    print("-" * 20)

    # Example 3
    s3 = "eceba"
    k3 = 3
    result3 = solution.longestKSubstr(s3, k3)
    print(f"Example 3: s = \"{s3}\", k = {k3}")
    print(f"Output: {result3}")
    print("-" * 20)

    # Example 4
    s4 = "abc"
    k4 = 2
    result4 = solution.longestKSubstr(s4, k4)
    print(f"Example 4: s = \"{s4}\", k = {k4}")
    print(f"Output: {result4}")
    print("-" * 20)

    # Example 5 (user input)
    print("Testing with user input...")
    try:
        # Take string input
        user_s = input("Enter a string: ")
        
        # Take k input
        user_k = int(input("Enter the exact number of distinct characters: "))

        user_result = solution.longestKSubstr(user_s, user_k)
        print(f"User Input: s = \"{user_s}\", k = {user_k}")
        print(f"Output: {user_result}")

    except ValueError:
        print("Invalid input. Please enter valid values.")
    except Exception as e:
        print(f"Error: {e}")