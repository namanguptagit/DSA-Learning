import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    df = customers.merge(orders, how = 'left',          
                         left_on = 'id', right_on = 'customerId')

    return (df[df.customerId.isna()]                    
                 .rename(columns = {'name':'Customers'}).iloc[:,[1]])


# Simple tests consistent with repository style (print + assert)
def test_find_customers():
    customers = pd.DataFrame({'id': [1, 2, 3], 'name': ['Alice', 'Bob', 'Charlie']})
    orders = pd.DataFrame({'id': [1, 2, 3], 'customerId': [1, 2, 2], 'product': ['A', 'B', 'A']})
    out = find_customers(customers, orders)
    # Only Charlie has not placed order
    print("Test 1:", out)
    assert out.reset_index(drop=True).equals(pd.DataFrame({'Customers': ['Charlie']}))

    # Test: all customers have orders
    orders2 = pd.DataFrame({'id': [1, 2, 3], 'customerId': [1, 2, 3], 'product': ['A', 'B', 'C']})
    out2 = find_customers(customers, orders2)
    print("Test 2:", out2)
    assert out2.empty

    # Test: no orders at all
    orders3 = pd.DataFrame({'id': [], 'customerId': [], 'product': []})
    out3 = find_customers(customers, orders3)
    print("Test 3:", out3)
    expected3 = pd.DataFrame({'Customers': ['Alice', 'Bob', 'Charlie']})
    assert out3.reset_index(drop=True).equals(expected3)

    # Test: empty customers input
    customers4 = pd.DataFrame({'id': [], 'name': []})
    orders4 = pd.DataFrame({'id': [1], 'customerId': [1], 'product': ['A']})
    out4 = find_customers(customers4, orders4)
    print("Test 4:", out4)
    assert out4.empty

    print("All tests passed for find_customers.")

if __name__ == "__main__":
    test_find_customers()