class Solution:
    def predictPartyVictory(self, senate: str) -> str:

        n = len(senate)

        r_arr = [i for i in range(len(senate)) if senate[i]=='R']
        d_arr = [j for j in range(len(senate)) if senate[j]=='D']
        
        while r_arr and d_arr:
            r = r_arr.pop(0)
            d = d_arr.pop(0)
            if r < d:
                r_arr.append(n + r)
            else:
                d_arr.append(n + d)
                
        return 'Radiant' if r_arr else 'Dire'

# Simple tests consistent with repository style (print + assert)
def test_predictPartyVictory():
    solver = Solution()

    # Test 1: Example from problem, "RD" -> Radiant bans Dire, wins
    s1 = "RD"
    out1 = solver.predictPartyVictory(s1)
    print("Test 1:", out1)
    assert out1 == "Radiant"

    # Test 2: "DDRRR" -> Dire bans two R, but last R survives and bans all D
    s2 = "DDRRR"
    out2 = solver.predictPartyVictory(s2)
    print("Test 2:", out2)
    assert out2 == "Radiant"

    # Test 3: All Dire
    s3 = "DDD"
    out3 = solver.predictPartyVictory(s3)
    print("Test 3:", out3)
    assert out3 == "Dire"

    # Test 4: All Radiant
    s4 = "RRRR"
    out4 = solver.predictPartyVictory(s4)
    print("Test 4:", out4)
    assert out4 == "Radiant"

    # Test 5: Alternating
    s5 = "RDRD"
    out5 = solver.predictPartyVictory(s5)
    print("Test 5:", out5)
    assert out5 == "Radiant"

    # Test 6: Edge case, length 1
    s6 = "D"
    out6 = solver.predictPartyVictory(s6)
    print("Test 6:", out6)
    assert out6 == "Dire"

    # Test 7: Radiant outnumbers Dire
    s7 = "RRRDD"
    out7 = solver.predictPartyVictory(s7)
    print("Test 7:", out7)
    assert out7 == "Radiant"

    # Test 8: Dire outnumbers Radiant
    s8 = "DRDDDD"
    out8 = solver.predictPartyVictory(s8)
    print("Test 8:", out8)
    assert out8 == "Dire"

    print("All tests passed for predictPartyVictory.")

if __name__ == "__main__":
    test_predictPartyVictory()