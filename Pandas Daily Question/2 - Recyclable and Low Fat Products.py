import pandas as pd


def find_products(products: pd.DataFrame) -> pd.DataFrame:
    return (
        products[products.low_fats == 'Y'][products.recyclable == 'Y']
        .iloc[:, [0]]
    )


# Simple tests consistent with repository style (print + assert)
def test_find_products():
    # Test 1: Basic example with mixed flags
    products1 = pd.DataFrame(
        {
            "product_id": [1001, 1002, 1003, 1004],
            "low_fats": ["Y", "N", "Y", "Y"],
            "recyclable": ["Y", "Y", "Y", "N"],
        }
    )
    res1 = find_products(products1)
    expected1 = pd.DataFrame({"product_id": [1001, 1003]})
    print("Test 1:\n", res1)
    pd.testing.assert_frame_equal(res1.reset_index(drop=True), expected1)

    # Test 2: No qualifying products
    products2 = pd.DataFrame(
        {
            "product_id": [2001, 2002],
            "low_fats": ["N", "N"],
            "recyclable": ["Y", "N"],
        }
    )
    res2 = find_products(products2)
    expected2 = pd.DataFrame({"product_id": []})
    print("Test 2:\n", res2)
    pd.testing.assert_frame_equal(res2.reset_index(drop=True), expected2)

    # Test 3: All products qualify
    products3 = pd.DataFrame(
        {
            "product_id": [3001, 3002, 3003],
            "low_fats": ["Y", "Y", "Y"],
            "recyclable": ["Y", "Y", "Y"],
        }
    )
    res3 = find_products(products3)
    expected3 = pd.DataFrame({"product_id": [3001, 3002, 3003]})
    print("Test 3:\n", res3)
    pd.testing.assert_frame_equal(res3.reset_index(drop=True), expected3)

    # Test 4: Preserve original order of qualifying products
    products4 = pd.DataFrame(
        {
            "product_id": [4003, 4001, 4002],
            "low_fats": ["Y", "Y", "Y"],
            "recyclable": ["N", "Y", "Y"],
        }
    )
    res4 = find_products(products4)
    expected4 = pd.DataFrame({"product_id": [4001, 4002]})
    print("Test 4:\n", res4)
    pd.testing.assert_frame_equal(res4.reset_index(drop=True), expected4)

    print("All tests passed!")


if __name__ == "__main__":
    test_find_products()