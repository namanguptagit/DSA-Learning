class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root

        return left or right

# ---- Simple tests consistent with repository style (print + assert) ----
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def build_tree_with_references(vals):
    """Builds binary tree from list of values, returns (root, all_nodes_dict[val]=node)."""
    if not vals: return None, {}
    nodes = {}
    treenodes = [None if v is None else TreeNode(v) for v in vals]
    for n in treenodes:
        if n: nodes[n.val] = n
    kids = treenodes[::-1]
    root = kids.pop()
    for node in treenodes:
        if node:
            if kids: node.left = kids.pop()
            if kids: node.right = kids.pop()
    return root, nodes

def test_lowestCommonAncestor():
    solver = Solution()

    # Test 1: Simple tree; 3 is root, 5 and 1 are children
    #      3
    #     / \
    #    5   1
    vals1 = [3,5,1]
    root1, nodes1 = build_tree_with_references(vals1)
    out1 = solver.lowestCommonAncestor(root1, nodes1[5], nodes1[1])
    print("Test 1:", out1.val)
    assert out1.val == 3

    # Test 2: Deeper tree
    #      3
    #     / \
    #    5   1
    #   / \ / \
    #  6  2 0 8
    #    / \
    #   7   4
    vals2 = [3,5,1,6,2,0,8,None,None,7,4]
    root2, nodes2 = build_tree_with_references(vals2)
    out2 = solver.lowestCommonAncestor(root2, nodes2[5], nodes2[4])
    print("Test 2:", out2.val)
    # Lowest common ancestor of 5 and 4 is 5
    assert out2.val == 5

    out3 = solver.lowestCommonAncestor(root2, nodes2[5], nodes2[1])
    print("Test 3:", out3.val)
    # LCA of 5 and 1 is 3
    assert out3.val == 3

    out4 = solver.lowestCommonAncestor(root2, nodes2[7], nodes2[0])
    print("Test 4:", out4.val)
    # LCA of 7 and 0 is 3
    assert out4.val == 3

    out5 = solver.lowestCommonAncestor(root2, nodes2[6], nodes2[4])
    print("Test 5:", out5.val)
    # LCA of 6 and 4 is 5
    assert out5.val == 5

    # Test 3: p equals q (find LCA of same node)
    out6 = solver.lowestCommonAncestor(root2, nodes2[8], nodes2[8])
    print("Test 6:", out6.val)
    assert out6.val == 8

    # Test 4: root is one of the nodes
    out7 = solver.lowestCommonAncestor(root2, root2, nodes2[8])
    print("Test 7:", out7.val)
    assert out7.val == 3

# Uncomment to run the tests
# test_lowestCommonAncestor()