from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        #returns height
        def dfs(curr):
            if not curr:
                return 0
            left = dfs(curr.left)
            right = dfs(curr.right)

            self.res = max(self.res,left+right)
            return max(left,right)+1
        dfs(root)
        return self.res


# Simple tests consistent with repository style (print + assert)
def test_diameterOfBinaryTree():
    solver = Solution()

    # Test 1: Empty tree
    root1 = None
    res1 = solver.diameterOfBinaryTree(root1)
    print("Test 1: Empty tree ->", res1)
    assert res1 == 0

    # Test 2: Single node
    root2 = TreeNode(1)
    res2 = solver.diameterOfBinaryTree(root2)
    print("Test 2: Single node ->", res2)
    assert res2 == 0

    # Test 3: Two nodes
    root3 = TreeNode(1)
    root3.left = TreeNode(2)
    res3 = solver.diameterOfBinaryTree(root3)
    print("Test 3: Two nodes ->", res3)
    assert res3 == 1

    # Test 4: Three nodes (simple path)
    root4 = TreeNode(1)
    root4.left = TreeNode(2)
    root4.right = TreeNode(3)
    res4 = solver.diameterOfBinaryTree(root4)
    print("Test 4: Three nodes ->", res4)
    assert res4 == 2

    # Test 5: Left skewed tree
    root5 = TreeNode(1)
    root5.left = TreeNode(2)
    root5.left.left = TreeNode(3)
    root5.left.left.left = TreeNode(4)
    res5 = solver.diameterOfBinaryTree(root5)
    print("Test 5: Left skewed tree ->", res5)
    assert res5 == 3

    # Test 6: Right skewed tree
    root6 = TreeNode(1)
    root6.right = TreeNode(2)
    root6.right.right = TreeNode(3)
    root6.right.right.right = TreeNode(4)
    res6 = solver.diameterOfBinaryTree(root6)
    print("Test 6: Right skewed tree ->", res6)
    assert res6 == 3

    # Test 7: Balanced tree
    root7 = TreeNode(1)
    root7.left = TreeNode(2)
    root7.right = TreeNode(3)
    root7.left.left = TreeNode(4)
    root7.left.right = TreeNode(5)
    res7 = solver.diameterOfBinaryTree(root7)
    print("Test 7: Balanced tree ->", res7)
    assert res7 == 3

    # Test 8: Complex tree
    root8 = TreeNode(1)
    root8.left = TreeNode(2)
    root8.right = TreeNode(3)
    root8.left.left = TreeNode(4)
    root8.left.right = TreeNode(5)
    root8.right.left = TreeNode(6)
    root8.right.right = TreeNode(7)
    res8 = solver.diameterOfBinaryTree(root8)
    print("Test 8: Complex tree ->", res8)
    assert res8 == 4

    # Test 9: Tree with long path through root
    root9 = TreeNode(1)
    root9.left = TreeNode(2)
    root9.left.left = TreeNode(3)
    root9.left.left.left = TreeNode(4)
    root9.right = TreeNode(5)
    root9.right.right = TreeNode(6)
    root9.right.right.right = TreeNode(7)
    res9 = solver.diameterOfBinaryTree(root9)
    print("Test 9: Long path through root ->", res9)
    assert res9 == 6

    # Test 10: Tree with diameter not through root
    root10 = TreeNode(1)
    root10.left = TreeNode(2)
    root10.left.left = TreeNode(3)
    root10.left.left.left = TreeNode(4)
    root10.left.left.right = TreeNode(5)
    root10.left.left.right.right = TreeNode(6)
    res10 = solver.diameterOfBinaryTree(root10)
    print("Test 10: Diameter not through root ->", res10)
    assert res10 == 4

    print("All tests passed!")


if __name__ == "__main__":
    test_diameterOfBinaryTree()
