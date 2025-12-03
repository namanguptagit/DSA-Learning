class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        n = len(rooms)
        seen = [False]*n
        seen[0] = True
        st = [0]
        while st:
            u = st.pop()
            for v in rooms[u]:
                if not seen[v]:
                    seen[v] = True
                    st.append(v)
        return all(seen)

# --- Simple tests consistent with repository style (print + assert) ---
if __name__ == "__main__":
    sol = Solution()
    # Test 1: Standard case, all rooms accessible
    rooms1 = [[1], [2], [3], []]
    out1 = sol.canVisitAllRooms(rooms1)
    print("Test 1:", out1)
    assert out1 == True

    # Test 2: Not all rooms accessible
    rooms2 = [[1, 3], [3, 0, 1], [2], [0]]
    out2 = sol.canVisitAllRooms(rooms2)
    print("Test 2:", out2)
    assert out2 == True

    # Test 3: Disconnected, one room cannot be reached
    rooms3 = [[1, 2], [2], [], [0]]
    out3 = sol.canVisitAllRooms(rooms3)
    print("Test 3:", out3)
    assert out3 == False

    # Test 4: Single room, always accessible
    rooms4 = [[]]
    out4 = sol.canVisitAllRooms(rooms4)
    print("Test 4:", out4)
    assert out4 == True

    # Test 5: Room 0 links to nothing, cannot reach room 1
    rooms5 = [[], [0]]
    out5 = sol.canVisitAllRooms(rooms5)
    print("Test 5:", out5)
    assert out5 == False