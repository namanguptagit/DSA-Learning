import pandas as pd
def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    return activity.groupby(
        'player_id'
    ).agg(
        first_login=('event_date', 'min')
    ).reset_index()

# ---- Simple tests consistent with repository style (print + assert) ----
def test_game_analysis():
    import pandas as pd

    # Test 1: Simple case with two players, multiple logins
    df1 = pd.DataFrame({
        'player_id': [1, 1, 2, 2, 2],
        'device_id': [101, 101, 202, 202, 202],
        'event_date': ['2016-03-01', '2016-05-01', '2016-03-01', '2016-06-01', '2016-02-28'],
        'games_played': [5, 8, 3, 6, 7]
    })
    out1 = game_analysis(df1)
    expected1 = pd.DataFrame({
        'player_id': [1, 2],
        'first_login': ['2016-03-01', '2016-02-28']
    })
    print("Test 1:\n", out1)
    # check sorted because order not guaranteed
    assert out1.sort_values('player_id').reset_index(drop=True).equals(
        expected1.sort_values('player_id').reset_index(drop=True)
    )

    # Test 2: One player only
    df2 = pd.DataFrame({
        'player_id': [5, 5],
        'device_id': [200, 200],
        'event_date': ['2019-11-09', '2019-10-12'],
        'games_played': [1, 2]
    })
    out2 = game_analysis(df2)
    expected2 = pd.DataFrame({
        'player_id': [5],
        'first_login': ['2019-10-12']
    })
    print("Test 2:\n", out2)
    assert out2[['player_id','first_login']].equals(expected2)

    # Test 3: No rows, empty DataFrame
    df3 = pd.DataFrame(columns=['player_id', 'device_id', 'event_date', 'games_played'])
    out3 = game_analysis(df3)
    print("Test 3:\n", out3)
    assert out3.shape == (0, 2)
    assert list(out3.columns) == ['player_id', 'first_login']

    # Test 4: Player with one login only
    df4 = pd.DataFrame({
        'player_id': [10],
        'device_id': [301],
        'event_date': ['2020-01-01'],
        'games_played': [3]
    })
    out4 = game_analysis(df4)
    expected4 = pd.DataFrame({
        'player_id': [10],
        'first_login': ['2020-01-01']
    })
    print("Test 4:\n", out4)
    assert out4.equals(expected4)

if __name__ == "__main__":
    test_game_analysis()