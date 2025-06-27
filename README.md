
# 🎬 Movie Recommender System

A smart, content-based movie recommendation web app built with **Streamlit**, **Pandas**, and **Scikit-learn**, powered by the **TMDB API** to fetch real-time movie posters. Just pick your favorite movie and instantly discover 12 similar ones!

---

## 🚀 Live Demo

📌 Coming soon — deploy on **Streamlit Cloud**, **Render**, or **Vercel** for public access.

---

## 📷 Preview

<p align="center">
  <img src="https://via.placeholder.com/900x500?text=App+Screenshot" alt="App Screenshot">
</p>

---

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

## 🔄 Future Improvements

- ✅ Add genre/tag-based filtering  
- ✅ Use combined content + collaborative filtering  
- ✅ Show trailers, ratings, and release dates  
- ✅ Deploy to public URL using Streamlit Cloud or Render  
- ✅ Cache API responses for faster UX

---

## 🙋‍♂️ Author

**Shaikh Saif**  
💼 [LinkedIn](https://www.linkedin.com/) | 💻 [GitHub](https://github.com/)

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

⭐️ **If you like this project, consider giving it a star!**
