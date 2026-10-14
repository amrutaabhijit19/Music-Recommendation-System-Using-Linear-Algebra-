# Personalized Music Recommendation System Using Linear Algebra
Project Overview-
The Personalized Music Recommendation System is a song recommendation application that suggests songs based on a user's musical preferences. It uses concepts from Linear Algebra to represent songs as feature vectors and identify similar songs using cosine similarity.
The system creates a user preference vector from the songs selected by the user and recommends songs with similar audio characteristics.

Dataset-
The project uses a music dataset obtained from Kaggle containing song metadata and audio features.
The dataset includes features such as:
- Danceability
- Energy
- Valence
- Acousticness
- Artist and track name
These features help represent the musical characteristics of each song.

Linear Algebra Concepts Used-
1. Vectors-Each song is represented as a vector containing its numerical audio features.
   User Preference Vector -A user preference vector is created by calculating the average of the feature vectors of the songs selected by the user.
2. Dot Product- The dot product is used in calculating the similarity between two vectors.
3. Vector Norms-Vector norms measure the magnitude of vectors and are used to normalize the dot product in the cosine similarity calculation.
4. Cosine Similarity-Cosine similarity measures the similarity between two vectors based on the angle between them. A higher similarity score indicates that the songs have more similar audio characteristics.

Methodology
1. Load the music dataset.
2. Extract the relevant audio features.
3. Represent each song as a feature vector.
4. Allow the user to select songs they enjoy.
5. Calculate the average feature vector to represent the user's preferences.
6. Compute cosine similarity between the user preference vector and the other songs.
7. Rank songs according to their similarity scores.
8. Display the recommended songs.

Limitations

- Recommendations depend on the selected audio features and may not fully reflect a user's musical preferences.
- Songs with similar audio characteristics may differ in language, genre, or cultural context.
- The system does not fully account for individual listening habits or contextual preferences.
- The dataset is static and does not update dynamically with newly released songs or changes in music trends.

Conclusion

This project demonstrates how Linear Algebra can be applied to build a personalized music recommendation system. By representing songs as vectors and using cosine similarity, the system identifies songs with audio characteristics similar to the user's preferences. The project provides a practical application of vector representation, dot products, vector norms, and similarity measures.
