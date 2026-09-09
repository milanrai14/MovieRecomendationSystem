# 🎬 Movie Recommendation System using DBSCAN

A Full-Stack Machine Learning project that recommends similar movies using the **DBSCAN clustering algorithm**. This project combines **Python, Scikit-learn, FastAPI, React, and Docker** to build a complete movie recommendation application.

---

## 📌 Project Overview

The main objective of this project is to recommend movies that are similar to a movie entered by the user. Instead of using collaborative filtering, this system uses **unsupervised learning** to cluster similar movies based on their features.

The application has three main parts:

- **Machine Learning Model** – DBSCAN clustering
- **FastAPI Backend** – Serves recommendations through REST APIs
- **React Frontend** – Provides a modern and user-friendly interface

---

## 🚀 Features

- Search movies by title
- Recommend Top-N similar movies
- DBSCAN-based clustering model
- FastAPI REST API
- React responsive frontend
- Docker containerization
- Swagger API documentation

---

## 🧠 Machine Learning

### Algorithm Used: DBSCAN

**DBSCAN (Density-Based Spatial Clustering of Applications with Noise)** is an unsupervised machine learning algorithm that groups similar data into clusters based on density.

### Why DBSCAN?

- No need to specify the number of clusters beforehand.
- Detects naturally occurring groups of similar movies.
- Identifies outlier movies as noise.
- Suitable for similarity-based recommendation systems.

### ML Workflow

1. Data collection
2. Data preprocessing
3. Feature engineering
4. Encoding categorical features
5. Feature scaling
6. DBSCAN clustering
7. Save trained model
8. Generate movie recommendations

---

## ⚡ Why FastAPI?

FastAPI is used as the backend because it is a **high-performance Python framework** designed for building APIs.

### Advantages of FastAPI

- Very fast and lightweight
- Automatic Swagger documentation
- Built-in data validation using Pydantic
- Easy integration with Machine Learning models
- Returns JSON responses efficiently

### API Endpoint

**POST** `/recommend`

#### Request

```json
{
  "title": "Inception",
  "top_n": 5
}
```

#### Response

```json
{
  "input_movie": "Inception",
  "recommendations": [
    "Interstellar",
    "Tenet",
    "The Prestige",
    "Memento",
    "The Dark Knight"
  ]
}
```

---

## 🎨 Why React?

React is used to create a modern and interactive frontend for users.

### Benefits of React

- Component-based architecture
- Fast and responsive interface
- Easy API integration using Fetch
- Better user experience than static HTML

The user simply enters a movie title, and React communicates with FastAPI to display recommendations instantly.

---




---

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| Pandas | Data Processing |
| Scikit-learn | Machine Learning |
| DBSCAN | Clustering Algorithm |
| FastAPI | Backend API |
| Pydantic | Data Validation |
| React | Frontend UI |
| JavaScript | Client-side Logic |


---

## 📂 Project Structure

```text
Movie-Recommendation-System/
│
├── backend/
│   ├── main.py
│   ├── recommender.py
│   ├── schemas.py
│   ├── model_loader.py
│   ├── requirements.txt
│   ├── models/
│   └── data/
│
├── frontend/
│   ├── src/
│   │   ├── App.jsx
│   │   ├── App.css
│   │   └── components/
│   ├── public/
│   └── package.json
│
├── notebooks/
   └── Movie_Clustering.ipynb



## 📸 Application Flow

```text
User
 │
 ▼
React Frontend
 │
 │ POST /recommend
 ▼
FastAPI Backend
 │
 ▼
DBSCAN Recommendation Model
 │
 ▼
Similar Movies Returned
 │
 ▼
React Displays Results
```

---

## 🔮 Future Improvements

- Add movie posters using TMDB API
- Filter by genre and year
- Hybrid recommendation system
- User login and favorites

---

## 👨‍💻 Author

**Milan Rai**

Machine Learning & Full-Stack Learning Project

---

