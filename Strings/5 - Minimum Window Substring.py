from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        lookup = Counter(t)
        mx = float("inf")
        output = ""
        S=len(s)
        start,end = 0,0
        count = len(lookup)
        #ADOBECODEBANC
        
        while end < S:
            #end pointer
            while end < S and count!=0:
                if s[end] in lookup:
                    lookup[s[end]] -= 1
                    if lookup[s[end]] == 0:
                        count -= 1
                end+=1
            #start pointer
            while start<end and count == 0:
                if end-start < mx:
                    mx = end-start
                    output = s[start:end]
                if s[start] in lookup:
                    lookup[s[start]] += 1
                    if lookup[s[start]]>0:
                        count += 1
                start+=1
            
        return output

# Add code below this line to test your solution
if __name__ == "__main__":
    # Example 1
    s1 = "ADOBECODEBANC"
    t1 = "ABC"
    solution = Solution()
    result1 = solution.minWindow(s1, t1)
    print(f"Example 1: s = \"{s1}\", t = \"{t1}\"")
    print(f"Output: \"{result1}\"")
    print("-" * 20)

    # Example 2
    s2 = "a"
    t2 = "a"
    result2 = solution.minWindow(s2, t2)
    print(f"Example 2: s = \"{s2}\", t = \"{t2}\"")
    print(f"Output: \"{result2}\"")
    print("-" * 20)

    # Example 3
    s3 = "a"
    t3 = "aa"
    result3 = solution.minWindow(s3, t3)
    print(f"Example 3: s = \"{s3}\", t = \"{t3}\"")
    print(f"Output: \"{result3}\"")
    print("-" * 20)

    # Example 4 (user input)
    print("Testing with user input...")
    try:
        # Take string s input
        user_s = input("Enter the string s: ")
        
        # Take string t input
        user_t = input("Enter the string t: ")

        user_result = solution.minWindow(user_s, user_t)
        print(f"User Input: s = \"{user_s}\", t = \"{user_t}\"")
        print(f"Output: \"{user_result}\"")

    except Exception as e:
        print(f"Error: {e}")