# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # helper dfs returns count of good nodes from this node down
        def dfs(node, max_so_far):
            if not node:
                return 0  # base case: null node, 0 good nodes

            # is this node good?
            count = 1 if node.val >= max_so_far else 0

            # update max for children
            new_max = max(max_so_far, node.val)

            # count good nodes in left and right subtrees
            count += dfs(node.left, new_max)
            count += dfs(node.right, new_max)

            return count

        return dfs(root, root.val)

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

def test_goodNodes():
    solver = Solution()
    # Test 1: Example -- [3,1,4,3,None,1,5] has 4 good nodes (3,4,3,5)
    root1 = build_tree([3,1,4,3,None,1,5])
    out1 = solver.goodNodes(root1)
    print("Test 1:", out1)
    assert out1 == 4

    # Test 2: All ascending right chain [2,None,3,None,4] -> all are good
    root2 = build_tree([2,None,3,None,4])
    out2 = solver.goodNodes(root2)
    print("Test 2:", out2)
    assert out2 == 3

    # Test 3: Single node
    root3 = build_tree([7])
    out3 = solver.goodNodes(root3)
    print("Test 3:", out3)
    assert out3 == 1

    # Test 4: All values are same [2,2,2]
    root4 = build_tree([2,2,2])
    out4 = solver.goodNodes(root4)
    print("Test 4:", out4)
    assert out4 == 3

    # Test 5: Decreasing left chain [5,4,3,2,1] -- only root is good
    root5 = TreeNode(5, TreeNode(4, TreeNode(3, TreeNode(2, TreeNode(1)))))
    out5 = solver.goodNodes(root5)
    print("Test 5:", out5)
    assert out5 == 1

    # Test 6: Empty tree
    out6 = solver.goodNodes(None)
    print("Test 6:", out6)
    assert out6 == 0

# Uncomment to run tests
test_goodNodes()