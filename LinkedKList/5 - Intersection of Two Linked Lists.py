from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        one = headA
        two = headB

        while one != two:
            one = headB if one is None else one.next
            two = headA if two is None else two.next
        return one

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

# Helper function to create two linked lists with intersection
def create_intersection(listA_values, listB_values, intersection_values):
    """Helper function to create two linked lists with intersection"""
    # Create the intersection part
    intersection_head = create_linked_list(intersection_values)
    
    # Create list A
    if listA_values:
        headA = ListNode(listA_values[0])
        current = headA
        for val in listA_values[1:]:
            current.next = ListNode(val)
            current = current.next
        current.next = intersection_head
    else:
        headA = intersection_head
    
    # Create list B
    if listB_values:
        headB = ListNode(listB_values[0])
        current = headB
        for val in listB_values[1:]:
            current.next = ListNode(val)
            current = current.next
        current.next = intersection_head
    else:
        headB = intersection_head
    
    return headA, headB, intersection_head

# Helper function to convert linked list to list for easy comparison
def linked_list_to_list(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

# Test cases
def test_intersection_of_linked_lists():
    solution = Solution()
    
    # Test Case 1: Basic example with intersection
    print("Test Case 1: Basic example with intersection")
    headA, headB, intersection = create_intersection([4, 1], [5, 6, 1], [8, 4, 5])
    result1 = solution.getIntersectionNode(headA, headB)
    print(f"Input: listA = [4,1,8,4,5], listB = [5,6,1,8,4,5]")
    print(f"Expected intersection value: 8")
    print(f"Got intersection value: {result1.val if result1 else None}")
    print(f"Test 1 {'PASSED' if result1 and result1.val == 8 else 'FAILED'}\n")
    
    # Test Case 2: Another example with intersection
    print("Test Case 2: Another example with intersection")
    headA2, headB2, intersection2 = create_intersection([1, 9, 1], [3], [2, 4])
    result2 = solution.getIntersectionNode(headA2, headB2)
    print(f"Input: listA = [1,9,1,2,4], listB = [3,2,4]")
    print(f"Expected intersection value: 2")
    print(f"Got intersection value: {result2.val if result2 else None}")
    print(f"Test 2 {'PASSED' if result2 and result2.val == 2 else 'FAILED'}\n")
    
    # Test Case 3: No intersection
    print("Test Case 3: No intersection")
    headA3 = create_linked_list([2, 6, 4])
    headB3 = create_linked_list([1, 5])
    result3 = solution.getIntersectionNode(headA3, headB3)
    print(f"Input: listA = [2,6,4], listB = [1,5]")
    print(f"Expected: None")
    print(f"Got: {result3}")
    print(f"Test 3 {'PASSED' if result3 is None else 'FAILED'}\n")
    
    # Test Case 4: Same lists (identical references)
    print("Test Case 4: Same lists")
    headA4 = create_linked_list([1, 2, 3])
    headB4 = headA4  # Same reference
    result4 = solution.getIntersectionNode(headA4, headB4)
    print(f"Input: listA = [1,2,3], listB = [1,2,3] (same reference)")
    print(f"Expected intersection value: 1")
    print(f"Got intersection value: {result4.val if result4 else None}")
    print(f"Test 4 {'PASSED' if result4 and result4.val == 1 else 'FAILED'}\n")
    
    # Test Case 5: Intersection at end
    print("Test Case 5: Intersection at end")
    headA5, headB5, intersection5 = create_intersection([1, 2], [3, 4], [5])
    result5 = solution.getIntersectionNode(headA5, headB5)
    print(f"Input: listA = [1,2,5], listB = [3,4,5]")
    print(f"Expected intersection value: 5")
    print(f"Got intersection value: {result5.val if result5 else None}")
    print(f"Test 5 {'PASSED' if result5 and result5.val == 5 else 'FAILED'}\n")
    
    # Test Case 6: Empty lists
    print("Test Case 6: Empty lists")
    result6 = solution.getIntersectionNode(None, None)
    print(f"Input: listA = None, listB = None")
    print(f"Expected: None")
    print(f"Got: {result6}")
    print(f"Test 6 {'PASSED' if result6 is None else 'FAILED'}\n")
    
    # Test Case 7: One empty list
    print("Test Case 7: One empty list")
    headA7 = create_linked_list([1, 2, 3])
    result7 = solution.getIntersectionNode(headA7, None)
    print(f"Input: listA = [1,2,3], listB = None")
    print(f"Expected: None")
    print(f"Got: {result7}")
    print(f"Test 7 {'PASSED' if result7 is None else 'FAILED'}\n")
    
    # Test Case 8: Single node intersection
    print("Test Case 8: Single node intersection")
    headA8, headB8, intersection8 = create_intersection([1, 2, 3], [4, 5], [6])
    result8 = solution.getIntersectionNode(headA8, headB8)
    print(f"Input: listA = [1,2,3,6], listB = [4,5,6]")
    print(f"Expected intersection value: 6")
    print(f"Got intersection value: {result8.val if result8 else None}")
    print(f"Test 8 {'PASSED' if result8 and result8.val == 6 else 'FAILED'}\n")
    
    print("🎉 All test cases completed!")

if __name__ == "__main__":
    test_intersection_of_linked_lists()