import pandas as pd

# Modify Person in place
def delete_duplicate_emails(person: pd.DataFrame) -> None:
    # Sort the rows based on id (Ascending order)
    person.sort_values(by='id', ascending=True, inplace=True)
    # Drop the duplicates based on email.
    person.drop_duplicates(subset='email', keep='first', inplace=True)

# Simple tests consistent with repository style (print + assert)
def test_delete_duplicate_emails():
    import pandas as pd

    # Test 1: No duplicates
    df1 = pd.DataFrame({
        "id": [1, 2, 3],
        "email": ["a@x.com", "b@x.com", "c@x.com"]
    })
    expected1 = pd.DataFrame({
        "id": [1, 2, 3],
        "email": ["a@x.com", "b@x.com", "c@x.com"]
    }).sort_values(by='id').reset_index(drop=True)
    delete_duplicate_emails(df1)
    out1 = df1.sort_values(by='id').reset_index(drop=True)
    print("Test 1:\n", out1)
    assert out1.equals(expected1)

    # Test 2: One duplicate
    df2 = pd.DataFrame({
        "id": [1, 2, 3],
        "email": ["a@x.com", "b@x.com", "a@x.com"]
    })
    expected2 = pd.DataFrame({
        "id": [1, 2],
        "email": ["a@x.com", "b@x.com"]
    }).sort_values(by='id').reset_index(drop=True)
    delete_duplicate_emails(df2)
    out2 = df2.sort_values(by='id').reset_index(drop=True)
    print("Test 2:\n", out2)
    assert out2.equals(expected2)

    # Test 3: Keep lowest id for each email
    df3 = pd.DataFrame({
        "id": [2, 3, 4, 1],
        "email": ["test@x.com", "foo@x.com", "foo@x.com", "test@x.com"]
    })
    expected3 = pd.DataFrame({
        "id": [1, 3],
        "email": ["test@x.com", "foo@x.com"]
    }).sort_values(by='id').reset_index(drop=True)
    delete_duplicate_emails(df3)
    out3 = df3.sort_values(by='id').reset_index(drop=True)
    print("Test 3:\n", out3)
    assert out3.equals(expected3)

    # Test 4: All duplicate emails
    df4 = pd.DataFrame({
        "id": [4, 2, 1, 3],
        "email": ["a@x.com", "a@x.com", "a@x.com", "a@x.com"]
    })
    expected4 = pd.DataFrame({
        "id": [1],
        "email": ["a@x.com"]
    }).reset_index(drop=True)
    delete_duplicate_emails(df4)
    out4 = df4.sort_values(by='id').reset_index(drop=True)
    print("Test 4:\n", out4)
    assert out4.equals(expected4)

    print("All tests passed for delete_duplicate_emails.")

if __name__ == "__main__":
    test_delete_duplicate_emails()