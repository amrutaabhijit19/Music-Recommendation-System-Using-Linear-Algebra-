import pandas as pd
# Load the dataset
def load_data(file_path):
    df = pd.read_csv(file_path)
    return df


# Features used for the mathematical model
def get_features(df):
    features = [
        "danceability",
        "energy",
        "valence",
        "acousticness"
    ]

    return df[features].values