# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        
        return 1 + max(left_depth, right_depth)
# ---- Simple tests consistent with repository style (print + assert) ----
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree(vals):
    """Helper to build binary tree from list (where None means missing node, level order)."""
    if not vals: return None
    nodes = [None if v is None else TreeNode(v) for v in vals]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids: node.left = kids.pop()
            if kids: node.right = kids.pop()
    return root

def test_maxDepth():
    solver = Solution()
    # Test 1: Example tree [3,9,20,None,None,15,7], maxDepth = 3
    root1 = build_tree([3,9,20,None,None,15,7])
    out1 = solver.maxDepth(root1)
    print("Test 1:", out1)
    assert out1 == 3

    # Test 2: Single node
    root2 = build_tree([1])
    out2 = solver.maxDepth(root2)
    print("Test 2:", out2)
    assert out2 == 1

    # Test 3: Chain tree [1,2,None,3], depth = 3
    root3 = TreeNode(1, TreeNode(2, TreeNode(3)))
    out3 = solver.maxDepth(root3)
    print("Test 3:", out3)
    assert out3 == 3

    # Test 4: Empty tree
    out4 = solver.maxDepth(None)
    print("Test 4:", out4)
    assert out4 == 0

    # Test 5: Balanced tree, [1,2,3,4,5,None,6], depth = 3
    root5 = build_tree([1,2,3,4,5,None,6])
    out5 = solver.maxDepth(root5)
    print("Test 5:", out5)
    assert out5 == 3

# Uncomment to run tests
# test_maxDepth()