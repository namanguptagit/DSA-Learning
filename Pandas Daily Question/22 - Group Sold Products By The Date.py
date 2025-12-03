import pandas as pd

def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    result = activities.groupby(
        'sell_date'
    )['product'].agg([
        ('num_sold', 'nunique'),
        ('products', lambda x: ','.join(sorted(x.unique())))
    ]).reset_index()
    return result

# --- Simple tests consistent with repository style (print + assert) ---
def test_categorize_products():
    data1 = pd.DataFrame({
        'sell_date': ['2024-01-01', '2024-01-01', '2024-01-01', '2024-01-02', '2024-01-02'],
        'product': ['apple', 'banana', 'banana', 'orange', 'apple']
    })
    out1 = categorize_products(data1)
    print("Test 1:")
    print(out1)
    assert set(out1.columns) == {'sell_date', 'num_sold', 'products'}
    assert out1.shape == (2, 3)
    assert any(out1['sell_date'] == '2024-01-01')
    assert out1[out1['sell_date'] == '2024-01-01']['num_sold'].iloc[0] == 2
    assert out1[out1['sell_date'] == '2024-01-01']['products'].iloc[0] == 'apple,banana'

    data2 = pd.DataFrame({
        'sell_date': ['2023-07-07'],
        'product': ['cucumber']
    })
    out2 = categorize_products(data2)
    print("Test 2:")
    print(out2)
    assert out2.iloc[0]['num_sold'] == 1
    assert out2.iloc[0]['products'] == 'cucumber'

    data3 = pd.DataFrame({
        'sell_date': [],
        'product': []
    })
    out3 = categorize_products(data3)
    print("Test 3:")
    print(out3)
    assert out3.shape == (0, 3)