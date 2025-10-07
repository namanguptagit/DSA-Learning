class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        word = ""
        s2 = ""
        
        for i in range(len(s) - 1, -1, -1):
            if s[i] == " ":
                if word:
                    s2 += word + " " 
                    word = ""
            else:
                word = s[i] + word
        if word:
            s2 += word
        
        return s2

# Add code below this line to test your solution
if __name__ == "__main__":
    # Example 1
    s1 = "the sky is blue"
    solution = Solution()
    result1 = solution.reverseWords(s1)
    print(f"Example 1: s = \"{s1}\"")
    print(f"Output: \"{result1}\"")
    print("-" * 20)

    # Example 2
    s2 = "  hello world  "
    result2 = solution.reverseWords(s2)
    print(f"Example 2: s = \"{s2}\"")
    print(f"Output: \"{result2}\"")
    print("-" * 20)

    # Example 3
    s3 = "a good   example"
    result3 = solution.reverseWords(s3)
    print(f"Example 3: s = \"{s3}\"")
    print(f"Output: \"{result3}\"")
    print("-" * 20)

    # Example 4 (user input)
    print("Testing with user input...")
    try:
        # Take string input
        user_s = input("Enter a string to reverse words: ")

        user_result = solution.reverseWords(user_s)
        print(f"User Input: s = \"{user_s}\"")
        print(f"Output: \"{user_result}\"")

    except Exception as e:
        print(f"Error: {e}")