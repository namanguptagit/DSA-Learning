# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        self.ans = 0

        def dfs(node, goLeft, length):
            if not node:
                return
            # update max answer so far
            self.ans = max(self.ans, length)

            if goLeft:
                # if going left now, next must be right
                dfs(node.left, False, length + 1)
                # OR restart fresh on right
                dfs(node.right, True, 1)
            else:
                dfs(node.right, True, length + 1)
                dfs(node.left, False, 1)

        dfs(root, True, 0)   # assume starting left
        dfs(root, False, 0)  # assume starting right
        return self.ans

# ---- Simple tests consistent with repository style (print + assert) ----
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

def test_longestZigZag():
    solver = Solution()

    # Test 1: Example from LeetCode (ZigZag length 3)
    # Tree: [1,null,1,1,1,null,null,1,1,null,1,null,null,null,1]
    root1 = build_tree([1,None,1,1,1,None,None,1,1,None,1,None,None,None,1])
    out1 = solver.longestZigZag(root1)
    print("Test 1:", out1)
    assert out1 == 3

    # Test 2: Tree with only root
    root2 = build_tree([1])
    out2 = solver.longestZigZag(root2)
    print("Test 2:", out2)
    assert out2 == 0

    # Test 3: Simple line, always right (no zigzag)
    root3 = build_tree([1,None,1,None,1,None,1])
    out3 = solver.longestZigZag(root3)
    print("Test 3:", out3)
    assert out3 == 1

    # Test 4: Simple straight line alternating to maximize ZigZag
    # [1,2,None,None,3,None,4]
    #      1
    #     /
    #    2
    #     \
    #      3
    #       \
    #        4
    root4 = build_tree([1,2,None,None,3,None,4])
    out4 = solver.longestZigZag(root4)
    print("Test 4:", out4)
    assert out4 == 3

    # Test 5: Only left child (no zigzag)
    root5 = build_tree([1,2])
    out5 = solver.longestZigZag(root5)
    print("Test 5:", out5)
    assert out5 == 1

    # Test 6: Empty tree
    out6 = solver.longestZigZag(None)
    print("Test 6:", out6)
    assert out6 == 0

    # Test 7: Full binary tree, no zigzag longer than 1
    root7 = build_tree([1,2,3,4,5,6,7])
    out7 = solver.longestZigZag(root7)
    print("Test 7:", out7)
    assert out7 == 2

    # Test 8: Short right, then left, then right
    # [1, None, 2, 3, None, None, 4]
    #     1
    #      \
    #       2
    #      /
    #     3
    #      \
    #       4
    root8 = build_tree([1, None, 2, 3, None, None, 4])
    out8 = solver.longestZigZag(root8)
    print("Test 8:", out8)
    assert out8 == 3

if __name__ == "__main__":
    test_longestZigZag()