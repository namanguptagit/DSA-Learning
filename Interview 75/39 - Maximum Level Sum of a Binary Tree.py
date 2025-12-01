class Solution:
    def maxLevelSum(self, root):
        if not root:
            return 0

        queue = [root]
        max_level = 1
        max_sum = float('-inf')
        level = 1

        while queue:
            level_sum = 0
            next_level = []

            for node in queue:
                level_sum += node.val

                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)

            if level_sum > max_sum:
                max_sum = level_sum
                max_level = level

            queue = next_level
            level += 1

        return max_level


# Test cases
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree_from_level_list(level_list):
    """Helper function to build tree from level list (None as null)."""
    if not level_list or level_list[0] is None:
        return None
    nodes = [TreeNode(val) if val is not None else None for val in level_list]
    kid_idx = 1
    for i in range(len(nodes)):
        if nodes[i] is not None:
            if kid_idx < len(nodes):
                nodes[i].left = nodes[kid_idx]
                kid_idx += 1
            if kid_idx < len(nodes):
                nodes[i].right = nodes[kid_idx]
                kid_idx += 1
    return nodes[0]

def test():
    # Example 1: [1,7,0,7,-8,None,None]
    root1 = build_tree_from_level_list([1,7,0,7,-8,None,None])
    assert Solution().maxLevelSum(root1) == 2

    # Example 2: [989,None,10250,98693,-89388,None,None,None,-32127]
    root2 = build_tree_from_level_list([989,None,10250,98693,-89388,None,None,None,-32127])
    assert Solution().maxLevelSum(root2) == 2

    # Extra: [1]
    root3 = build_tree_from_level_list([1])
    assert Solution().maxLevelSum(root3) == 1

    # Extra: [1,2,3]
    root4 = build_tree_from_level_list([1,2,3])
    assert Solution().maxLevelSum(root4) == 2

    print("All test cases passed.")

if __name__ == "__main__":
    test()