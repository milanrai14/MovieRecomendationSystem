from fastapi import FastAPI, HTTPException
from schemas import MovieRequest
from recommender import get_recommendations

app = FastAPI(
    title="Movie Recomendation API",
    version="1.0"
    )

@app.get("/")
def home():
    return{
        "message": "Movie Recommendation API is running"
    }

@app.post("/recommend")
def recommend(request: MovieRequest):
    results = get_recommendations(
        request.title,
        request.top_n
    )

    if results is None:
        raise HTTPException(
            status_code=404,
            detail="Movie not found"
        )

    return{
        "input_movie" : request.title,
        "recommendations": results
    }