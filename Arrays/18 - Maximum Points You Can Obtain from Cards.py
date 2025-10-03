class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        total = sum(cardPoints)

        if k == n:
            return total

        window_size = n - k
        curr = sum(cardPoints[:window_size])
        min_window = curr

        for i in range(window_size, n):
            curr += cardPoints[i] - cardPoints[i - window_size]
            min_window = min(min_window, curr)

        return total - min_window