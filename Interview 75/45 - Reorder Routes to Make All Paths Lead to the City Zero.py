class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        adj=defaultdict(list)
        seen=set()
        for x,y in connections:
            adj[x].append(y)
            adj[y].append(x)
            seen.add((x,y))
        vis=[False]*n
        q=deque()
        q.append(0)
        vis[0]=True
        ans=0
        while q:
            node=q.popleft()
            for nei in adj[node]:
                if not vis[nei]:
                    vis[nei]=1
                    if (node,nei) in seen:
                        ans+=1
                    q.append(nei)
        return ans

        # Simple test cases (consistent with repository style: print + assert)

from collections import defaultdict, deque
from typing import List

def test_minReorder():
    sol = Solution()
    
    # Test 1: Example from LeetCode - 6 nodes, 3 reversals needed
    n1 = 6
    connections1 = [[0,1],[1,3],[2,3],[4,0],[4,5]]
    out1 = sol.minReorder(n1, connections1)
    print("Test 1:", out1)
    assert out1 == 3

    # Test 2: All already correct (no reversals needed)
    n2 = 5
    connections2 = [[1,0],[2,0],[3,0],[4,0]]
    out2 = sol.minReorder(n2, connections2)
    print("Test 2:", out2)
    assert out2 == 0

    # Test 3: Only one node, no roads
    n3 = 1
    connections3 = []
    out3 = sol.minReorder(n3, connections3)
    print("Test 3:", out3)
    assert out3 == 0

    # Test 4: Chain of 4 (all edges need reversal)
    n4 = 4
    connections4 = [[1,0],[2,1],[3,2]]
    out4 = sol.minReorder(n4, connections4)
    print("Test 4:", out4)
    assert out4 == 0

    # Test 5: All edges directed away from 0
    n5 = 4
    connections5 = [[0,1],[1,2],[2,3]]
    out5 = sol.minReorder(n5, connections5)
    print("Test 5:", out5)
    assert out5 == 3

    # Test 6: Reverse chain, but shuffled roads
    n6 = 5
    connections6 = [[2,3],[4,2],[3,1],[1,0]]
    out6 = sol.minReorder(n6, connections6)
    print("Test 6:", out6)
    assert out6 == 0

if __name__ == "__main__":
    test_minReorder()