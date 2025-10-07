from typing import List

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

# Add code below this line to test your solution
if __name__ == "__main__":
    # Example 1
    cardPoints1 = [1, 2, 3, 4, 5, 6, 1]
    k1 = 3
    solution = Solution()
    result1 = solution.maxScore(cardPoints1, k1)
    print(f"Example 1: cardPoints = {cardPoints1}, k = {k1}")
    print(f"Output: {result1}")
    print("-" * 20)

    # Example 2
    cardPoints2 = [2, 2, 2]
    k2 = 2
    result2 = solution.maxScore(cardPoints2, k2)
    print(f"Example 2: cardPoints = {cardPoints2}, k = {k2}")
    print(f"Output: {result2}")
    print("-" * 20)

    # Example 3
    cardPoints3 = [9, 7, 7, 9, 7, 7, 9]
    k3 = 7
    result3 = solution.maxScore(cardPoints3, k3)
    print(f"Example 3: cardPoints = {cardPoints3}, k = {k3}")
    print(f"Output: {result3}")
    print("-" * 20)

    # Example 4
    cardPoints4 = [1, 1000, 1]
    k4 = 1
    result4 = solution.maxScore(cardPoints4, k4)
    print(f"Example 4: cardPoints = {cardPoints4}, k = {k4}")
    print(f"Output: {result4}")
    print("-" * 20)

    # Example 5 (user input)
    print("Testing with user input...")
    try:
        # Take list input
        user_cards_str = input("Enter a list of card points separated by spaces (e.g., 1 2 3 4 5 6 1): ")
        user_cards = list(map(int, user_cards_str.split()))
        
        # Take k input
        user_k = int(input("Enter the number of cards to pick: "))

        user_result = solution.maxScore(user_cards, user_k)
        print(f"User Input: cardPoints = {user_cards}, k = {user_k}")
        print(f"Output: {user_result}")

    except ValueError:
        print("Invalid input. Please enter valid numbers.")