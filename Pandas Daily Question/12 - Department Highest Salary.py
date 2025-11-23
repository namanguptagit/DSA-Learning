import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    merged = employee.merge(department, left_on='departmentId', right_on='id', how='left')
    highest_salary = merged.loc[merged.groupby('departmentId')['salary'].transform('max') == merged['salary']]
    result = highest_salary[['name_x', 'salary', 'name_y']].rename(columns={ 
        'name_y': 'Department',  
        'name_x': 'Employee',    
        'salary': 'Salary'       
    })
        
    out = result[['Department', 'Employee', 'Salary']]
    return out

# Simple tests consistent with repository style (print + assert)
def test_department_highest_salary():
    employee = pd.DataFrame({
        'id': [1, 2, 3, 4, 5, 6],
        'name': ['Joe', 'Henry', 'Sam', 'Max', 'Jane', 'Janet'],
        'salary': [70000, 80000, 60000, 90000, 85000, 90000],
        'departmentId': [1, 2, 2, 1, 1, 1]
    })
    department = pd.DataFrame({
        'id': [1, 2],
        'name': ['IT', 'Sales']
    })

    expected = pd.DataFrame({
        'Department': ['IT', 'IT', 'Sales'],
        'Employee': ['Max', 'Janet', 'Henry'],
        'Salary': [90000, 90000, 80000]
    })

    out = department_highest_salary(employee, department)
    out_sorted = out.sort_values(['Department', 'Employee']).reset_index(drop=True)
    exp_sorted = expected.sort_values(['Department', 'Employee']).reset_index(drop=True)
    print("Test 1:", out_sorted)
    assert out_sorted.equals(exp_sorted)

    # Test: Department with only one employee
    employee2 = pd.DataFrame({
        'id': [1, 2],
        'name': ['Lily', 'John'],
        'salary': [125000, 115000],
        'departmentId': [1, 2]
    })
    department2 = pd.DataFrame({
        'id': [1, 2],
        'name': ['Design', 'HR']
    })
    expected2 = pd.DataFrame({
        'Department': ['Design', 'HR'],
        'Employee': ['Lily', 'John'],
        'Salary': [125000, 115000]
    })
    out2 = department_highest_salary(employee2, department2)
    out2_sorted = out2.sort_values(['Department', 'Employee']).reset_index(drop=True)
    exp2_sorted = expected2.sort_values(['Department', 'Employee']).reset_index(drop=True)
    print("Test 2:", out2_sorted)
    assert out2_sorted.equals(exp2_sorted)

    # Test: Multiple employees with same highest salary in a department
    employee3 = pd.DataFrame({
        'id': [1, 2, 3],
        'name': ['Ann', 'Bob', 'Cathy'],
        'salary': [50000, 80000, 80000],
        'departmentId': [1, 1, 1]
    })
    department3 = pd.DataFrame({'id': [1], 'name': ['HR']})
    expected3 = pd.DataFrame({
        'Department': ['HR', 'HR'],
        'Employee': ['Bob', 'Cathy'],
        'Salary': [80000, 80000]
    })
    out3 = department_highest_salary(employee3, department3)
    out3_sorted = out3.sort_values(['Department', 'Employee']).reset_index(drop=True)
    exp3_sorted = expected3.sort_values(['Department', 'Employee']).reset_index(drop=True)
    print("Test 3:", out3_sorted)
    assert out3_sorted.equals(exp3_sorted)

    print("All tests passed for department_highest_salary.")

if __name__ == "__main__":
    test_department_highest_salary()