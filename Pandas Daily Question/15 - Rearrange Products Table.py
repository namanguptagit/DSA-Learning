import pandas as pd

def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:
    result = pd.melt(
        products, id_vars='product_id', var_name='store', value_name='price'
    ).dropna()
    return result

# Simple tests consistent with repository style (print + assert)
def test_rearrange_products_table():
    import pandas as pd

    # Test 1: Example from LeetCode
    df1 = pd.DataFrame({
        "product_id": [1, 2],
        "store1": [95, 70],
        "store2": [100, None],
        "store3": [None, 80],
    })
    expected1 = pd.DataFrame({
        "product_id": [1, 1, 2, 2, 2],
        "store": ["store1", "store2", "store1", "store3", "store2"],
        "price": [95.0, 100.0, 70.0, 80.0, None]
    })
    expected1 = expected1.dropna().reset_index(drop=True)
    out1 = rearrange_products_table(df1).sort_values(by=["product_id", "store"]).reset_index(drop=True)
    print("Test 1:\n", out1)
    assert out1.equals(expected1)

    # Test 2: All stores have prices
    df2 = pd.DataFrame({
        "product_id": [1],
        "store1": [20],
        "store2": [25],
        "store3": [30]
    })
    expected2 = pd.DataFrame({
        "product_id": [1, 1, 1],
        "store": ["store1", "store2", "store3"],
        "price": [20, 25, 30]
    }).sort_values(by=["store"]).reset_index(drop=True)
    out2 = rearrange_products_table(df2).sort_values(by=["store"]).reset_index(drop=True)
    print("Test 2:\n", out2)
    assert out2.equals(expected2)

    # Test 3: All stores missing for a product
    df3 = pd.DataFrame({
        "product_id": [1],
        "store1": [None],
        "store2": [None],
        "store3": [None]
    })
    expected3 = pd.DataFrame({
        "product_id": [],
        "store": [],
        "price": []
    })
    out3 = rearrange_products_table(df3)
    print("Test 3:\n", out3)
    assert out3.empty

if __name__ == "__main__":
    test_rearrange_products_table()