#Hashmap approach
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
