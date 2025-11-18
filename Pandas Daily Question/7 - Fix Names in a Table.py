import pandas as pd

def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    
    users.name = users.name.str.capitalize()
    return users.sort_values('user_id')
    # Simple tests consistent with repository style (print + assert)
    if __name__ == "__main__":
        # Test 1: Basic example with various case and order
        df1 = pd.DataFrame({
            'user_id': [2, 1, 3],
            'name': ['ALICE', 'bob', 'John']
        })
        expected1 = pd.DataFrame({
            'user_id': [1, 2, 3],
            'name': ['Bob', 'Alice', 'John']
        })
        out1 = fix_names(df1.copy())
        print("Test 1:\n", out1)
        assert out1.reset_index(drop=True).equals(expected1)

        # Test 2: Already capitalized, already sorted
        df2 = pd.DataFrame({
            'user_id': [1, 2],
            'name': ['Jane', 'Mark']
        })
        expected2 = pd.DataFrame({
            'user_id': [1, 2],
            'name': ['Jane', 'Mark']
        })
        out2 = fix_names(df2.copy())
        print("Test 2:\n", out2)
        assert out2.reset_index(drop=True).equals(expected2)

        # Test 3: Lowercase, mixed order
        df3 = pd.DataFrame({
            'user_id': [3, 2],
            'name': ['zack', 'lISA']
        })
        expected3 = pd.DataFrame({
            'user_id': [2, 3],
            'name': ['Lisa', 'Zack']
        })
        out3 = fix_names(df3.copy())
        print("Test 3:\n", out3)
        assert out3.reset_index(drop=True).equals(expected3)

        # Test 4: One entry
        df4 = pd.DataFrame({
            'user_id': [5],
            'name': ['mARY']
        })
        expected4 = pd.DataFrame({
            'user_id': [5],
            'name': ['Mary']
        })
        out4 = fix_names(df4.copy())
        print("Test 4:\n", out4)
        assert out4.reset_index(drop=True).equals(expected4)

        print("All tests passed for fix_names.")