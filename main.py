import streamlit as st
from data_loader import load_data
from recommender import get_recommendations


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="TuneMatch 🎧",
    page_icon="🎧",
    layout="centered"
)


# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

/* ---------- MAIN PAGE ---------- */

.stApp {
    background: linear-gradient(
        135deg,
        #fff5fa 0%,
        #f7efff 50%,
        #eef5ff 100%
    );
    color: #333333;
}


/* ---------- ALL NORMAL TEXT ---------- */

.stApp p,
.stApp label,
.stApp span,
.stApp div {
    color: #333333;
}


/* ---------- TITLE ---------- */

.main-title {
    text-align: center;
    font-size: 46px;
    font-weight: 800;
    color: #7b2cbf !important;
    margin-top: 10px;
    margin-bottom: 5px;
}

.subtitle {
    text-align: center;
    font-size: 18px;
    color: #666666 !important;
    margin-bottom: 25px;
}


/* ---------- METRICS ---------- */

[data-testid="stMetricLabel"] {
    color: #6d597a !important;
    font-weight: 600 !important;
}

[data-testid="stMetricValue"] {
    color: #7b2cbf !important;
    font-weight: 800 !important;
}


/* ---------- SECTION HEADINGS ---------- */

.section-title {
    color: #7b2cbf !important;
    font-size: 26px;
    font-weight: 750;
    margin-top: 15px;
    margin-bottom: 8px;
}


/* ---------- INPUT LABEL ---------- */

.stMultiSelect label {
    color: #5a3d66 !important;
    font-weight: 650 !important;
}


/* ---------- SELECTED SONG BOX ---------- */

.pick-card {
    background: white;
    padding: 14px 18px;
    border-radius: 16px;
    margin: 8px 0;
    border: 1px solid #eadcf5;
    box-shadow: 0 4px 12px rgba(123, 44, 191, 0.08);
}

.pick-song {
    font-size: 18px;
    font-weight: 700;
    color: #333333 !important;
}

.pick-artist {
    font-size: 14px;
    color: #777777 !important;
    margin-top: 3px;
}


/* ---------- BUTTON ---------- */

.stButton > button {
    width: 100%;
    border-radius: 14px;
    border: none;
    padding: 12px 20px;
    background: linear-gradient(
        90deg,
        #9d4edd,
        #c77dff
    );
    color: white !important;
    font-size: 17px;
    font-weight: 700;
    box-shadow: 0 5px 15px rgba(157, 78, 221, 0.25);
}

.stButton > button:hover {
    background: linear-gradient(
        90deg,
        #7b2cbf,
        #9d4edd
    );
    color: white !important;
}


/* ---------- RECOMMENDATION CARDS ---------- */

.song-card {
    background: rgba(255, 255, 255, 0.96);
    padding: 20px 22px;
    border-radius: 20px;
    margin: 14px 0;
    border: 1px solid #eadcf5;
    box-shadow: 0 6px 18px rgba(123, 44, 191, 0.10);
}

.song-number {
    font-size: 15px;
    font-weight: 800;
    color: #9d4edd !important;
    margin-bottom: 5px;
}

.song-name {
    font-size: 23px;
    font-weight: 750;
    color: #292929 !important;
    margin-bottom: 5px;
}

.artist {
    font-size: 15px;
    color: #666666 !important;
}

.similarity {
    display: inline-block;
    margin-top: 12px;
    padding: 6px 12px;
    border-radius: 20px;
    background: #f3e5ff;
    color: #7b2cbf !important;
    font-size: 14px;
    font-weight: 700;
}


/* ---------- INFO / WARNING ---------- */

.stAlert p {
    color: #444444 !important;
}


/* ---------- EXPANDER ---------- */

[data-testid="stExpander"] {
    background: rgba(255, 255, 255, 0.75);
    border: 1px solid #eadcf5;
    border-radius: 16px;
}

[data-testid="stExpander"] summary {
    color: #6a1b9a !important;
    font-weight: 700;
}


/* ---------- DIVIDER ---------- */

hr {
    border: none;
    height: 1px;
    background: #eadcf5;
    margin: 25px 0;
}


/* ---------- FOOTER ---------- */

