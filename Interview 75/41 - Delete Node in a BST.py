# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return None 
        if root.val == key:
            return self.helper(root)
        
        dummy = root
        while root is not None:
            if root.val > key:
                if root.left is not None and root.left.val == key:
                    root.left = self.helper(root.left)
                    break
                else:
                    root = root.left
            else:
                if root.right is not None and root.right.val == key:
                    root.right = self.helper(root.right)
                    break
                else:
                    root = root.right
        return dummy
    
    def helper(self, root):
        if root.left is None:
            return root.right
        if root.right is None:
            return root.left
        
        rightChild = root.right
        lastRight = self.flr(root.left)  # rightmost node in left subtree
        lastRight.right = rightChild
        return root.left
    
    def flr(self, root):
        if root.right is None:
            return root
        return self.flr(root.right)


# --- Simple tests consistent with repository style (print + assert) ---

# Binary tree node definition
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree_from_list(values):
    """ Helper to build a binary search tree from list using level order (None means empty)"""
    if not values:
        return None
    root = TreeNode(values[0])
    nodes = [root]
    i = 1
    for node in nodes:
        if node is not None:
            if i < len(values):
                val = values[i]
                if val is not None:
                    node.left = TreeNode(val)
                nodes.append(node.left if val is not None else None)
                i += 1
            if i < len(values):
                val = values[i]
                if val is not None:
                    node.right = TreeNode(val)
                nodes.append(node.right if val is not None else None)
                i += 1
    return root

def inorder_traversal(root):
    result = []
    def inorder(node):
        if node:
            inorder(node.left)
            result.append(node.val)
            inorder(node.right)
    inorder(root)
    return result

def test_deleteNode():
    sol = Solution()

    # Test 1: Delete leaf node
    vals1 = [5,3,6,2,4,None,7]
    root1 = build_tree_from_list(vals1)
    out1 = sol.deleteNode(root1, 2)
    print("Test 1:", inorder_traversal(out1))
    assert inorder_traversal(out1) == [3,4,5,6,7]

    # Test 2: Delete node with one child
    vals2 = [5,3,6,2,4,None,7]
    root2 = build_tree_from_list(vals2)
    out2 = sol.deleteNode(root2, 6)
    print("Test 2:", inorder_traversal(out2))
    assert inorder_traversal(out2) == [2,3,4,5,7]

    # Test 3: Delete node with two children
    vals3 = [5,3,6,2,4,None,7]
    root3 = build_tree_from_list(vals3)
    out3 = sol.deleteNode(root3, 3)
    print("Test 3:", inorder_traversal(out3))
    assert inorder_traversal(out3) == [2,4,5,6,7]

    # Test 4: Delete root with two children
    vals4 = [5,3,6,2,4,None,7]
    root4 = build_tree_from_list(vals4)
    out4 = sol.deleteNode(root4, 5)
    print("Test 4:", inorder_traversal(out4))
    assert inorder_traversal(out4) == [2,3,4,6,7]

    # Test 5: Delete root, single-node tree
    vals5 = [10]
    root5 = build_tree_from_list(vals5)
    out5 = sol.deleteNode(root5, 10)
    print("Test 5:", inorder_traversal(out5))
    assert inorder_traversal(out5) == []

    # Test 6: Delete non-existent value
    vals6 = [8,3,10,1,6,None,14]
    root6 = build_tree_from_list(vals6)
    out6 = sol.deleteNode(root6, 99)
    print("Test 6:", inorder_traversal(out6))
    assert inorder_traversal(out6) == [1,3,6,8,10,14]

    # Test 7: Delete from empty tree
    out7 = sol.deleteNode(None, 1)
    print("Test 7:", inorder_traversal(out7))
    assert inorder_traversal(out7) == []

# Uncomment to run tests
# test_deleteNode()