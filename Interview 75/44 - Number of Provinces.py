class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set()
        provinces = 0

        def dfs(city):
            visited.add(city)
            for cur, connected in enumerate(isConnected[city]):
                if connected and cur not in visited:
                    dfs(cur)
            
        for i in range(len(isConnected)):
            if i not in visited:
                dfs(i)
                provinces += 1

        return provinces

# --- Simple tests consistent with repository style (print + assert) ---
if __name__ == "__main__":
    from typing import List
    sol = Solution()

    # Test 1: Simple case with two provinces
    isConnected1 = [
        [1,1,0],
        [1,1,0],
        [0,0,1]
    ]
    out1 = sol.findCircleNum(isConnected1)
    print("Test 1:", out1)
    assert out1 == 2

    # Test 2: All cities are in one province
    isConnected2 = [
        [1,1,0],
        [1,1,1],
        [0,1,1]
    ]
    out2 = sol.findCircleNum(isConnected2)
    print("Test 2:", out2)
    assert out2 == 1

    # Test 3: Each city disconnected (3 provinces)
    isConnected3 = [
        [1,0,0],
        [0,1,0],
        [0,0,1]
    ]
    out3 = sol.findCircleNum(isConnected3)
    print("Test 3:", out3)
    assert out3 == 3

    # Test 4: Single city
    isConnected4 = [
        [1]
    ]
    out4 = sol.findCircleNum(isConnected4)
    print("Test 4:", out4)
    assert out4 == 1

    # Test 5: Chain (expect 1 province)
    isConnected5 = [
        [1,1,0,0,0],
        [1,1,1,0,0],
        [0,1,1,1,0],
        [0,0,1,1,1],
        [0,0,0,1,1]
    ]
    out5 = sol.findCircleNum(isConnected5)
    print("Test 5:", out5)
    assert out5 == 1
