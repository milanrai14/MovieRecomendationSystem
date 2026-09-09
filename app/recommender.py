from model_loader import movies

def get_recommendations(title: str, top_n: int=5):
    movie = movies[movies["title"].str.lower() == title.lower()]

    if movie.empty():
        return None

    cluster = movie.iloc[0]['dbscan_cluster']

    recs = movies[
        (movies['dbscan_cluster'] == cluster) & 
        (movies['title'].str.lower() != title.lower())
    ]

    recs = recs.sort_values("imdb_score", ascending = False)

    return recs.head(top_n)[
        ["title", "main_genre", "release_year", "imdb_score"]
    ].to_dict(orient= "records")