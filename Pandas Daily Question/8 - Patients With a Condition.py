import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:

    return patients[(patients.conditions.str.contains  (' DIAB1')) |
                    (patients.conditions.str.startswith('DIAB1' )) ]

# Simple tests consistent with repository style (print + assert)
def test_find_patients():
    # Test 1: Conditions contains " DIAB1" and starts with "DIAB1"
    df1 = pd.DataFrame({
        'patient_id': [1,2,3,4,5],
        'conditions': [
            'DIAB1 HYPT',      # startswith "DIAB1"
            'HYPT',            # no DIAB1
            'ASTHMA DIAB1',    # contains " DIAB1"
            'DIAB2',           # only DIAB2
            'foo bar',         # neither
        ]
    })
    expected1 = pd.DataFrame({
        'patient_id': [1,3],
        'conditions': [
            'DIAB1 HYPT',
            'ASTHMA DIAB1'
        ]
    }, index=[0,2])
    out1 = find_patients(df1)
    print("Test 1:\n", out1)
    # Compare sorted patient_id sets (ignoring row order)
    assert set(out1.patient_id) == set(expected1.patient_id)

    # Test 2: All patients have DIAB1 somewhere
    df2 = pd.DataFrame({
        'patient_id': [10,11],
        'conditions': ['DIAB1', 'foo DIAB1 bar'],
    })
    expected2 = df2.copy()
    out2 = find_patients(df2)
    print("Test 2:\n", out2)
    assert out2.reset_index(drop=True).equals(expected2)

    # Test 3: No patient has DIAB1 at all
    df3 = pd.DataFrame({
        'patient_id': [100,101],
        'conditions': ['ASTHMA', 'DIAB2'],
    })
    out3 = find_patients(df3)
    print("Test 3:\n", out3)
    assert len(out3) == 0

    # Test 4: Edge case — 'DIAB1' in middle, but not preceded by space
    df4 = pd.DataFrame({
        'patient_id': [1,2],
        'conditions': ['fooDIAB1 bar', 'bar DIAB1baz'],
    })
    # First has no match, second is not matched unless " DIAB1" is there exactly
    expected4 = pd.DataFrame([], columns=['patient_id', 'conditions'])
    out4 = find_patients(df4)
    print("Test 4:\n", out4)
    assert len(out4) == 0

    # Test 5: patient with condition is only " DIAB1" (with leading space)
    df5 = pd.DataFrame({
        'patient_id': [20],
        'conditions': [' DIAB1'],
    })
    expected5 = df5.copy()
    out5 = find_patients(df5)
    print("Test 5:\n", out5)
    assert out5.reset_index(drop=True).equals(expected5)

    print("All tests passed for find_patients.")

if __name__ == "__main__":
    test_find_patients()