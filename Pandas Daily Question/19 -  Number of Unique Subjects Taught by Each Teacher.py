import pandas as pd

def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    result = (
        teacher.groupby('teacher_id')['subject_id']
               .nunique()
               .reset_index(name='cnt')
    )
    return result

# ---- Simple tests consistent with repository style (print + assert) ----
def test_count_unique_subjects():
    import pandas as pd

    # Test 1: Simple case, two teachers, overlapping subjects
    df1 = pd.DataFrame({
        'teacher_id': [1, 1, 2, 2, 2, 1],
        'subject_id': [101, 103, 101, 104, 104, 101]
    })
    out1 = count_unique_subjects(df1)
    expected1 = pd.DataFrame({
        'teacher_id': [1, 2],
        'cnt': [2, 2]
    })
    print("Test 1:\n", out1)
    assert out1.sort_values('teacher_id').reset_index(drop=True).equals(
        expected1.sort_values('teacher_id').reset_index(drop=True)
    )

    # Test 2: One teacher, all unique subjects
    df2 = pd.DataFrame({
        'teacher_id': [3, 3, 3],
        'subject_id': [201, 202, 203]
    })
    out2 = count_unique_subjects(df2)
    expected2 = pd.DataFrame({
        'teacher_id': [3],
        'cnt': [3]
    })
    print("Test 2:\n", out2)
    assert out2.equals(expected2)

    # Test 3: One teacher, duplicate subjects
    df3 = pd.DataFrame({
        'teacher_id': [4, 4, 4, 4],
        'subject_id': [301, 301, 301, 301]
    })
    out3 = count_unique_subjects(df3)
    expected3 = pd.DataFrame({
        'teacher_id': [4],
        'cnt': [1]
    })
    print("Test 3:\n", out3)
    assert out3.equals(expected3)

    # Test 4: No teachers/data
    df4 = pd.DataFrame(columns=['teacher_id', 'subject_id'])
    out4 = count_unique_subjects(df4)
    expected4 = pd.DataFrame(columns=['teacher_id', 'cnt'])
    print("Test 4:\n", out4)
    assert out4.shape == (0, 2)
    assert list(out4.columns) == ['teacher_id', 'cnt']

# Uncomment to run tests
# test_count_unique_subjects()