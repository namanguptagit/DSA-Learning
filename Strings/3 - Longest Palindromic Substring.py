class Solution:
    def longestPalindrome(self, str:str)->str:
        pal = ""
        for i in range(len(str)):
            l,r = i,i 
            found = self.findpal(str,l,r)
            if len(pal) <len(found):
                pal = found
            l,r = i,i+1
            found = self.findpal(str,l,r)
            if len(pal) <len(found):
                pal = found
        return pal
    def findpal(self,s,l,r):
        ls = len(s)
        while l>=0 and r<ls and s[l]==s[r]:
            l-=1
            r+=1
        return s[l+1:r]

# Add code below this line to test your solution
if __name__ == "__main__":
    # Example 1
    s1 = "babad"
    solution = Solution()
    result1 = solution.longestPalindrome(s1)
    print(f"Example 1: s = \"{s1}\"")
    print(f"Output: \"{result1}\"")
    print("-" * 20)

    # Example 2
    s2 = "cbbd"
    result2 = solution.longestPalindrome(s2)
    print(f"Example 2: s = \"{s2}\"")
    print(f"Output: \"{result2}\"")
    print("-" * 20)

    # Example 3
    s3 = "a"
    result3 = solution.longestPalindrome(s3)
    print(f"Example 3: s = \"{s3}\"")
    print(f"Output: \"{result3}\"")
    print("-" * 20)

    # Example 4
    s4 = "racecar"
    result4 = solution.longestPalindrome(s4)
    print(f"Example 4: s = \"{s4}\"")
    print(f"Output: \"{result4}\"")
    print("-" * 20)

    # Example 5 (user input)
    print("Testing with user input...")
    try:
        # Take string input
        user_s = input("Enter a string to find longest palindromic substring: ")

        user_result = solution.longestPalindrome(user_s)
        print(f"User Input: s = \"{user_s}\"")
        print(f"Output: \"{user_result}\"")

    except Exception as e:
        print(f"Error: {e}")