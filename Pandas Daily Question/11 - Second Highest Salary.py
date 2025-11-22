import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:

    colName = 'SecondHighestSalary'
    df = employee.drop_duplicates(['salary'])
    
    if df.salary.count() > 1:
        df = df.sort_values('salary')
        salary = [df.iloc[-2, 1]]  
    else:
        salary = [None]     
        
    return pd.DataFrame({colName: salary})

# Simple tests consistent with repository style (print + assert)
def test_second_highest_salary():
    # Test 1: Multiple distinct salaries
    df1 = pd.DataFrame({
        'id': [1, 2, 3, 4],
        'salary': [100, 200, 300, 200]
    })
    out1 = second_highest_salary(df1)
    expected1 = pd.DataFrame({'SecondHighestSalary': [200]})
    print("Test 1:\n", out1)
    assert out1.equals(expected1)

    # Test 2: Only one salary (should be None)
    df2 = pd.DataFrame({
        'id': [1],
        'salary': [500]
    })
    out2 = second_highest_salary(df2)
    expected2 = pd.DataFrame({'SecondHighestSalary': [None]})
    print("Test 2:\n", out2)
    assert out2.equals(expected2)

    # Test 3: All same salary (should be None)
    df3 = pd.DataFrame({
        'id': [1, 2, 3],
        'salary': [100, 100, 100]
    })
    out3 = second_highest_salary(df3)
    expected3 = pd.DataFrame({'SecondHighestSalary': [None]})
    print("Test 3:\n", out3)
    assert out3.equals(expected3)

    # Test 4: Only two distinct salaries
    df4 = pd.DataFrame({
        'id': [1, 2],
        'salary': [50, 60]
    })
    out4 = second_highest_salary(df4)
    expected4 = pd.DataFrame({'SecondHighestSalary': [50]})
    print("Test 4:\n", out4)
    assert out4.equals(expected4)

    # Test 5: Empty dataframe
    df5 = pd.DataFrame({'id': [], 'salary': []})
    out5 = second_highest_salary(df5)
    expected5 = pd.DataFrame({'SecondHighestSalary': [None]})
    print("Test 5:\n", out5)
    assert out5.equals(expected5)

    print("All tests passed for second_highest_salary.")

if __name__ == "__main__":
    test_second_highest_salary()