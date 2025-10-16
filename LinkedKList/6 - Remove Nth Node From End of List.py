from typing import Optional


# Definition for singly-linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        first = dummy
        second = dummy

        for _ in range(n + 1):
            first = first.next

        while first is not None:
            first = first.next
            second = second.next

        second.next = second.next.next

        return dummy.next


# Helper function to create a linked list from a list of values
def create_linked_list(values):
    if not values:
        return None

    head = ListNode(values[0])
    current = head

    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next

    return head


# Helper function to convert linked list to list for easy comparison
def linked_list_to_list(head):
    result = []
    current = head

    while current:
        result.append(current.val)
        current = current.next

    return result


# Test cases (matching style used in other LinkedList files)
def test_removeNthFromEnd():
    solution = Solution()

    # Test Case 1: Remove 2nd from end in [1,2,3,4,5] -> [1,2,3,5]
    print("Test Case 1: [1,2,3,4,5], n=2")
    head1 = create_linked_list([1, 2, 3, 4, 5])
    result1 = solution.removeNthFromEnd(head1, 2)
    list1 = linked_list_to_list(result1)
    expected1 = [1, 2, 3, 5]
    print(f"Output: {list1}")
    print(f"Expected: {expected1}")
    assert list1 == expected1, "Test Case 1 failed"
    print("\u2713 Passed\n")

    # Test Case 2: Single node [1], n=1 -> []
    print("Test Case 2: [1], n=1")
    head2 = create_linked_list([1])
    result2 = solution.removeNthFromEnd(head2, 1)
    list2 = linked_list_to_list(result2)
    expected2 = []
    print(f"Output: {list2}")
    print(f"Expected: {expected2}")
    assert list2 == expected2, "Test Case 2 failed"
    print("\u2713 Passed\n")

    # Test Case 3: Remove head when n equals length [1,2], n=2 -> [2]
    print("Test Case 3: [1,2], n=2")
    head3 = create_linked_list([1, 2])
    result3 = solution.removeNthFromEnd(head3, 2)
    list3 = linked_list_to_list(result3)
    expected3 = [2]
    print(f"Output: {list3}")
    print(f"Expected: {expected3}")
    assert list3 == expected3, "Test Case 3 failed"
    print("\u2713 Passed\n")

    # Test Case 4: Remove tail [1,2], n=1 -> [1]
    print("Test Case 4: [1,2], n=1")
    head4 = create_linked_list([1, 2])
    result4 = solution.removeNthFromEnd(head4, 1)
    list4 = linked_list_to_list(result4)
    expected4 = [1]
    print(f"Output: {list4}")
    print(f"Expected: {expected4}")
    assert list4 == expected4, "Test Case 4 failed"
    print("\u2713 Passed\n")

    # Test Case 5: Longer list remove head [1,2,3], n=3 -> [2,3]
    print("Test Case 5: [1,2,3], n=3")
    head5 = create_linked_list([1, 2, 3])
    result5 = solution.removeNthFromEnd(head5, 3)
    list5 = linked_list_to_list(result5)
    expected5 = [2, 3]
    print(f"Output: {list5}")
    print(f"Expected: {expected5}")
    assert list5 == expected5, "Test Case 5 failed"
    print("\u2713 Passed\n")

    print("\ud83c\udf89 All test cases passed!")


if __name__ == "__main__":
    test_removeNthFromEnd()