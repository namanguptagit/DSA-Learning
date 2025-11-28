# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(root):
            if root is None:
                return []
            leaves = dfs(root.left) + dfs(root.right)
            return leaves or [root.val]
        return dfs(root1) == dfs(root2)

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

def test_leafSimilar():
    solver = Solution()
    # Test 1: Example -- [3,5,1,6,2,9,8,None,None,7,4] and [3,5,1,6,7,4,2,None,None,None,None,None,None,9,8] → leaf-similar
    root1 = build_tree([3,5,1,6,2,9,8,None,None,7,4])
    root2 = build_tree([3,5,1,6,7,4,2,None,None,None,None,None,None,9,8])
    out1 = solver.leafSimilar(root1, root2)
    print("Test 1:", out1)
    assert out1 is True

    # Test 2: Trees with different leaves
    root3 = build_tree([1,2,3])
    root4 = build_tree([1,3,2])
    out2 = solver.leafSimilar(root3, root4)
    print("Test 2:", out2)
    assert out2 is False

    # Test 3: Both single node, same value
    root5 = build_tree([7])
    root6 = build_tree([7])
    out3 = solver.leafSimilar(root5, root6)
    print("Test 3:", out3)
    assert out3 is True

    # Test 4: Both single node, different values
    root7 = build_tree([1])
    root8 = build_tree([2])
    out4 = solver.leafSimilar(root7, root8)
    print("Test 4:", out4)
    assert out4 is False

if __name__ == "__main__":
    test_leafSimilar()