import pandas as pd  # For data handling
import streamlit as st  # To create a web app interface
import requests  # To call the TMDB API for poster
from sklearn.feature_extraction.text import TfidfVectorizer  # NLP tool to convert text to numbers
from sklearn.metrics.pairwise import cosine_similarity  # To measure how similar two movies are

# 🔑 Your actual TMDB API key (Replace this with your real API key)
API_KEY = "cf0a26167f595f5ff3ec31218ebf74c2"

# 📥 Load datasets
movies = pd.read_csv('tmdb_5000_movies.csv')  # Movie metadata
credits = pd.read_csv('tmdb_5000_credits.csv')  # Cast & crew info

# 🔗 Merge both datasets on the title
movies = movies.merge(credits, on='title')

# 🎯 Keep only relevant columns
movies = movies[['movie_id', 'title', 'overview']]
movies['overview'] = movies['overview'].fillna('')  # Handle missing overviews

# 🔠 Convert text to TF-IDF vectors (for NLP-based similarity)
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(movies['overview'])

# 🔁 Compute cosine similarity between all movie overviews
similarity = cosine_similarity(tfidf_matrix, tfidf_matrix)


# 🎬 Function to fetch poster using TMDB API
def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=en-US"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        poster_path = data.get('poster_path')
        if poster_path:
            return f"https://image.tmdb.org/t/p/w500{poster_path}"
    return "https://via.placeholder.com/300x450?text=No+Image"


# 🤖 Function to recommend movies
def recommend(movie_title, count=12):  # Show top 'count' similar movies
    if movie_title not in movies['title'].values:
        return [], []

    idx = movies[movies['title'] == movie_title].index[0]
    sim_scores = list(enumerate(similarity[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:count+1]

    movie_indices = [i[0] for i in sim_scores]
    recommended_titles = movies['title'].iloc[movie_indices]
    recommended_ids = movies['movie_id'].iloc[movie_indices]
    posters = [fetch_poster(mid) for mid in recommended_ids]

    return recommended_titles, posters


# 🌐 Streamlit UI
st.set_page_config(page_title="Movie Recommender", layout="wide")
st.markdown("""
    <h1 style='text-align: center; color: #E50914; font-size: 40px;'>🎬 Movie Recommender</h1>
    <p style='text-align: center; font-size: 18px;'>Get similar movies based on your favorite one!</p>
""", unsafe_allow_html=True)

# 🔽 Dropdown selection
selected_movie = st.selectbox("🎥 Choose a movie:", movies['title'].values)

# ▶️ Show recommendations when button is clicked
if st.button("🔍 Recommend Movies"):
    titles, posters = recommend(selected_movie, count=12)  # Show top 12 movies

    st.subheader(f"📽️ Because you liked **{selected_movie}**, you might also enjoy:")

    for i in range(0, len(titles), 4):  # Show 4 movies per row
        cols = st.columns(4)
        for j in range(4):
            if i + j < len(titles):
                with cols[j]:
                    st.image(posters[i + j], use_container_width=True)
                    st.markdown(f"<h4 style='text-align: center;'>{titles.iloc[i + j]}</h4>", unsafe_allow_html=True)
