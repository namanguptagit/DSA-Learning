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