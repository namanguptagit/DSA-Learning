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