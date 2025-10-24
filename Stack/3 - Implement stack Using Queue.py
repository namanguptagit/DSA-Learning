from collections import deque


class MyStack:

    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        self.q.append(x)
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self) -> int:
        return self.q.popleft()
        
    def top(self) -> int:
        return self.q[0]

    def empty(self) -> bool:
        return len(self.q) == 0


# Simple tests consistent with repository style (print + assert)
def test_myStack():
    # Test 1: Basic operations
    s1 = MyStack()
    s1.push(1)
    s1.push(2)
    top1 = s1.top()
    pop1 = s1.pop()
    empty1 = s1.empty()
    print("Test 1: push(1), push(2), top(), pop(), empty() ->", top1, pop1, empty1)
    assert top1 == 2
    assert pop1 == 2
    assert empty1 is False

    # Test 2: Empty stack
    s2 = MyStack()
    empty2 = s2.empty()
    print("Test 2: empty() on empty stack ->", empty2)
    assert empty2 is True

    # Test 3: Single element
    s3 = MyStack()
    s3.push(5)
    top3 = s3.top()
    pop3 = s3.pop()
    empty3 = s3.empty()
    print("Test 3: push(5), top(), pop(), empty() ->", top3, pop3, empty3)
    assert top3 == 5
    assert pop3 == 5
    assert empty3 is True

    # Test 4: Multiple elements LIFO order
    s4 = MyStack()
    s4.push(1)
    s4.push(2)
    s4.push(3)
    pop4_1 = s4.pop()
    pop4_2 = s4.pop()
    pop4_3 = s4.pop()
    empty4 = s4.empty()
    print("Test 4: push(1,2,3), pop(), pop(), pop(), empty() ->", pop4_1, pop4_2, pop4_3, empty4)
    assert pop4_1 == 3
    assert pop4_2 == 2
    assert pop4_3 == 1
    assert empty4 is True

    # Test 5: Push after pop
    s5 = MyStack()
    s5.push(1)
    s5.push(2)
    s5.pop()
    s5.push(3)
    top5 = s5.top()
    pop5 = s5.pop()
    print("Test 5: push(1,2), pop(), push(3), top(), pop() ->", top5, pop5)
    assert top5 == 3
    assert pop5 == 3

    # Test 6: Large sequence
    s6 = MyStack()
    for i in range(5):
        s6.push(i)
    
    results6 = []
    for i in range(3):
        results6.append(s6.pop())
    
    s6.push(10)
    results6.append(s6.pop())
    results6.append(s6.empty())
    
    print("Test 6: push(0,1,2,3,4), pop(3), push(10), pop(), empty() ->", results6)
    assert results6 == [4, 3, 2, 10, False]

    # Test 7: Top without pop
    s7 = MyStack()
    s7.push(7)
    s7.push(8)
    top7_1 = s7.top()
    top7_2 = s7.top()
    pop7 = s7.pop()
    print("Test 7: push(7,8), top(), top(), pop() ->", top7_1, top7_2, pop7)
    assert top7_1 == 8
    assert top7_2 == 8
    assert pop7 == 8

    # Test 8: Zero and negative numbers
    s8 = MyStack()
    s8.push(0)
    s8.push(-1)
    s8.push(1)
    pop8_1 = s8.pop()
    pop8_2 = s8.pop()
    pop8_3 = s8.pop()
    print("Test 8: push(0,-1,1), pop(), pop(), pop() ->", pop8_1, pop8_2, pop8_3)
    assert pop8_1 == 1
    assert pop8_2 == -1
    assert pop8_3 == 0

    # Test 9: Multiple top calls
    s9 = MyStack()
    s9.push(10)
    s9.push(20)
    top9_1 = s9.top()
    top9_2 = s9.top()
    top9_3 = s9.top()
    print("Test 9: push(10,20), top(), top(), top() ->", top9_1, top9_2, top9_3)
    assert top9_1 == 20
    assert top9_2 == 20
    assert top9_3 == 20

    # Test 10: Mixed operations
    s10 = MyStack()
    s10.push(1)
    s10.push(2)
    top10_1 = s10.top()
    s10.push(3)
    pop10_1 = s10.pop()
    top10_2 = s10.top()
    pop10_2 = s10.pop()
    empty10 = s10.empty()
    print("Test 10: push(1,2), top(), push(3), pop(), top(), pop(), empty() ->", top10_1, pop10_1, top10_2, pop10_2, empty10)
    assert top10_1 == 2
    assert pop10_1 == 3
    assert top10_2 == 2
    assert pop10_2 == 2
    assert empty10 is False

    print("All tests passed!")


if __name__ == "__main__":
    test_myStack()