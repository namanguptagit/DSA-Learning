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
            # if it’s a new character, increment distinct count
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