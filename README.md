# 📚 Book Recommendation System

A Machine Learning--based Book Recommendation System built using
Item-Based Collaborative Filtering and deployed with Streamlit.

This system recommends books similar to a selected book based on user
rating behavior using cosine similarity.

------------------------------------------------------------------------

## 🚀 Live Demo

https://bookrecomendationsystem-d7tc2pxwnc6vjpy4pmupuw.streamlit.app

------------------------------------------------------------------------

## 📌 Project Overview

The goal of this project is to build a recommendation engine that
suggests books based on similarity in user rating patterns.

The system:

-   Filters active users to reduce noise
-   Selects frequently rated books to improve similarity accuracy
-   Creates a user-book interaction matrix
-   Applies cosine similarity for item-based collaborative filtering
-   Returns top 5 similar book recommendations

------------------------------------------------------------------------

## 🧠 Recommendation Strategy

### 🔹 Popularity-Based Filtering

-   Calculated number of ratings per book
-   Computed average rating
-   Selected highly rated and frequently rated books

### 🔹 Item-Based Collaborative Filtering

-   Created pivot table (Book-Title × User-ID)
-   Replaced missing values with 0
-   Applied cosine similarity to compute similarity scores
-   Retrieved top 5 most similar books

------------------------------------------------------------------------

## 🛠️ Tech Stack

-   Python
-   Pandas
-   NumPy
-   Scikit-learn
-   Streamlit

------------------------------------------------------------------------

## 📂 Dataset

The project uses three datasets:

-   books.csv
-   users.csv
-   ratings.csv

The dataset includes:

-   Book metadata (Title, Author, ISBN, Image URL)
-   User information
-   Book ratings

------------------------------------------------------------------------

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

git clone
https://github.com/gandrabharadhwaj01/Book_Recomendation_System\
cd book-recommendation-system

### 2️⃣ Install dependencies

pip install -r requirements.txt

### 3️⃣ Run the application

streamlit run app.py

------------------------------------------------------------------------

## 📊 Key Features

-   Data preprocessing and cleaning
-   Active user filtering (200+ ratings)
-   Popular book filtering (50+ ratings)
-   Sparse matrix creation
-   Cosine similarity computation
-   Top-5 recommendation engine
-   Interactive Streamlit UI

------------------------------------------------------------------------

## 🔎 How It Works

1.  Merge books and ratings dataset
2.  Filter active users
3.  Filter frequently rated books
4.  Create pivot table (Book vs User matrix)
5.  Compute cosine similarity
6.  Recommend top 5 similar books

------------------------------------------------------------------------

## 📈 Future Improvements

-   Implement fuzzy search
-   Use SVD for dimensionality reduction
-   Add personalized user-based recommendations
-   Deploy with FastAPI backend
-   Build hybrid recommendation system

------------------------------------------------------------------------

## 👨‍💻 Author

Gandra Bharadhwaj
AI & Machine Learning Engineer

------------------------------------------------------------------------

⭐ If you found this project helpful, please give it a star on GitHub!
