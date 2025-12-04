class Solution:
    def countCollisions(self, D: str) -> int:
        n = len(D)
        if n == 1:
            return 0
        l, r = 0, n - 1
        while l < r and D[l] == 'L':
            l += 1
        while l < r and D[r] == 'R':
            r -= 1
        if l >= r:
            return 0
        return sum(D[i] != 'S' for i in range(l, r + 1))


# --- Simple tests consistent with repository style (print + assert) ---
if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        # test case format: (input, expected_output)
        ("RLRSLL", 5),       # all except middle 'S' collide
        ("LLRR", 0),         # all cars move away, no collision
        ("SSRSSRLLRSLLRSRSSRLRRRRLLRRLSSRR", 20),
        ("S", 0),            # one stationary car, no collision
        ("R", 0),            # one car to right - no collision
        ("L", 0),            # one car to left - no collision
        ("SRRLL", 2),        # only 'RL' in middle will collide (not leading S)
        ("LSLRRLLS", 5),     # strip outer L and R, middle count collisions
        ("RRS", 1),          # the second R collides with S
        ("SRS", 1),          # only single R in middle collides
        ("RS", 1),           # R collides with S
        ("SR", 0),           # no collision, S first, then R goes away
        ("LS", 0),           # no collision, L leaves
        ("SL", 1),           # L collides with S
        ("LR", 0),           # both leave, zero collision
        ("RLLR", 2)          # RL in middle, both collide once each
    ]
    for i, (D, expected) in enumerate(test_cases, 1):
        out = sol.countCollisions(D)
        print(f"Test {i}: countCollisions({D!r}) -> {out}")
        assert out == expected
    print("All tests passed for countCollisions")