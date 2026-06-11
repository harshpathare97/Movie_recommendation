# 🎬 Movie Recommender

A Streamlit-based movie recommendation app that suggests similar films using TF-IDF movie tags and cosine similarity.

## 🚀 Overview

- Search for a movie by name.
- Choose the closest match from the search results.
- Get recommendations for similar movies based on genre, cast, crew, and tags.
- View top-rated movies when no movie is selected.

## 🧠 Recommendation Approach

- Uses `TfidfVectorizer` to convert movie `tags` into vector embeddings.
- Computes cosine similarity between movie tag vectors.
- Retrieves the most similar movies to the selected title.

## 🛠 Tech Stack

- Python
- Streamlit
- pandas
- scikit-learn

## 📦 Files

- `app.py` — main Streamlit app for movie recommendations
- `movies.csv` — movie dataset used for recommendations
- `requirements.txt` — package dependencies
- `preprocessing_dataset.ipynb` — optional dataset preprocessing notebook

## 📥 Installation

1. Create a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## ▶️ Run the App

```bash
streamlit run app.py
```

Then open the URL shown in the terminal.

## 📝 Dataset

The app uses `movies.csv` with columns such as:

- `imdb_id`
- `title`
- `year`
- `genres`
- `rating`
- `votes`
- `actors`
- `directors`
- `tags`
- `score`

The dataset is derived from the official IMDb non-commercial datasets.

## 💡 Usage

- Type a movie title into the search box.
- Select the movie from the dropdown.
- Click `Recommend` to view recommended movies.
- If no movie is selected, the app displays the top 10 rated movies.

## 🚀 Notes

- The recommendation engine is based on text similarity and works best with cleaned and descriptive tags.
- The app caches data loading and similarity computations to improve performance.
