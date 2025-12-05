import pandas as pd

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:

    actor_director = actor_director.groupby(['actor_id', 'director_id'])['timestamp'
                      ].size().reset_index()
   
    return actor_director[actor_director.timestamp >= 3].iloc[:,[0,1]]

# --- Simple tests consistent with repository style (print + assert) ---
def test_actors_and_directors():
    df1 = pd.DataFrame({
        'actor_id': [1,1,1,1,2,2,2,3],
        'director_id': [10,10,10,11,10,10,11,10],
        'timestamp': [100,101,102,103,104,105,106,107]
    })
    # actor 1 w/ director 10: 3 times, with 11: 1 time
    # actor 2 w/ director 10: 2 times, with 11: 1 time
    # actor 3 w/ director 10: 1 time
    out1 = actors_and_directors(df1)
    print("Test 1 result:\n", out1)
    # Only actor 1 and director 10 qualifies
    assert out1.shape[0] == 1
    assert (out1.iloc[0] == [1,10]).all()

    df2 = pd.DataFrame({
        'actor_id': [],
        'director_id': [],
        'timestamp': []
    })
    out2 = actors_and_directors(df2)
    print("Test 2 (empty):\n", out2)
    assert out2.shape[0] == 0

    df3 = pd.DataFrame({
        'actor_id': [1, 1, 1],
        'director_id': [5, 5, 5],
        'timestamp': [1, 2, 3]
    })
    out3 = actors_and_directors(df3)
    print("Test 3 (exactly three):\n", out3)
    assert out3.shape[0] == 1
    assert (out3.iloc[0] == [1,5]).all()

    df4 = pd.DataFrame({
        'actor_id': [1, 1, 2],
        'director_id': [2, 2, 2],
        'timestamp': [1, 2, 3]
    })
    out4 = actors_and_directors(df4)
    print("Test 4 (actor 2 appears once):\n", out4)
    assert out4.shape[0] == 1
    assert (out4.iloc[0] == [1,2]).all()

if __name__ == "__main__":
    test_actors_and_directors()