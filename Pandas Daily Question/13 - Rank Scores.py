import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    # Use the rank method to assign ranks to the scores in descending order with no gaps
    scores['rank'] = scores['score'].rank(method='dense', ascending=False)
    
    # Drop id column & Sort the DataFrame by score in descending order
    result_df = scores.drop('id',axis=1).sort_values(by='score', ascending=False)
    
    return result_df

# Simple tests consistent with repository style (print + assert)
def test_order_scores():
    scores1 = pd.DataFrame({
        "id": [1, 2, 3, 4],
        "score": [3.5, 3.65, 4.0, 3.85],
    })
    expected1 = pd.DataFrame({
        "score": [4.0, 3.85, 3.65, 3.5],
        "rank": [1.0, 2.0, 3.0, 4.0],
    }).reset_index(drop=True)
    out1 = order_scores(scores1).reset_index(drop=True)
    print("Test 1:\n", out1)
    assert out1.equals(expected1)

    # Test 2: Duplicate scores
    scores2 = pd.DataFrame({
        "id": [1,2,3,4],
        "score": [100, 90, 90, 80],
    })
    expected2 = pd.DataFrame({
        "score": [100, 90, 90, 80],
        "rank": [1.0, 2.0, 2.0, 3.0],
    }).reset_index(drop=True)
    out2 = order_scores(scores2).reset_index(drop=True)
    print("Test 2:\n", out2)
    assert out2.equals(expected2)

    # Test 3: Single row
    scores3 = pd.DataFrame({
        "id": [1],
        "score": [88],
    })
    expected3 = pd.DataFrame({
        "score": [88],
        "rank": [1.0],
    }).reset_index(drop=True)
    out3 = order_scores(scores3).reset_index(drop=True)
    print("Test 3:\n", out3)
    assert out3.equals(expected3)

    # Test 4: Already descending
    scores4 = pd.DataFrame({
        "id": [10,11,12],
        "score": [100,98,10],
    })
    expected4 = pd.DataFrame({
        "score": [100,98,10],
        "rank": [1.0,2.0,3.0],
    }).reset_index(drop=True)
    out4 = order_scores(scores4).reset_index(drop=True)
    print("Test 4:\n", out4)
    assert out4.equals(expected4)

    # Test 5: Empty DataFrame
    scores5 = pd.DataFrame(columns=["id", "score"])
    expected5 = pd.DataFrame(columns=["score", "rank"])
    out5 = order_scores(scores5).reset_index(drop=True)
    print("Test 5:\n", out5)
    assert out5.equals(expected5)

    print("All tests passed for order_scores.")

if __name__ == "__main__":
    test_order_scores()