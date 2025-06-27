# 🎬 Movie Recommender System

This project is a movie recommendation system built with Streamlit and powered by a machine learning model. It recommends movies based on a selected title using cosine similarity and displays movie posters fetched from the TMDB API.


**Overview**
The movie recommendation system helps users discover movies similar to their favorites. By selecting a movie from the list, users receive a list of top 10 recommended movies along with their posters. This project leverages machine learning techniques to analyze the features of movies and find similarities between them. It uses the TMDB API to fetch and display movie posters, enhancing the user experience by providing visual context for the recommendations. The system is built with Streamlit, providing an interactive and user-friendly interface for users to explore movie recommendations easily.



## 💡 Features

- 🎥 Select any movie from TMDB's top 5000 dataset  
- 📚 Recommendations based on **movie overview (plot summary)** using **TF-IDF + Cosine Similarity**
- 🧠 Intelligent, fast, and scalable content-based filtering
- 🖼️ Posters fetched directly from **TMDB API**
- 💻 Clean, responsive, and interactive **Streamlit UI**
- ⚙️ Fully customizable for additional features like genres, ratings, or hybrid models

---

## 🧠 How It Works

1. All movie overviews are converted into **TF-IDF vectors** (ignoring common words).
2. **Cosine similarity** is computed to find how similar each movie is to the selected one.
3. The top 12 most similar movies are displayed along with their posters via **TMDB API**.

---

## 🗂️ Project Structure

```
📁 movie-recommender/
├── app.py                   # Main Streamlit app
├── tmdb_5000_movies.csv     # Movie metadata
├── tmdb_5000_credits.csv    # Cast & crew info
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation
```

---

## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/movie-recommender.git
   cd movie-recommender
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Add your TMDB API key**  
   Replace the value of `API_KEY` in `app.py`:
   ```python
   API_KEY = "your_tmdb_api_key"
   ```

4. **Run the app**
   ```bash
   streamlit run app.py
   ```

---

## 🔑 Get Your TMDB API Key

1. Create a free account on [TMDB](https://www.themoviedb.org/).
2. Go to [API settings](https://www.themoviedb.org/settings/api) under your profile.
3. Generate an API key (v3 auth) and paste it into your code.

---

## 🧾 Requirements

```txt
pandas
streamlit
scikit-learn
requests
```

You can also generate this automatically:
```bash
pip freeze > requirements.txt
```

---

**Results**

The system provides the top 10 recommended movies for any selected movie title. It also fetches and displays the posters of these recommended movies using the TMDB API.



![image](https://github.com/user-attachments/assets/2939d9e2-ddb7-4953-bc7c-17a416da992f)


## 🔄 Future Improvements

- ✅ Add genre/tag-based filtering  
- ✅ Use combined content + collaborative filtering  
- ✅ Show trailers, ratings, and release dates  
- ✅ Deploy to public URL using Streamlit Cloud or Render  
- ✅ Cache API responses for faster UX



## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

⭐️ **If you like this project, consider giving it a star!**
