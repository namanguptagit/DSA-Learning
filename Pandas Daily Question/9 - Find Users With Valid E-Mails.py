import pandas as pd

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    pattern = r'^[A-Za-z][A-Za-z0-9_.-]*@leetcode\.com$'
    valid_emails_df = users[users['mail'].str.match(pattern)]
    
    return valid_emails_df

# Simple tests consistent with repository style (print + assert)
def test_valid_emails():
    # Test 1: Valid and invalid emails
    df1 = pd.DataFrame({
        'user_id': [1, 2, 3, 4, 5, 6, 7],
        'mail': [
            'alice@leetcode.com',       # valid
            'BOB@leetcode.com',         # valid (starts with letter, uppercase okay)
            'john.doe@leetcode.com',    # valid
            'jane_doe@leetcode.com',    # valid
            'mary@leet_code.com',       # invalid domain
            '1bob@leetcode.com',        # invalid, doesn't start with letter
            'eve@leetcode.co.uk',       # invalid domain
        ]
    })
    expected1 = pd.DataFrame({
        'user_id': [1, 2, 3, 4],
        'mail': [
            'alice@leetcode.com',
            'BOB@leetcode.com',
            'john.doe@leetcode.com',
            'jane_doe@leetcode.com'
        ]
    }, index=[0,1,2,3])
    out1 = valid_emails(df1)
    print("Test 1:\n", out1)
    assert out1.reset_index(drop=True).equals(expected1.reset_index(drop=True))

    # Test 2: All invalid
    df2 = pd.DataFrame({
        'user_id': [10, 11],
        'mail': [
            '42john@leetcode.com',      # starts with number
            '@leetcode.com',            # starts with @
        ]
    })
    out2 = valid_emails(df2)
    print("Test 2:\n", out2)
    assert len(out2) == 0

    # Test 3: All valid, various cases
    df3 = pd.DataFrame({
        'user_id': [20, 21],
        'mail': [
            'A_b-c.1@leetcode.com',
            'Z@leetcode.com'
        ]
    })
    expected3 = df3.copy()
    out3 = valid_emails(df3)
    print("Test 3:\n", out3)
    assert out3.reset_index(drop=True).equals(expected3.reset_index(drop=True))

    # Test 4: Edge case, only one row, valid email
    df4 = pd.DataFrame({
        'user_id': [99],
        'mail': ['a@leetcode.com']
    })
    expected4 = df4.copy()
    out4 = valid_emails(df4)
    print("Test 4:\n", out4)
    assert out4.reset_index(drop=True).equals(expected4.reset_index(drop=True))

    # Test 5: Edge case, minimum length not met
    df5 = pd.DataFrame({
        'user_id': [101],
        'mail': ['@leetcode.com']   # starts with @, not letter
    })
    out5 = valid_emails(df5)
    print("Test 5:\n", out5)
    assert len(out5) == 0

    print("All tests passed for valid_emails.")

if __name__ == "__main__":
    test_valid_emails()