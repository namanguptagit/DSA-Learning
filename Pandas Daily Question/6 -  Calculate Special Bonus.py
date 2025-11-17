def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:

    employees['ch_bonus'] = ~employees.name.str.startswith('M')
    employees['id_bonus'] = employees.employee_id%2
    employees.salary*= employees.ch_bonus * employees.employee_id%2

    return (employees.rename(columns = {'salary':'bonus'})
                    .sort_values('employee_id').iloc[:,[0,2]])

# Simple tests consistent with repository style (print + assert)
if __name__ == "__main__":
    import pandas as pd

    # Test 1: Sample use - names not starting with 'M', odd employee_id
    df1 = pd.DataFrame({
        'employee_id': [1, 2, 3, 4],
        'name': ['Alice', 'Bob', 'Mary', 'John'],
        'salary': [1000, 1200, 1300, 1400]
    })
    expected1 = pd.DataFrame({
        'employee_id': [1,2,3,4],
        'bonus': [1000,0,0,0]
    })
    out1 = calculate_special_bonus(df1.copy())
    print("Test 1:\n", out1)
    assert out1.reset_index(drop=True).equals(expected1)

    # Test 2: All names start with 'M' (no one gets bonus)
    df2 = pd.DataFrame({
        'employee_id': [1, 3, 5],
        'name': ['Mary','Ming','Mike'],
        'salary':[100,200,300]
    })
    expected2 = pd.DataFrame({
        'employee_id': [1,3,5],
        'bonus':[0,0,0]
    })
    out2 = calculate_special_bonus(df2.copy())
    print("Test 2:\n", out2)
    assert out2.reset_index(drop=True).equals(expected2)

    # Test 3: All odd ids, but some names 'M'
    df3 = pd.DataFrame({
        'employee_id': [1,3,5,7],
        'name': ['Mona','Jake','Jill','Morris'],
        'salary':[10,20,30,40]
    })
    expected3 = pd.DataFrame({
        'employee_id':[1,3,5,7],
        'bonus':[0,20,30,0]
    })
    out3 = calculate_special_bonus(df3.copy())
    print("Test 3:\n", out3)
    assert out3.reset_index(drop=True).equals(expected3)

    # Test 4: Even ids only
    df4 = pd.DataFrame({
        'employee_id': [2, 4, 6],
        'name': ['Anna', 'Bella', 'Mark'],
        'salary': [111, 222, 333]
    })
    expected4 = pd.DataFrame({
        'employee_id': [2,4,6],
        'bonus':[0,0,0]
    })
    out4 = calculate_special_bonus(df4.copy())
    print("Test 4:\n", out4)
    assert out4.reset_index(drop=True).equals(expected4)

    print("All tests passed for calculate_special_bonus.")