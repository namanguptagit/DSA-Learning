class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        adj = [[] for _ in range(n)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        self.ans = 0

        def dfs(node, parent):
            s = values[node]
            for nxt in adj[node]:
                if nxt != parent:
                    s += dfs(nxt, node)
            if s % k == 0:
                self.ans += 1
            return s % k

        dfs(0, -1)
        return self.ans

# ---- Simple tests consistent with repository style (print + assert) ----
def test_maxKDivisibleComponents():
    solver = Solution()
    
    # Test 1: All nodes value 1, k = 1 (every subtree sum divisible)
    n1 = 3
    edges1 = [[0,1],[1,2]]
    values1 = [1,1,1]
    k1 = 1
    out1 = solver.maxKDivisibleComponents(n1, edges1, values1, k1)
    print("Test 1:", out1)
    assert out1 == 3

    # Test 2: Tree sum not divisible except at root (k = 3)
    n2 = 4
    edges2 = [[0,1],[1,2],[1,3]]
    values2 = [1,2,2,1]
    k2 = 3
    out2 = solver.maxKDivisibleComponents(n2, edges2, values2, k2)
    print("Test 2:", out2)
    assert out2 == 1

    # Test 3: Subtrees and root divisible (k = 2)
    n3 = 5
    edges3 = [[0,1],[0,2],[1,3],[1,4]]
    values3 = [2,2,2,2,2]
    k3 = 2
    out3 = solver.maxKDivisibleComponents(n3, edges3, values3, k3)
    print("Test 3:", out3)
    assert out3 == 5  # Every node's subtree is even

    # Test 4: Single-node tree, value divisible
    n4 = 1
    edges4 = []
    values4 = [7]
    k4 = 7
    out4 = solver.maxKDivisibleComponents(n4, edges4, values4, k4)
    print("Test 4:", out4)
    assert out4 == 1

    # Test 5: Single-node tree, value not divisible
    n5 = 1
    edges5 = []
    values5 = [8]
    k5 = 5
    out5 = solver.maxKDivisibleComponents(n5, edges5, values5, k5)
    print("Test 5:", out5)
    assert out5 == 0

    # Test 6: Negative values, k = 3
    n6 = 3
    edges6 = [[0,1],[0,2]]
    values6 = [3,-6,6]
    k6 = 3
    out6 = solver.maxKDivisibleComponents(n6, edges6, values6, k6)
    print("Test 6:", out6)
    assert out6 == 3

if __name__ == "__main__":
    test_maxKDivisibleComponents()