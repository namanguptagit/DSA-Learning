class MyQueue:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x):
        while self.s1:
            self.s2.append(self.s1.pop())
        self.s1.append(x)
        while self.s2:
            self.s1.append(self.s2.pop())

    def pop(self):
        return self.s1.pop()

    def peek(self):
        return self.s1[-1]

    def empty(self):
        return not self.s1


# Simple tests consistent with repository style (print + assert)
def test_myQueue():
    # Test 1: Basic operations
    q1 = MyQueue()
    q1.push(1)
    q1.push(2)
    peek1 = q1.peek()
    pop1 = q1.pop()
    empty1 = q1.empty()
    print("Test 1: push(1), push(2), peek(), pop(), empty() ->", peek1, pop1, empty1)
    assert peek1 == 2
    assert pop1 == 1
    assert empty1 is False

    # Test 2: Empty queue
    q2 = MyQueue()
    empty2 = q2.empty()
    print("Test 2: empty() on empty queue ->", empty2)
    assert empty2 is True

    # Test 3: Single element
    q3 = MyQueue()
    q3.push(5)
    peek3 = q3.peek()
    pop3 = q3.pop()
    empty3 = q3.empty()
    print("Test 3: push(5), peek(), pop(), empty() ->", peek3, pop3, empty3)
    assert peek3 == 5
    assert pop3 == 5
    assert empty3 is True

    # Test 4: Multiple elements FIFO order
    q4 = MyQueue()
    q4.push(1)
    q4.push(2)
    q4.push(3)
    pop4_1 = q4.pop()
    pop4_2 = q4.pop()
    pop4_3 = q4.pop()
    empty4 = q4.empty()
    print("Test 4: push(1,2,3), pop(), pop(), pop(), empty() ->", pop4_1, pop4_2, pop4_3, empty4)
    assert pop4_1 == 1
    assert pop4_2 == 2
    assert pop4_3 == 3
    assert empty4 is True

    # Test 5: Push after pop
    q5 = MyQueue()
    q5.push(1)
    q5.push(2)
    q5.pop()
    q5.push(3)
    peek5 = q5.peek()
    pop5 = q5.pop()
    print("Test 5: push(1,2), pop(), push(3), peek(), pop() ->", peek5, pop5)
    assert peek5 == 3
    assert pop5 == 2

    # Test 6: Large sequence
    q6 = MyQueue()
    for i in range(5):
        q6.push(i)
    
    results6 = []
    for i in range(3):
        results6.append(q6.pop())
    
    q6.push(10)
    results6.append(q6.pop())
    results6.append(q6.empty())
    
    print("Test 6: push(0,1,2,3,4), pop(3), push(10), pop(), empty() ->", results6)
    assert results6 == [0, 1, 2, 10, False]

    # Test 7: Peek without pop
    q7 = MyQueue()
    q7.push(7)
    q7.push(8)
    peek7_1 = q7.peek()
    peek7_2 = q7.peek()
    pop7 = q7.pop()
    print("Test 7: push(7,8), peek(), peek(), pop() ->", peek7_1, peek7_2, pop7)
    assert peek7_1 == 8
    assert peek7_2 == 8
    assert pop7 == 7

    # Test 8: Zero and negative numbers
    q8 = MyQueue()
    q8.push(0)
    q8.push(-1)
    q8.push(1)
    pop8_1 = q8.pop()
    pop8_2 = q8.pop()
    pop8_3 = q8.pop()
    print("Test 8: push(0,-1,1), pop(), pop(), pop() ->", pop8_1, pop8_2, pop8_3)
    assert pop8_1 == 0
    assert pop8_2 == -1
    assert pop8_3 == 1

    print("All tests passed!")


if __name__ == "__main__":
    test_myQueue()