import joblib
import pandas as pd

movies = pd.read_csv('models\movies.csv')

cluster_model = joblib.load("models\dbscan_model.pkl")
scaler = joblib.load("models\scaler.pkl")
print(movies.columns.tolist())