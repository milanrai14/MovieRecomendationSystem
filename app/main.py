from fastapi import FastAPI, HTTPException
import pandas as pd
import joblib

app = FastAPI(title="Movie Recommendation API")


titles = pd.read_csv("titles.csv")
credits = pd.read_csv("credits.csv")

# Merge datasets
df = pd.merge(titles, credits, on="id", how="left")

# Load trained DBSCAN model
dbscan = joblib.load("dbscan_model.pkl")

# Attach cluster labels
df["cluster"] = dbscan.labels_


@app.get("/")
def home():
    return {"message": "Movie Recommendation System"}


@app.get("/recommend/{movie_title}")
def recommend_movie(movie_title: str):

    # Search movie (case-insensitive)
    movie = df[df["title"].str.lower() == movie_title.lower()]

    if movie.empty:
        raise HTTPException(
            status_code=404,
            detail="Movie not found"
        )

    cluster = movie.iloc[0]["cluster"]

    # Outlier movie
    if cluster == -1:
        return {
            "movie": movie_title,
            "message": "This movie is an outlier. No similar movies found."
        }

    # Top 5 movies from same cluster
    recommendations = (
        df[(df["cluster"] == cluster) &
           (df["title"] != movie.iloc[0]["title"])]
        ["title"]
        .drop_duplicates()
        .head(5)
        .tolist()
    )

    return {
        "movie": movie.iloc[0]["title"],
        "cluster": int(cluster),
        "recommended_movies": recommendations
    }