.footer {
    text-align: center;
    color: #888888 !important;
    font-size: 13px;
    margin-top: 35px;
    margin-bottom: 20px;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# LOAD DATA
# =========================================================

file_path = "final.csv"

df = load_data(file_path)


# =========================================================
# HEADER
# =========================================================

st.markdown(
    '<div class="main-title">🎧 TuneMatch</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Find songs that match your vibe using Linear Algebra ✨'
    '</div>',
    unsafe_allow_html=True
)


# =========================================================
# DATASET INFO
# =========================================================

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("🎵 Songs", len(df))

with col2:
    st.metric("🎤 Artists", df["artist_name"].nunique())

with col3:
    st.metric("🌎 Languages", df["language"].nunique())


st.markdown("---")


# =========================================================
# SONG SELECTION
# =========================================================

st.markdown(
    '<div class="section-title">💗 Tell us what you love</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<p style="color:#666666 !important;">'
    'Pick <b>3 songs</b> you already love, and we\'ll find '
    'songs with a similar musical vibe! 🎶'
    '</p>',
    unsafe_allow_html=True
)


song_options = sorted(
    df["track_name"].dropna().unique()
)


selected_songs = st.multiselect(
    "🎵 Choose your favourite songs",
    song_options,
    max_selections=3,
    placeholder="Search for a song..."
)


# =========================================================
# SHOW SELECTED SONGS
# =========================================================

if selected_songs:

    st.markdown(
        '<div class="section-title">💕 Your picks</div>',
        unsafe_allow_html=True
    )

    for song in selected_songs:

        song_info = df[
            df["track_name"] == song
        ].iloc[0]

        # IMPORTANT:
        # No indentation inside the HTML string.
        card = f"""
<div class="pick-card">
<div class="pick-song">🎵 {song}</div>
<div class="pick-artist">🎤 {song_info["artist_name"]} &nbsp; • &nbsp; 🌎 {song_info["language"]}</div>
</div>
"""

        st.markdown(
            card,
            unsafe_allow_html=True
        )


# =========================================================
# RECOMMENDATIONS
# =========================================================

if len(selected_songs) == 3:

    st.write("")

    if st.button("✨ Find My Songs ✨"):

        with st.spinner("🎶 Finding songs that match your vibe..."):

            recommendations = get_recommendations(
                df,
                selected_songs,
                top_n=3
            )


        # =================================================
        # RESULTS
        # =================================================

        if (
            recommendations is not None
            and not recommendations.empty
        ):

            st.markdown("---")

            st.markdown(
                '<div class="section-title">'
                '🌷 Your Top 3 Recommendations'
                '</div>',
                unsafe_allow_html=True
            )

            st.markdown(
                '<p style="color:#666666 !important;">'
                'Based on the audio features of your selected songs '
                'and cosine similarity 💫'
                '</p>',
                unsafe_allow_html=True
            )


            # ---------------------------------------------
            # RECOMMENDATION CARDS
            # ---------------------------------------------

            for index, (_, song) in enumerate(
                recommendations.iterrows(),
                start=1
            ):

                similarity_percentage = (
                    song["similarity"] * 100
                )

                card = f"""
<div class="song-card">
<div class="song-number">#{index} 🎧</div>
<div class="song-name">{song["track_name"]}</div>
<div class="artist">🎤 {song["artist_name"]} &nbsp; • &nbsp; 🌎 {song["language"]}</div>
<div class="similarity">💜 Similarity: {similarity_percentage:.2f}%</div>
</div>
"""

                st.markdown(
                    card,
                    unsafe_allow_html=True
                )


            # =============================================
            # MATH EXPLANATION
            # =============================================

            st.markdown("")

            with st.expander(
                "🧮 How did we choose these songs?"
            ):

                st.markdown(
                    "Each song is represented as a "
                    "**4-dimensional feature vector**:"
                )

                st.latex(
                    r"""
                    [danceability,\ energy,\ valence,\ acousticness]
                    """
                )

                st.markdown(
                    "Your three selected songs are averaged "
                    "to create your **user preference vector**."
                )

                st.markdown(
                    "We then calculate the cosine similarity "
                    "between your preference vector and every "
                    "candidate song:"
                )

                st.latex(
                    r"""
                    \cos(\theta)
                    =
                    \frac{A \cdot B}
                    {\|A\|\|B\|}
                    """
                )

                st.markdown(
                    "Songs with the highest similarity scores "
                    "are recommended to you! 🎵✨"
                )


        else:

            st.warning(
                "🥲 I couldn't find enough matching songs. "
                "Try choosing different songs!"
            )


# =========================================================
# ASK FOR MORE SONGS
# =========================================================

elif len(selected_songs) > 0:

    remaining = 3 - len(selected_songs)

    st.info(
        f"💭 Pick {remaining} more "
        f"{'song' if remaining == 1 else 'songs'} to continue!"
    )


# =========================================================
# FOOTER
# =========================================================

st.markdown(
    '<div class="footer">'
    'Made with 💜 using Python, Streamlit & Linear Algebra'
    '<br>'
    '🎧 TuneMatch • Personalized Song Recommendation'
    '</div>',
    unsafe_allow_html=True
)