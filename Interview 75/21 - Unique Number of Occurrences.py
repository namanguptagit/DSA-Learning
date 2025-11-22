class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq = {}
        for x in arr:
            freq[x] = freq.get(x, 0) + 1

        return len(freq) == len(set(freq.values()))
        # Simple tests consistent with repository style (print + assert)
        def test_uniqueOccurrences():
            solver = Solution()

            # Test 1: Distinct frequencies
            arr1 = [1,2,2,1,1,3]
            expected1 = True
            out1 = solver.uniqueOccurrences(arr1)
            print("Test 1:", out1)
            assert out1 == expected1

            # Test 2: Not unique frequencies
            arr2 = [1,2]
            expected2 = False
            out2 = solver.uniqueOccurrences(arr2)
            print("Test 2:", out2)
            assert out2 == expected2

            # Test 3: All numbers same
            arr3 = [7,7,7,7]
            expected3 = True
            out3 = solver.uniqueOccurrences(arr3)
            print("Test 3:", out3)
            assert out3 == expected3

            # Test 4: Negative and zero values, unique
            arr4 = [0,-1,-1,2,2,2]
            expected4 = True
            out4 = solver.uniqueOccurrences(arr4)
            print("Test 4:", out4)
            assert out4 == expected4

            # Test 5: Negative and zero values, not unique
            arr5 = [0,0,-2,-2,3,3]
            expected5 = False
            out5 = solver.uniqueOccurrences(arr5)
            print("Test 5:", out5)
            assert out5 == expected5

            # Test 6: Empty list
            arr6 = []
            expected6 = True  # vacuously true
            out6 = solver.uniqueOccurrences(arr6)
            print("Test 6:", out6)
            assert out6 == expected6

            # Test 7: One element
            arr7 = [42]
            expected7 = True
            out7 = solver.uniqueOccurrences(arr7)
            print("Test 7:", out7)
            assert out7 == expected7

            # Test 8: Multiple frequencies, not all unique
            arr8 = [4,4,2,2,4,2,3,3]
            expected8 = False
            out8 = solver.uniqueOccurrences(arr8)
            print("Test 8:", out8)
            assert out8 == expected8

            print("All tests passed for uniqueOccurrences.")

        if __name__ == "__main__":
            test_uniqueOccurrences()