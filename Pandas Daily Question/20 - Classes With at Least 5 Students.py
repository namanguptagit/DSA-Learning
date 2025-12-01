import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    result = (
        courses
        .groupby("class")["student"]
        .count()
        .reset_index()
        .query("student >= 5")[["class"]]
        .sort_values("class")
        .reset_index(drop=True)
    )
    return result