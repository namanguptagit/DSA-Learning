from collections import Counter

class Solution:
    def longestKSubstr(self, s, k):
        i = 0
        j = 0
        count = 0
        S = len(s)
        mx = 0
        lookup = Counter()

        while j < S:
            # include s[j]
            lookup[s[j]] += 1
            if lookup[s[j]] == 1:
                count += 1

            # shrink while we have more than k distinct chars
            while count > k:
                lookup[s[i]] -= 1
                if lookup[s[i]] == 0:
                    del lookup[s[i]]
                    count -= 1
                i += 1

            # now distinct chars <= k -> update max
            mx = max(mx, j - i + 1)
            j += 1

        return mx

# Add code below this line to test your solution
if __name__ == "__main__":
    # Example 1
    s1 = "eceba"
    k1 = 2
    solution = Solution()
    result1 = solution.longestKSubstr(s1, k1)
    print(f"Example 1: s = \"{s1}\", k = {k1}")
    print(f"Output: {result1}")
    print("-" * 20)

    # Example 2
    s2 = "aa"
    k2 = 1
    result2 = solution.longestKSubstr(s2, k2)
    print(f"Example 2: s = \"{s2}\", k = {k2}")
    print(f"Output: {result2}")
    print("-" * 20)

    # Example 3
    s3 = "aabacbebebe"
    k3 = 3
    result3 = solution.longestKSubstr(s3, k3)
    print(f"Example 3: s = \"{s3}\", k = {k3}")
    print(f"Output: {result3}")
    print("-" * 20)

    # Example 4 (user input)
    print("Testing with user input...")
    try:
        # Take string input
        user_s = input("Enter a string: ")
        
        # Take k input
        user_k = int(input("Enter the maximum number of distinct characters: "))

        user_result = solution.longestKSubstr(user_s, user_k)
        print(f"User Input: s = \"{user_s}\", k = {user_k}")
        print(f"Output: {user_result}")

    except ValueError:
        print("Invalid input. Please enter valid values.")
    except Exception as e:
        print(f"Error: {e}")