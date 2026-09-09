from fastapi import FastAPI, HTTPException
from schemas import MovieRequest
from recommender import get_recommendations

app = FastAPI(
    title="Movie Recomendation API")