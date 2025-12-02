import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    result = orders['customer_number'].mode().to_frame()
    result.columns = ['customer_number']
    return result

# --- Simple tests consistent with repository style (print + assert) ---
def test_largest_orders():
    data1 = pd.DataFrame({
        'order_number': [1,2,3,4,5],
        'customer_number': [1,2,2,3,3]
    })
    # customer_number 2 and 3 both have 2 orders (mode is [2,3])
    out1 = largest_orders(data1)
    print("Test 1:")
    print(out1)
    assert set(out1['customer_number']) == {2,3}
    assert out1.shape == (2,1)

    data2 = pd.DataFrame({
        'order_number': [11,12,13,14],
        'customer_number': [7,7,7,7]
    })
    # Only customer 7 has all orders
    out2 = largest_orders(data2)
    print("Test 2:")
    print(out2)
    assert out2.iloc[0,0] == 7
    assert out2.shape == (1,1)

    data3 = pd.DataFrame({
        'order_number': [5,6,7,8,9],
        'customer_number': [1,2,3,4,5]
    })
    # All customers have one order: mode is all customer numbers
    out3 = largest_orders(data3)
    print("Test 3:")
    print(out3)
    assert set(out3['customer_number']) == {1,2,3,4,5}
    assert out3.shape == (5,1)

    data4 = pd.DataFrame({
        'order_number': [],
        'customer_number': []
    })
    # Empty DataFrame
    out4 = largest_orders(data4)
    print("Test 4:")
    print(out4)
    assert out4.empty

# Uncomment to run tests
# test_largest_orders()