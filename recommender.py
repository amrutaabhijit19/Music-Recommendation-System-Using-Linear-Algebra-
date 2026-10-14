from similarity import cosine_similarity
FEATURES = [
    "danceability",
    "energy",
    "valence",
    "acousticness"
]
def create_user_vector(df, selected_songs):
    """
    Create a user preference vector by averaging
    the feature vectors of the selected songs.
    """

    selected = df[
        df["track_name"].isin(selected_songs)
    ]

    if selected.empty:
        return None

    user_vector = selected[FEATURES].mean().values

    return user_vector


def get_recommendations(df, selected_songs, top_n=3):
    """
    Generate the top N song recommendations
    based on cosine similarity.
    """

    # Create the user's preference vector
    user_vector = create_user_vector(
        df,
        selected_songs
    )

    if user_vector is None:
        return None

    # Find the songs selected by the user
    selected = df[
        df["track_name"].isin(selected_songs)
    ]

    # Get the language(s) of the selected songs
    selected_languages = (
        selected["language"]
        .dropna()
        .unique()
    )

    # Keep only songs in the same language
    results = df[
        df["language"].isin(selected_languages)
    ].copy()

    # Calculate cosine similarity for every song
    similarities = []

    for _, song in results.iterrows():

        song_vector = song[
            FEATURES
        ].values.astype(float)

        similarity = cosine_similarity(
            user_vector,
            song_vector
        )

        similarities.append(similarity)
    # Add similarity scores
    results["similarity"] = similarities

    # Remove songs already selected by the user
    results = results[
        ~results["track_name"].isin(selected_songs)
    ]

    # Sort by highest similarity
    results = results.sort_values(
        by="similarity",
        ascending=False
    )

    # Return top 3
    return results.head(top_n)