import pandas as pd
def daily_leads_and_partners(daily_sales: pd.DataFrame) -> pd.DataFrame:
    result = daily_sales.groupby(
        ['date_id', 'make_name']
    ).nunique().reset_index().rename(columns={
        'lead_id': 'unique_leads',
        'partner_id': 'unique_partners',
    })
    return result

# --- Simple tests consistent with repository style (print + assert) ---
def test_daily_leads_and_partners():
    df1 = pd.DataFrame({
        'date_id': [1, 1, 1, 2, 2],
        'make_name': ['toyota', 'toyota', 'honda', 'toyota', 'honda'],
        'lead_id': [100, 101, 102, 100, 100],
        'partner_id': [200, 201, 200, 202, 203]
    })
    out1 = daily_leads_and_partners(df1)
    print("Test 1:")
    print(out1)
    # Check result shape
    assert set(out1.columns) == {'date_id', 'make_name', 'unique_leads', 'unique_partners'}
    # Check specific values
    toyota_1 = out1[(out1['date_id'] == 1) & (out1['make_name'] == 'toyota')]
    assert toyota_1['unique_leads'].iloc[0] == 2
    assert toyota_1['unique_partners'].iloc[0] == 2

    honda_1 = out1[(out1['date_id'] == 1) & (out1['make_name'] == 'honda')]
    assert honda_1['unique_leads'].iloc[0] == 1

    toyota_2 = out1[(out1['date_id'] == 2) & (out1['make_name'] == 'toyota')]
    assert toyota_2['unique_leads'].iloc[0] == 1
    assert toyota_2['unique_partners'].iloc[0] == 1

    df2 = pd.DataFrame({
        'date_id': [],
        'make_name': [],
        'lead_id': [],
        'partner_id': []
    })
    out2 = daily_leads_and_partners(df2)
    print("Test 2 (empty):")
    print(out2)
    assert out2.shape == (0, 4)

    df3 = pd.DataFrame({
        'date_id': [1],
        'make_name': ['tesla'],
        'lead_id': [100],
        'partner_id': [200]
    })
    out3 = daily_leads_and_partners(df3)
    print("Test 3 (single row):")
    print(out3)
    assert out3['unique_leads'].iloc[0] == 1
    assert out3['unique_partners'].iloc[0] == 1

if __name__ == "__main__":
    test_daily_leads_and_partners()