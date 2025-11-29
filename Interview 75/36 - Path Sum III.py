# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        prefix = {0: 1}  # base: one path with sum=0

        def dfs(node, currSum):
            if not node:
                return 0

            currSum += node.val
            count = prefix.get(currSum - targetSum, 0)

            prefix[currSum] = prefix.get(currSum, 0) + 1
            count += dfs(node.left, currSum)
            count += dfs(node.right, currSum)
            prefix[currSum] -= 1  # backtrack

            return count

        return dfs(root, 0)

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

def test_pathSum():
    solver = Solution()
    # Test 1: Example -- [10,5,-3,3,2,None,11,3,-2,None,1], sum=8
    # Paths: 5->3, 5->2->1, -3->11
    root1 = build_tree([10,5,-3,3,2,None,11,3,-2,None,1])
    out1 = solver.pathSum(root1, 8)
    print("Test 1:", out1)
    assert out1 == 3

    # Test 2: Example -- [1,None,2,None,3,None,4,None,5], sum=3
    # Only [1,2], [3], [1,2,None,4,-4]
    root2 = build_tree([1,None,2,None,3,None,4,None,5])
    out2 = solver.pathSum(root2, 3)
    print("Test 2:", out2)
    assert out2 == 2

    # Test 3: Only negative values, [1,-2,-3,1,3,-2,None,-1], sum = -1
    root3 = build_tree([1,-2,-3,1,3,-2,None,-1])
    out3 = solver.pathSum(root3, -1)
    print("Test 3:", out3)
    assert out3 == 4

    # Test 4: Single node, exact match
    root4 = build_tree([7])
    out4 = solver.pathSum(root4, 7)
    print("Test 4:", out4)
    assert out4 == 1

    # Test 5: Single node, mismatch
    root5 = build_tree([7])
    out5 = solver.pathSum(root5, 1)
    print("Test 5:", out5)
    assert out5 == 0

    # Test 6: Empty tree
    out6 = solver.pathSum(None, 0)
    print("Test 6:", out6)
    assert out6 == 0

    # Test 7: All zeros, multiple paths
    root7 = build_tree([0,0,0,0,None,0,None,None,None,0])
    out7 = solver.pathSum(root7, 0)
    print("Test 7:", out7)
    # We check that at least one path exists (it's 6)
    assert out7 == 6

# Uncomment to run tests
test_pathSum()