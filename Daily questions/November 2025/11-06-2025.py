from typing import List

class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        parent=list(range(c+1))
        def find(x):
            while parent[x]!=x:
                parent[x]=parent[parent[x]]
                x=parent[x]
            return x
        for a,b in connections:
            ra,rb=find(a),find(b)
            if ra!=rb:
                parent[rb]=ra
        next_node=[0]*(c+1)
        comp_min=[0]*(c+1)
        last={}
        for i in range(1,c+1):
            r=find(i)
            if comp_min[r]==0:
                comp_min[r]=i
            else:
                next_node[last[r]]=i
            last[r]=i
        offline=[False]*(c+1)
        res=[]
        for t,x in queries:
            if t==1:
                if not offline[x]:
                    res.append(x)
                else:
                    r=find(x)
                    m=comp_min[r]
                    res.append(m if m else -1)
            else:
                if offline[x]:
                    continue
                offline[x]=True
                r=find(x)
                if comp_min[r]==x:
                    y=next_node[x]
                    while y and offline[y]:
                        y=next_node[y]
                    comp_min[r]=y
        return res


# Simple tests consistent with repository style (print + assert)
def test_processQueries():
    solver = Solution()

    # Test 1: Basic query on online node
    c1, conn1, queries1 = 3, [[1, 2], [2, 3]], [[1, 1], [1, 2]]
    res1 = solver.processQueries(c1, conn1, queries1)
    print("Test 1: c=", c1, "connections=", conn1, "queries=", queries1, "->", res1)
    assert res1 == [1, 2]

    # Test 2: Query on offline node (should return minimum in component)
    c2, conn2, queries2 = 3, [[1, 2], [2, 3]], [[2, 1], [1, 1]]
    res2 = solver.processQueries(c2, conn2, queries2)
    print("Test 2: c=", c2, "connections=", conn2, "queries=", queries2, "->", res2)
    # After disconnecting 1, component min becomes 2
    assert res2 == [2]

    # Test 3: Multiple disconnects, query returns next minimum
    c3, conn3, queries3 = 4, [[1, 2], [2, 3], [3, 4]], [[2, 1], [2, 2], [1, 1]]
    res3 = solver.processQueries(c3, conn3, queries3)
    print("Test 3: c=", c3, "connections=", conn3, "queries=", queries3, "->", res3)
    # After disconnecting 1 and 2, component min becomes 3
    assert res3 == [3]

    # Test 4: No connections, each node is separate component
    c4, conn4, queries4 = 3, [], [[1, 1], [1, 2], [2, 1], [1, 1]]
    res4 = solver.processQueries(c4, conn4, queries4)
    print("Test 4: c=", c4, "connections=", conn4, "queries=", queries4, "->", res4)
    # After disconnecting 1, querying 1 returns -1 (no online nodes in component)
    assert res4 == [1, 2, -1]

    # Test 5: Single node, query then disconnect
    c5, conn5, queries5 = 1, [], [[1, 1], [2, 1], [1, 1]]
    res5 = solver.processQueries(c5, conn5, queries5)
    print("Test 5: c=", c5, "connections=", conn5, "queries=", queries5, "->", res5)
    # After disconnecting 1, querying 1 returns -1
    assert res5 == [1, -1]

    # Test 6: Complex component with multiple queries
    c6, conn6, queries6 = 5, [[1, 2], [3, 4], [4, 5]], [[1, 1], [1, 3], [2, 1], [1, 2], [1, 1]]
    res6 = solver.processQueries(c6, conn6, queries6)
    print("Test 6: c=", c6, "connections=", conn6, "queries=", queries6, "->", res6)
    # Component 1-2: query 1 returns 1, disconnect 1, query 2 returns 2, query 1 returns 2
    # Component 3-4-5: query 3 returns 3
    assert res6 == [1, 3, 2, 2]

    # Test 7: Disconnect all nodes in component, query returns -1
    c7, conn7, queries7 = 3, [[1, 2], [2, 3]], [[2, 1], [2, 2], [2, 3], [1, 1]]
    res7 = solver.processQueries(c7, conn7, queries7)
    print("Test 7: c=", c7, "connections=", conn7, "queries=", queries7, "->", res7)
    # All nodes disconnected, query returns -1
    assert res7 == [-1]

    print("All tests passed!")


if __name__ == "__main__":
    test_processQueries()