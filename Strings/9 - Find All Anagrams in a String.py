#Hashmap approach
from collections import Counter
from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res=[]
        hashmap=Counter(p)
        for i in range(len(s)-len(p)+1):
            if Counter(s[i:i+len(p)])==hashmap:
                res.append(i)
        return res 

#Sliding window approach
from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        len_p = len(p)
        len_s = len(s)
        if len_p > len_s:
            return res
        
        p_count = Counter(p)
        window = Counter(s[:len_p - 1])  # initial window of size len(p)-1
        
        for i in range(len_p - 1, len_s):
            # include next character in window
            window[s[i]] += 1
            
            # check window
            if window == p_count:
                res.append(i - len_p + 1)
            
            # remove leftmost character
            left_char = s[i - len_p + 1]
            window[left_char] -= 1
            if window[left_char] == 0:
                del window[left_char]
        
            # slide window
        return res

# Add code below this line to test your solution
if __name__ == "__main__":
    # Example 1 - Hashmap Approach
    s1 = "cbaebabacd"
    p1 = "abc"
    solution1 = Solution()
    result1 = solution1.findAnagrams(s1, p1)
    print(f"Example 1 (Hashmap): s = \"{s1}\", p = \"{p1}\"")
    print(f"Output: {result1}")
    print("-" * 20)

    # Example 2 - Hashmap Approach
    s2 = "abab"
    p2 = "ab"
    result2 = solution1.findAnagrams(s2, p2)
    print(f"Example 2 (Hashmap): s = \"{s2}\", p = \"{p2}\"")
    print(f"Output: {result2}")
    print("-" * 20)

    # Example 1 - Sliding Window Approach
    s3 = "cbaebabacd"
    p3 = "abc"
    solution2 = Solution()
    result3 = solution2.findAnagrams(s3, p3)
    print(f"Example 1 (Sliding Window): s = \"{s3}\", p = \"{p3}\"")
    print(f"Output: {result3}")
    print("-" * 20)

    # Example 2 - Sliding Window Approach
    s4 = "abab"
    p4 = "ab"
    result4 = solution2.findAnagrams(s4, p4)
    print(f"Example 2 (Sliding Window): s = \"{s4}\", p = \"{p4}\"")
    print(f"Output: {result4}")
    print("-" * 20)

    # Example 3 (user input)
    print("Testing with user input...")
    try:
        # Take string s input
        user_s = input("Enter the string s: ")
        
        # Take string p input
        user_p = input("Enter the string p: ")

        user_result = solution2.findAnagrams(user_s, user_p)
        print(f"User Input: s = \"{user_s}\", p = \"{user_p}\"")
        print(f"Output: {user_result}")

    except Exception as e:
        print(f"Error: {e}")
