import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    
  return (employees.groupby(['emp_id', 'event_day']).agg(sum)
                   .reset_index(names = ['emp_id', 'day'])
                   .assign(total_time = lambda x: x.out_time - x.in_time)
                   .iloc[:,[1,0,4]])

# ---- Simple tests consistent with repository style (print + assert) ----
def test_total_time():
    import pandas as pd

    # Test 1: Example with two employees, one day each
    df1 = pd.DataFrame({
        'emp_id': [1, 2, 1, 2],
        'event_day': ['2023-11-01', '2023-11-01', '2023-11-01', '2023-11-01'],
        'in_time': [1, 2, 3, 8],
        'out_time': [5, 5, 7, 12],
    })
    out1 = total_time(df1)
    expected1 = pd.DataFrame({
        'day': ['2023-11-01', '2023-11-01'],
        'emp_id': [1,2],
        'total_time': [(5+7)-(1+3), (5+12)-(2+8)]  # (12-4)=8, (17-10)=7
    })
    print("Test 1:\n", out1)
    assert out1[['day','emp_id','total_time']].reset_index(drop=True).equals(expected1)

    # Test 2: Multiple days for one employee
    df2 = pd.DataFrame({
        'emp_id': [1, 1, 1, 1],
        'event_day': ['2023-11-01', '2023-11-01', '2023-11-02', '2023-11-02'],
        'in_time': [1, 5, 2, 6],
        'out_time': [4, 7, 6, 10],
    })
    out2 = total_time(df2)
    expected2 = pd.DataFrame({
        'day': ['2023-11-01','2023-11-02'],
        'emp_id': [1,1],
        'total_time':[ (4+7)-(1+5), (6+10)-(2+6) ]  # 11-6=5, 16-8=8
    })
    print("Test 2:\n", out2)
    assert out2[['day','emp_id','total_time']].reset_index(drop=True).equals(expected2)

    # Test 3: Single employee, single row
    df3 = pd.DataFrame({
        'emp_id': [7],
        'event_day': ['2024-06-30'],
        'in_time': [10],
        'out_time': [18]
    })
    out3 = total_time(df3)
    expected3 = pd.DataFrame({'day':['2024-06-30'],'emp_id':[7],'total_time':[8]})
    print("Test 3:\n", out3)
    assert out3[['day','emp_id','total_time']].reset_index(drop=True).equals(expected3)

    # Test 4: Empty input
    df4 = pd.DataFrame(columns=['emp_id', 'event_day', 'in_time', 'out_time'])
    out4 = total_time(df4)
    expected4 = pd.DataFrame(columns=['day', 'emp_id', 'total_time'])
    print("Test 4:\n", out4)
    # Careful: check columns and shape
    assert out4.shape == (0, 3)
    assert (list(out4.columns) == ['day','emp_id','total_time'])

if __name__ == "__main__":
    test_total_time()