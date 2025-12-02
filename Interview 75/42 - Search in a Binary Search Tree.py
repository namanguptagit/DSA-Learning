# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        while root:
            if root.val > val:
                root = root.left 
            elif root.val < val:
                root = root.right 
            else:
                return root 
        return None 

# --- Simple tests consistent with repository style (print + assert) ---

# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree_from_list(values):
    """Helper to build a binary search tree from list using level order (None means empty)"""
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

def tree_to_list_preorder(root):
    if not root:
        return []
    return [root.val] + tree_to_list_preorder(root.left) + tree_to_list_preorder(root.right)

def test_searchBST():
    sol = Solution()
    
    # Test 1: Target present in left subtree
    vals1 = [4,2,7,1,3]
    root1 = build_tree_from_list(vals1)
    node = sol.searchBST(root1, 2)
    print("Test 1:", tree_to_list_preorder(node))
    assert tree_to_list_preorder(node) == [2,1,3]

    # Test 2: Target present in right subtree
    node = sol.searchBST(root1, 7)
    print("Test 2:", tree_to_list_preorder(node))
    assert tree_to_list_preorder(node) == [7]

    # Test 3: Target is root
    node = sol.searchBST(root1, 4)
    print("Test 3:", tree_to_list_preorder(node))
    assert tree_to_list_preorder(node) == [4,2,1,3,7]

    # Test 4: Target not found
    node = sol.searchBST(root1, 10)
    print("Test 4:", tree_to_list_preorder(node))
    assert node is None

    # Test 5: Empty tree
    node = sol.searchBST(None, 5)
    print("Test 5:", tree_to_list_preorder(node))
    assert node is None

    # Test 6: Single node (found)
    root2 = build_tree_from_list([1])
    node = sol.searchBST(root2, 1)
    print("Test 6:", tree_to_list_preorder(node))
    assert tree_to_list_preorder(node) == [1]

    # Test 7: Single node (not found)
    node = sol.searchBST(root2, 2)
    print("Test 7:", tree_to_list_preorder(node))
    assert node is None

# Uncomment to run tests
# test_searchBST()