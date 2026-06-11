import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import  TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from difflib import get_close_matches

# Load Data
@st.cache_data
def load_data():
    df = pd.read_csv("movies.csv")
    df = df.dropna()
    return df

movies = load_data()

# Vectorization (Cached)
@st.cache_resource
def compute_similarity(data):
    vectorizer = TfidfVectorizer(
        stop_words="english",
        max_features=5000,
        ngram_range=(1, 2)
    )
    matrix = vectorizer.fit_transform(data["tags"])
    similarity = cosine_similarity(matrix)
    return similarity

similarity = compute_similarity(movies)

# Fast Lookup Map
title_to_index = {title: idx for idx, title in enumerate(movies["title"])}

# Recommendation Function
def find_movie(title):
    titles = movies["title"].tolist()
    match = get_close_matches(title, titles, n=1, cutoff=0.6)
    return match[0] if match else None

def recommend(movie_name, n=10):
    movie_name = find_movie(movie_name)
    
    if not movie_name:
        return "Movie not found"

    idx = title_to_index.get(movie_name)

    sim_scores = list(enumerate(similarity[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:n+1]

    movie_indices = [i[0] for i in sim_scores]
   
    return movies.iloc[movie_indices]
    
# STREAMLIT UI
st.set_page_config(page_title="Movie Recommender", page_icon="🎬", layout="wide")
st.title("🎬 Movie Recommendation")

search_query = st.text_input("Search for a movie you liked")

selected_movie = None

if search_query:
    filtered_titles = movies[movies["title"].str.contains(search_query, case=False, na=False)]
    selected_movie = st.selectbox("Select a Movie", filtered_titles["title"].values)
    
# Recommend Button
if st.button("Recommend") and selected_movie is not None:

    recommendations = recommend(selected_movie)

    st.subheader("Recommended Movies:")
    st.write(f"showing result for:{selected_movie}")
    cols = st.columns(4)

    for i, (_, movie_data) in enumerate(recommendations.iterrows()):
        with cols[i % 4]:
            st.markdown(f"### {movie_data['title']}")
            st.write(f"⭐ {movie_data['rating']} | 👍 {movie_data['votes']}")
            st.write(f"🎭 {movie_data['genres']}")
            st.write(f"🎬 {movie_data['directors']}")
            st.write(f"{movie_data['year']}")

            imdb_link = f"https://www.imdb.com/title/{movie_data['imdb_id']}"
            st.markdown(f"[View on IMDb]({imdb_link})")
            st.markdown("---")

#  Default view
if selected_movie is None:
    st.subheader("👍 Top 10 Rated Movies")

    top_movies = movies.sort_values(by=['score'], ascending=False).head(10)

    cols = st.columns(4)
    for i, (_, movie_data) in enumerate(top_movies.iterrows()):
        with cols[i % 4]:
            st.markdown(f"### {movie_data['title']}")
            st.write(f"⭐ {movie_data['rating']} | 👍 {movie_data['votes']}")
            st.write(f"🎭 {movie_data['genres']}")
            st.write(f"🎬 {movie_data['directors']}")
            st.write(f"{movie_data['year']}")


            imdb_link = f"https://www.imdb.com/title/{movie_data['imdb_id']}"
            st.markdown(f"[View on IMDb]({imdb_link})")
            st.markdown("---")