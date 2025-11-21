import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:

    colName = 'getNthHighestSalary('+str(N)+')'
    df = employee.drop_duplicates(['salary'])
    
    if 0 < N <= df.salary.count():
        df = df.sort_values('salary')
        salary = [df.iloc[-N, 1]]  
    else:
        salary = [None]     
        
    return pd.DataFrame({colName: salary})   

# Simple tests consistent with repository style (print + assert)
def test_nth_highest_salary():
    # Test 1: Example with multiple distinct salaries
    df1 = pd.DataFrame({
        'id': [1, 2, 3, 4],
        'salary': [100, 200, 300, 200]
    })
    out1 = nth_highest_salary(df1, 2)
    expected1 = pd.DataFrame({'getNthHighestSalary(2)': [200]})
    print("Test 1:\n", out1)
    assert out1.equals(expected1)

    # Test 2: N greater than number of distinct salaries
    out2 = nth_highest_salary(df1, 10)
    expected2 = pd.DataFrame({'getNthHighestSalary(10)': [None]})
    print("Test 2:\n", out2)
    assert out2.equals(expected2)

    # Test 3: N = 1 (highest salary)
    out3 = nth_highest_salary(df1, 1)
    expected3 = pd.DataFrame({'getNthHighestSalary(1)': [300]})
    print("Test 3:\n", out3)
    assert out3.equals(expected3)

    # Test 4: Only one employee
    df4 = pd.DataFrame({'id': [1], 'salary': [700]})
    out4 = nth_highest_salary(df4, 1)
    expected4 = pd.DataFrame({'getNthHighestSalary(1)': [700]})
    print("Test 4:\n", out4)
    assert out4.equals(expected4)

    # Test 5: N = 0 (invalid N, should return None)
    out5 = nth_highest_salary(df1, 0)
    expected5 = pd.DataFrame({'getNthHighestSalary(0)': [None]})
    print("Test 5:\n", out5)
    assert out5.equals(expected5)

    # Test 6: Empty DataFrame
    df6 = pd.DataFrame({'id': [], 'salary': []})
    out6 = nth_highest_salary(df6, 1)
    expected6 = pd.DataFrame({'getNthHighestSalary(1)': [None]})
    print("Test 6:\n", out6)
    assert out6.equals(expected6)

    print("All tests passed for nth_highest_salary.")

if __name__ == "__main__":
    test_nth_highest_salary()