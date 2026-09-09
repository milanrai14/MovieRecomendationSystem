from model_loader import movies

# DBSCAN labels points that don't belong to any cluster as -1 ("noise").
NOISE_CLUSTER = -1


def get_recommendations(title: str, top_n: int = 5):
    matches = movies[movies["title"].str.lower() == title.lower()]

    if matches.empty:
        return None

    movie = matches.iloc[0]
    cluster = movie["dbscan_cluster"]

    if cluster == NOISE_CLUSTER:
        # This movie was never assigned to a cluster, so there is no
        # meaningful group of similar movies to recommend from.
        return []

    recs = movies[
        (movies["dbscan_cluster"] == cluster)
        & (movies["title"].str.lower() != title.lower())
    ]

    recs = recs.sort_values("imdb_score", ascending=False)

    return recs.head(top_n)[
        ["title", "genres", "release_year", "imdb_score"]
    ].to_dict(orient="records")