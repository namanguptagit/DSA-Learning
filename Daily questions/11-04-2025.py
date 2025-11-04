from typing import List


class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        def x_sum(freq):
            freq2=sorted(freq, reverse=True)
            Sum=0
            for f, num in freq2[:x]:
                if f==0: break
                Sum+=num*f
            return Sum
        n=len(nums)
        sz=n-k+1
        ans=[0]*sz
        freq=[[0, 0] for _ in range(51)]
        for z in nums[:k]:
            freq[z][1]=z
            freq[z][0]+=1
        ans[0]=x_sum(freq)
        for l in range(1, sz):
            L, R=nums[l-1], nums[l+k-1]
            freq[L][0]-=1
            freq[R][0]+=1
            freq[R][1]=R
            ans[l]=x_sum(freq)
        return ans


# Simple tests consistent with repository style (print + assert)
def test_findXSum():
    solver = Solution()

    # Test 1: Basic increasing numbers, k=2, x=1 (pick larger in each window)
    nums1, k1, x1 = [1, 2, 3, 4], 2, 1
    res1 = solver.findXSum(nums1, k1, x1)
    print("Test 1:", nums1, "k=", k1, "x=", x1, "->", res1)
    assert res1 == [2, 3, 4]

    # Test 2: Basic increasing numbers, k=2, x=2 (sum both since all unique)
    nums2, k2, x2 = [1, 2, 3, 4], 2, 2
    res2 = solver.findXSum(nums2, k2, x2)
    print("Test 2:", nums2, "k=", k2, "x=", x2, "->", res2)
    assert res2 == [3, 5, 7]

    # Test 3: Repeated elements, favor higher frequency times value
    nums3, k3, x3 = [1, 1, 2, 2], 3, 1
    res3 = solver.findXSum(nums3, k3, x3)
    print("Test 3:", nums3, "k=", k3, "x=", x3, "->", res3)
    assert res3 == [2, 4]

    # Test 4: Whole array as one window
    nums4, k4, x4 = [2, 2, 3], 3, 1
    res4 = solver.findXSum(nums4, k4, x4)
    print("Test 4:", nums4, "k=", k4, "x=", x4, "->", res4)
    # freq: 2->2, 3->1 => pick 2: 2*2=4
    assert res4 == [4]

    # Test 5: k=1 returns each element (x>=1)
    nums5, k5, x5 = [5, 1, 4], 1, 3
    res5 = solver.findXSum(nums5, k5, x5)
    print("Test 5:", nums5, "k=", k5, "x=", x5, "->", res5)
    assert res5 == [5, 1, 4]

    # Test 6: Mixed window with ties on frequency, prefer larger number first
    nums6, k6, x6 = [1, 2, 1, 2], 3, 1
    res6 = solver.findXSum(nums6, k6, x6)
    print("Test 6:", nums6, "k=", k6, "x=", x6, "->", res6)
    # Window [1,2,1]: freq 1->2,2->1 => pick 1 => 2
    # Window [2,1,2]: freq 2->2,1->1 => pick 2 => 4
    assert res6 == [2, 4]

    # Test 7: x larger than unique count, should stop when f==0
    nums7, k7, x7 = [0, 1, 0], 2, 5
    res7 = solver.findXSum(nums7, k7, x7)
    print("Test 7:", nums7, "k=", k7, "x=", x7, "->", res7)
    # [0,1] -> pick 1 => 1; [1,0] -> pick 1 => 1
    assert res7 == [1, 1]

    print("All tests passed!")


if __name__ == "__main__":
    test_findXSum()
