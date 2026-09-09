import { useState } from "react";
import { Film, Search, Ticket, AlertCircle, Loader2, Star } from "lucide-react";
import "./App.css";

const API = "http://127.0.0.1:8000";

export default function App() {
  const [title, setTitle] = useState("");
  const [topN, setTopN] = useState(5);
  const [movies, setMovies] = useState([]);
  const [inputMovie, setInputMovie] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const getRecommendations = async (e) => {
    e.preventDefault();

    if (!title.trim()) {
      setError("Please enter a movie title.");
      return;
    }

    setLoading(true);
    setError("");
    setMovies([]);

    try {
      const res = await fetch(`${API}/recommend`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          title: title.trim(),
          top_n: Number(topN),
        }),
      });

      const data = await res.json();

      if (!res.ok) {
        setError(data.detail || "Movie not found");
      } else {
        setInputMovie(data.input_movie);
        setMovies(data.recommendations);
      }
    } catch {
      setError("Cannot connect to FastAPI server.");
    }

    setLoading(false);
  };

  return (
    <div className="app">
      <div className="overlay">
        <div className="container">
          <div className="header">
            <Film size={42} className="icon" />
            <h1 className="text-5xl font-bold text-green text-center">
               Movie Recommendation System
            </h1>{" "}
            <p>Discover movies similar to your favorite film</p>
          </div>

          <form className="search-box" onSubmit={getRecommendations}>
            <div className="input-group">
              <Search size={18} />
              <input
                type="text"
                placeholder="Enter movie title..."
                value={title}
                onChange={(e) => setTitle(e.target.value)}
              />
            </div>

            <input
              className="number"
              type="number"
              min="1"
              max="10"
              value={topN}
              onChange={(e) => setTopN(e.target.value)}
            />

            <button type="submit" disabled={loading}>
              {loading ? (
                <>
                  <Loader2 size={18} className="spin" />
                  Loading...
                </>
              ) : (
                <>
                  <Film size={18} />
                  Recommend
                </>
              )}
            </button>
          </form>

          {error && (
            <div className="error">
              <AlertCircle size={18} />
              {error}
            </div>
          )}

          {movies.length > 0 && (
            <div className="results">
              <h2>
                Recommendations for <span>{inputMovie}</span>
              </h2>

              {movies.map((movie, index) => (
                <div className="movie-card" key={index}>
                  <div className="rank">{index + 1}</div>

                  <div className="movie-info">
                    <h3>{typeof movie === "string" ? movie : movie.title}</h3>
                    <p>Similar movie recommendation</p>
                  </div>

                  <div className="ticket">
                    <Ticket size={20} />
                    <Star size={16} className="star" />
                  </div>
                </div>
              ))}
            </div>
          )}
        </div>
      </div>
    </div>
  );
}
