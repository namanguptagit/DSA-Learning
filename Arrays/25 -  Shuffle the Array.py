from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans = [None] *(n*2)
        j=0
        for i in range(0,n):
            ans[j]= nums[i]
            ans[j+1]=nums[i+n]
            j+=2
        return ans


# Simple tests consistent with repository style (print + assert)
def test_shuffle():
    solver = Solution()

    # Test 1: Basic example
    nums1 = [2, 5, 1, 3, 4, 7]
    n1 = 3
    res1 = solver.shuffle(nums1, n1)
    print("Test 1:", nums1, "n =", n1, "->", res1)
    assert res1 == [2, 3, 5, 4, 1, 7]

    # Test 2: Small array
    nums2 = [1, 2]
    n2 = 1
    res2 = solver.shuffle(nums2, n2)
    print("Test 2:", nums2, "n =", n2, "->", res2)
    assert res2 == [1, 2]

    # Test 3: Four elements
    nums3 = [1, 1, 2, 2]
    n3 = 2
    res3 = solver.shuffle(nums3, n3)
    print("Test 3:", nums3, "n =", n3, "->", res3)
    assert res3 == [1, 2, 1, 2]

    # Test 4: Another example
    nums4 = [1, 2, 3, 4, 4, 3, 2, 1]
    n4 = 4
    res4 = solver.shuffle(nums4, n4)
    print("Test 4:", nums4, "n =", n4, "->", res4)
    assert res4 == [1, 4, 2, 3, 3, 2, 4, 1]

    # Test 5: Array with zeros
    nums5 = [0, 1, 0, 1]
    n5 = 2
    res5 = solver.shuffle(nums5, n5)
    print("Test 5:", nums5, "n =", n5, "->", res5)
    assert res5 == [0, 0, 1, 1]

    # Test 6: Array with negative numbers
    nums6 = [-1, 1, -2, 2]
    n6 = 2
    res6 = solver.shuffle(nums6, n6)
    print("Test 6:", nums6, "n =", n6, "->", res6)
    assert res6 == [-1, -2, 1, 2]

    # Test 7: Larger array
    nums7 = [1, 2, 3, 4, 5, 6, 7, 8]
    n7 = 4
    res7 = solver.shuffle(nums7, n7)
    print("Test 7:", nums7, "n =", n7, "->", res7)
    assert res7 == [1, 5, 2, 6, 3, 7, 4, 8]

    # Test 8: All same elements
    nums8 = [5, 5, 5, 5]
    n8 = 2
    res8 = solver.shuffle(nums8, n8)
    print("Test 8:", nums8, "n =", n8, "->", res8)
    assert res8 == [5, 5, 5, 5]

    print("All tests passed!")


if __name__ == "__main__":
    test_shuffle()