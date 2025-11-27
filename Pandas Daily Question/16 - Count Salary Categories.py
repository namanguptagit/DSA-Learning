import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
        return pd.DataFrame({
            'category': ['Low Salary', 'Average Salary', 'High Salary'],
            'accounts_count': [
                accounts[accounts.income < 20000].shape[0],
                accounts[(accounts.income >= 20000) & (accounts.income <= 50000)].shape[0],
                accounts[accounts.income > 50000].shape[0],
            ],
        })

    # Simple tests consistent with repository style (print + assert)
    def test_count_salary_categories():
        import pandas as pd

        # Test 1: Example with all salary categories
        df1 = pd.DataFrame({
            "account_id": [1, 2, 3, 4, 5, 6],
            "income": [15000, 25000, 40000, 60000, 51000, 18000]
        })
        out1 = count_salary_categories(df1)
        expected1 = pd.DataFrame({
            'category': ['Low Salary', 'Average Salary', 'High Salary'],
            'accounts_count': [2, 2, 2]
        })
        print("Test 1:\n", out1)
        assert out1.equals(expected1)

        # Test 2: Only high salaries present
        df2 = pd.DataFrame({
            "account_id": [1, 2],
            "income": [80000, 70000]
        })
        out2 = count_salary_categories(df2)
        expected2 = pd.DataFrame({
            'category': ['Low Salary', 'Average Salary', 'High Salary'],
            'accounts_count': [0, 0, 2]
        })
        print("Test 2:\n", out2)
        assert out2.equals(expected2)

        # Test 3: Only low and average
        df3 = pd.DataFrame({
            "account_id": [1,2,3],
            "income": [10000, 49999, 20000]
        })
        out3 = count_salary_categories(df3)
        expected3 = pd.DataFrame({
            'category': ['Low Salary', 'Average Salary', 'High Salary'],
            'accounts_count': [1, 2, 0]
        })
        print("Test 3:\n", out3)
        assert out3.equals(expected3)

        # Test 4: Empty DataFrame
        df4 = pd.DataFrame({"account_id": [], "income": []})
        out4 = count_salary_categories(df4)
        expected4 = pd.DataFrame({
            'category': ['Low Salary', 'Average Salary', 'High Salary'],
            'accounts_count': [0, 0, 0]
        })
        print("Test 4:\n", out4)
        assert out4.equals(expected4)

        # Test 5: Boundary values
        df5 = pd.DataFrame({
            "account_id": [1,2,3],
            "income": [20000, 50000, 19999]
        })
        out5 = count_salary_categories(df5)
        expected5 = pd.DataFrame({
            'category': ['Low Salary', 'Average Salary', 'High Salary'],
            'accounts_count': [1, 2, 0]
        })
        print("Test 5:\n", out5)
        assert out5.equals(expected5)

    if __name__ == "__main__":
        test_count_salary_categories()