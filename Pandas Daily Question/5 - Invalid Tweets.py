import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    invalid = tweets[tweets['content'].str.len() > 15]

    return invalid[['tweet_id']]

# Simple tests consistent with repository style (print + assert)
def test_invalid_tweets():
    # Test 1: Typical input
    tweets = pd.DataFrame({
        'tweet_id': [1, 2, 3, 4],
        'content': [
            "short",                          # valid
            "this tweet is too long!!",       # invalid
            "fifteen chars!!",                # invalid (16 chars)
            "123456789012345"                 # valid (15 chars)
        ]
    })
    out = invalid_tweets(tweets)
    print("Test 1:", out)
    expected = pd.DataFrame({'tweet_id': [2, 3]})
    assert out.reset_index(drop=True).equals(expected)

    # Test 2: All valid
    tweets2 = pd.DataFrame({
        'tweet_id': [5, 6],
        'content': [
            "one",        # valid
            "exactly15char"  # valid (13 chars)
        ]
    })
    out2 = invalid_tweets(tweets2)
    print("Test 2:", out2)
    assert out2.empty

    # Test 3: Empty DataFrame
    tweets3 = pd.DataFrame({'tweet_id': [], 'content': []})
    out3 = invalid_tweets(tweets3)
    print("Test 3:", out3)
    assert out3.empty

    # Test 4: Content of exactly 15 chars
    tweets4 = pd.DataFrame({'tweet_id': [7], 'content': ["abcdefghijklmno"]})
    out4 = invalid_tweets(tweets4)
    print("Test 4:", out4)
    assert out4.empty

    print("All tests passed for invalid_tweets.")

if __name__ == "__main__":
    test_invalid_tweets()