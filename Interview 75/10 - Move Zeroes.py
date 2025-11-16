class Solution:
    def moveZeroes(self, nums: list) -> None:
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != 0 and nums[slow] == 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]

            # wait while we find a non-zero element to
            # swap with you
            if nums[slow] != 0:
                slow += 1

# Simple tests consistent with repository style (print + assert)
def test_moveZeroes():
    solver = Solution()

    # Test 1: Basic example
    lst1 = [0,1,0,3,12]
    solver.moveZeroes(lst1)
    print("Test 1:", lst1)
    assert lst1 == [1,3,12,0,0]

    # Test 2: No zeros
    lst2 = [1,2,3]
    solver.moveZeroes(lst2)
    print("Test 2:", lst2)
    assert lst2 == [1,2,3]

    # Test 3: All zeros
    lst3 = [0,0,0]
    solver.moveZeroes(lst3)
    print("Test 3:", lst3)
    assert lst3 == [0,0,0]

    # Test 4: Zeros at the end
    lst4 = [1,2,3,0,0]
    solver.moveZeroes(lst4)
    print("Test 4:", lst4)
    assert lst4 == [1,2,3,0,0]

    # Test 5: Zeros at the start
    lst5 = [0,0,1,2,3]
    solver.moveZeroes(lst5)
    print("Test 5:", lst5)
    assert lst5 == [1,2,3,0,0]

    # Test 6: Single element zero
    lst6 = [0]
    solver.moveZeroes(lst6)
    print("Test 6:", lst6)
    assert lst6 == [0]

    # Test 7: Single element non-zero
    lst7 = [7]
    solver.moveZeroes(lst7)
    print("Test 7:", lst7)
    assert lst7 == [7]

    # Test 8: Empty list
    lst8 = []
    solver.moveZeroes(lst8)
    print("Test 8:", lst8)
    assert lst8 == []

    print("All tests passed for moveZeroes.")

if __name__ == "__main__":
    test_moveZeroes()