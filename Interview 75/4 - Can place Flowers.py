from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        for i in range(len(flowerbed)):
            # Check if the current plot is empty.
            if flowerbed[i] == 0:
                # Check if the left and right plots are empty.
                empty_left_plot = (i == 0) or (flowerbed[i - 1] == 0)
                empty_right_lot = (i == len(flowerbed) - 1) or (flowerbed[i + 1] == 0)

                # If both plots are empty, we can plant a flower here.
                if empty_left_plot and empty_right_lot:
                    flowerbed[i] = 1
                    count += 1
                    if count >= n:
                        return True

        return count >= n


# Simple tests consistent with repository style (print + assert)
def test_canPlaceFlowers():
    solver = Solution()

    # Test 1: Basic example where planting is possible
    flowerbed1 = [1, 0, 0, 0, 1]
    n1 = 1
    res1 = solver.canPlaceFlowers(flowerbed1.copy(), n1)
    print("Test 1: flowerbed =", flowerbed1, "n =", n1, "->", res1)
    assert res1 is True

    # Test 2: Planting more than allowed
    flowerbed2 = [1, 0, 0, 0, 1]
    n2 = 2
    res2 = solver.canPlaceFlowers(flowerbed2.copy(), n2)
    print("Test 2: flowerbed =", flowerbed2, "n =", n2, "->", res2)
    assert res2 is False

    # Test 3: Single empty plot
    flowerbed3 = [0]
    n3 = 1
    res3 = solver.canPlaceFlowers(flowerbed3.copy(), n3)
    print("Test 3: flowerbed =", flowerbed3, "n =", n3, "->", res3)
    assert res3 is True

    # Test 4: Single occupied plot
    flowerbed4 = [1]
    n4 = 1
    res4 = solver.canPlaceFlowers(flowerbed4.copy(), n4)
    print("Test 4: flowerbed =", flowerbed4, "n =", n4, "->", res4)
    assert res4 is False

    # Test 5: Multiple empty plots
    flowerbed5 = [0, 0, 0, 0, 0]
    n5 = 2
    res5 = solver.canPlaceFlowers(flowerbed5.copy(), n5)
    print("Test 5: flowerbed =", flowerbed5, "n =", n5, "->", res5)
    assert res5 is True

    # Test 6: No planting needed
    flowerbed6 = [1, 0, 0, 0, 1]
    n6 = 0
    res6 = solver.canPlaceFlowers(flowerbed6.copy(), n6)
    print("Test 6: flowerbed =", flowerbed6, "n =", n6, "->", res6)
    assert res6 is True

    # Test 7: Planting at edges
    flowerbed7 = [0, 0, 1, 0, 0]
    n7 = 2
    res7 = solver.canPlaceFlowers(flowerbed7.copy(), n7)
    print("Test 7: flowerbed =", flowerbed7, "n =", n7, "->", res7)
    assert res7 is True

    # Test 8: Not enough space due to adjacency
    flowerbed8 = [0, 1, 0, 1, 0]
    n8 = 1
    res8 = solver.canPlaceFlowers(flowerbed8.copy(), n8)
    print("Test 8: flowerbed =", flowerbed8, "n =", n8, "->", res8)
    assert res8 is False

    # Test 9: Large n compared to available spaces
    flowerbed9 = [0, 0, 1, 0, 0, 0, 1, 0, 0]
    n9 = 3
    res9 = solver.canPlaceFlowers(flowerbed9.copy(), n9)
    print("Test 9: flowerbed =", flowerbed9, "n =", n9, "->", res9)
    assert res9 is True

    # Test 10: Alternating pattern
    flowerbed10 = [0, 1, 0, 1, 0, 1, 0]
    n10 = 1
    res10 = solver.canPlaceFlowers(flowerbed10.copy(), n10)
    print("Test 10: flowerbed =", flowerbed10, "n =", n10, "->", res10)
    assert res10 is False

    print("All tests passed!")


if __name__ == "__main__":
    test_canPlaceFlowers()