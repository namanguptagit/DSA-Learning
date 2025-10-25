from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans=[]
        def inorder(root,ans):
            if not root:
                return None
            inorder(root.left,ans)
            inorder(root.right,ans)
            ans.append(root.val)
        inorder(root,ans)
        return ans


# Simple tests consistent with repository style (print + assert)
def test_postorderTraversal():
    solver = Solution()

    # Test 1: Empty tree
    root1 = None
    res1 = solver.postorderTraversal(root1)
    print("Test 1: Empty tree ->", res1)
    assert res1 == []

    # Test 2: Single node
    root2 = TreeNode(1)
    res2 = solver.postorderTraversal(root2)
    print("Test 2: Single node ->", res2)
    assert res2 == [1]

    # Test 3: Two nodes (left child)
    root3 = TreeNode(1)
    root3.left = TreeNode(2)
    res3 = solver.postorderTraversal(root3)
    print("Test 3: Two nodes (left child) ->", res3)
    assert res3 == [2, 1]

    # Test 4: Two nodes (right child)
    root4 = TreeNode(1)
    root4.right = TreeNode(2)
    res4 = solver.postorderTraversal(root4)
    print("Test 4: Two nodes (right child) ->", res4)
    assert res4 == [2, 1]

    # Test 5: Three nodes (both children)
    root5 = TreeNode(1)
    root5.left = TreeNode(2)
    root5.right = TreeNode(3)
    res5 = solver.postorderTraversal(root5)
    print("Test 5: Three nodes (both children) ->", res5)
    assert res5 == [2, 3, 1]

    # Test 6: Left skewed tree
    root6 = TreeNode(1)
    root6.left = TreeNode(2)
    root6.left.left = TreeNode(3)
    root6.left.left.left = TreeNode(4)
    res6 = solver.postorderTraversal(root6)
    print("Test 6: Left skewed tree ->", res6)
    assert res6 == [4, 3, 2, 1]

    # Test 7: Right skewed tree
    root7 = TreeNode(1)
    root7.right = TreeNode(2)
    root7.right.right = TreeNode(3)
    root7.right.right.right = TreeNode(4)
    res7 = solver.postorderTraversal(root7)
    print("Test 7: Right skewed tree ->", res7)
    assert res7 == [4, 3, 2, 1]

    # Test 8: Balanced tree
    root8 = TreeNode(1)
    root8.left = TreeNode(2)
    root8.right = TreeNode(3)
    root8.left.left = TreeNode(4)
    root8.left.right = TreeNode(5)
    res8 = solver.postorderTraversal(root8)
    print("Test 8: Balanced tree ->", res8)
    assert res8 == [4, 5, 2, 3, 1]

    # Test 9: Complex tree
    root9 = TreeNode(1)
    root9.left = TreeNode(2)
    root9.right = TreeNode(3)
    root9.left.left = TreeNode(4)
    root9.left.right = TreeNode(5)
    root9.right.left = TreeNode(6)
    root9.right.right = TreeNode(7)
    res9 = solver.postorderTraversal(root9)
    print("Test 9: Complex tree ->", res9)
    assert res9 == [4, 5, 2, 6, 7, 3, 1]

    # Test 10: Tree with negative values
    root10 = TreeNode(0)
    root10.left = TreeNode(-1)
    root10.right = TreeNode(1)
    root10.left.left = TreeNode(-2)
    root10.right.right = TreeNode(2)
    res10 = solver.postorderTraversal(root10)
    print("Test 10: Tree with negative values ->", res10)
    assert res10 == [-2, -1, 2, 1, 0]

    print("All tests passed!")


if __name__ == "__main__":
    test_postorderTraversal()
        