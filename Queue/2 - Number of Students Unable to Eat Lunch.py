class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        count0 = students.count(0)
        count1 = len(students) - count0
        
        for s in sandwiches:
            if s == 0:
                if count0 == 0:
                    return count1
                count0 -= 1
            else:
                if count1 == 0:
                    return count0
                count1 -= 1
        return 0

# Simple tests consistent with repository style (print + assert)
def test_countStudents():
    solver = Solution()

    # Test 1: all students want sandwiches in order
    students1 = [1,1,0,0]
    sandwiches1 = [0,1,0,1]
    res1 = solver.countStudents(students1.copy(), sandwiches1.copy())
    print("Test 1:", res1)
    assert res1 == 0

    # Test 2: all get sandwich except one
    students2 = [1,1,1,0,0,1]
    sandwiches2 = [1,0,0,0,1,1]
    res2 = solver.countStudents(students2.copy(), sandwiches2.copy())
    print("Test 2:", res2)
    assert res2 == 3

    # Test 3: all want 1, all sandwiches are 1
    students3 = [1,1,1]
    sandwiches3 = [1,1,1]
    res3 = solver.countStudents(students3.copy(), sandwiches3.copy())
    print("Test 3:", res3)
    assert res3 == 0

    # Test 4: no sandwich can be given
    students4 = [0,0,0]
    sandwiches4 = [1,1,1]
    res4 = solver.countStudents(students4.copy(), sandwiches4.copy())
    print("Test 4:", res4)
    assert res4 == 3

    # Test 5: empty input
    students5 = []
    sandwiches5 = []
    res5 = solver.countStudents(students5.copy(), sandwiches5.copy())
    print("Test 5:", res5)
    assert res5 == 0

    # Test 6: single student matches
    students6 = [0]
    sandwiches6 = [0]
    res6 = solver.countStudents(students6.copy(), sandwiches6.copy())
    print("Test 6:", res6)
    assert res6 == 0

    # Test 7: one student does not match
    students7 = [0]
    sandwiches7 = [1]
    res7 = solver.countStudents(students7.copy(), sandwiches7.copy())
    print("Test 7:", res7)
    assert res7 == 1

    print("All tests passed for countStudents.")

if __name__ == "__main__":
    test_countStudents()