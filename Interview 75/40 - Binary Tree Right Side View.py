from collections import deque

class Solution:
    def rightSideView(self, root):
        if not root:
            return []
        res, q = [], deque([root])

        while q:
            size = len(q)
            for i in range(size):
                node = q.popleft()
                # if last node of this level → visible
                if i == size - 1:
                    res.append(node.val)
                # push children
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return res

# --- Simple tests consistent with repository style (print + assert) ---

# Binary tree node definition
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree_from_list(values):
    """Helper to build a binary tree from list (BFS order, None means no node)"""
    if not values:
        return None
    root = TreeNode(values[0])
    q = deque([root])
    i = 1
    while q and i < len(values):
        node = q.popleft()
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            q.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            q.append(node.right)
        i += 1
    return root

def test_rightSideView():
    solver = Solution()

    # Test 1: [1,2,3,None,5,None,4]
    vals1 = [1,2,3,None,5,None,4]
    tree1 = build_tree_from_list(vals1)
    out1 = solver.rightSideView(tree1)
    print("Test 1:", vals1, "->", out1)
    assert out1 == [1,3,4]

    # Test 2: [1,None,3]
    vals2 = [1,None,3]
    tree2 = build_tree_from_list(vals2)
    out2 = solver.rightSideView(tree2)
    print("Test 2:", vals2, "->", out2)
    assert out2 == [1,3]

    # Test 3: []
    vals3 = []
    tree3 = build_tree_from_list(vals3)
    out3 = solver.rightSideView(tree3)
    print("Test 3:", vals3, "->", out3)
    assert out3 == []

    # Test 4: [1]
    vals4 = [1]
    tree4 = build_tree_from_list(vals4)
    out4 = solver.rightSideView(tree4)
    print("Test 4:", vals4, "->", out4)
    assert out4 == [1]

    # Test 5: Full complete tree
    vals5 = [1,2,3,4,5,6,7]
    tree5 = build_tree_from_list(vals5)
    out5 = solver.rightSideView(tree5)
    print("Test 5:", vals5, "->", out5)
    assert out5 == [1,3,7]

# Uncomment to run tests
# test_rightSideView()