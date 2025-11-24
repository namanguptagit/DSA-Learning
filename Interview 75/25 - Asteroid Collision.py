class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        j = 0
        n = len(asteroids)

        for i in range(n):
            asteroid = asteroids[i]
            while j > 0 and asteroids[j - 1] > 0 and asteroid < 0 and asteroids[j - 1] < abs(asteroid):
                j -= 1

            if j == 0 or asteroid > 0 or asteroids[j - 1] < 0:
                asteroids[j] = asteroid
                j += 1
            elif asteroids[j - 1] == abs(asteroid):
                j -= 1
        return asteroids[:j]

# Simple tests consistent with repository style (print + assert)
def test_asteroidCollision():
    solver = Solution()
    # Test 1: Example case
    asteroids1 = [5,10,-5]
    expected1 = [5,10]
    out1 = solver.asteroidCollision(asteroids1[:])
    print("Test 1:", out1)
    assert out1 == expected1

    # Test 2: Example from LeetCode, both annihilate
    asteroids2 = [8,-8]
    expected2 = []
    out2 = solver.asteroidCollision(asteroids2[:])
    print("Test 2:", out2)
    assert out2 == expected2

    # Test 3: More on left survive
    asteroids3 = [10,2,-5]
    expected3 = [10]
    out3 = solver.asteroidCollision(asteroids3[:])
    print("Test 3:", out3)
    assert out3 == expected3

    # Test 4: All right, no collision
    asteroids4 = [-2,-1,1,2]
    expected4 = [-2,-1,1,2]
    out4 = solver.asteroidCollision(asteroids4[:])
    print("Test 4:", out4)
    assert out4 == expected4

    # Test 5: Many same magnitude
    asteroids5 = [1,-1,1,-1]
    expected5 = []
    out5 = solver.asteroidCollision(asteroids5[:])
    print("Test 5:", out5)
    assert out5 == expected5

    # Test 6: No collisions (all moving right)
    asteroids6 = [1,2,3,4,5]
    expected6 = [1,2,3,4,5]
    out6 = solver.asteroidCollision(asteroids6[:])
    print("Test 6:", out6)
    assert out6 == expected6

    # Test 7: No collisions (all moving left)
    asteroids7 = [-1,-2,-3,-4,-5]
    expected7 = [-1,-2,-3,-4,-5]
    out7 = solver.asteroidCollision(asteroids7[:])
    print("Test 7:", out7)
    assert out7 == expected7

    # Test 8: Empty input
    asteroids8 = []
    expected8 = []
    out8 = solver.asteroidCollision(asteroids8[:])
    print("Test 8:", out8)
    assert out8 == expected8

    print("All tests passed for asteroidCollision.")

if __name__ == "__main__":
    # Needed for List typing
    from typing import List
    test_asteroidCollision()