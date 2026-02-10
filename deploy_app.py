import numpy as np
import pandas as pd
import streamlit as st
from scikit-learn.metrics.pairwise import cosine_similarity

# -----------------------------
# Load data
# -----------------------------
@st.cache_data
def load_data():
    books = pd.read_csv('books.csv')
    users = pd.read_csv('users.csv')
    ratings = pd.read_csv('ratings.csv')
    return books, users, ratings

books, users, ratings = load_data()

# -----------------------------
# Data preprocessing
# -----------------------------
ratings_with_books = ratings.merge(books, on='ISBN')

# Popularity-based filtering
num_rating_df = ratings_with_books.groupby('Book-Title').count()['Book-Rating'].reset_index()
num_rating_df.rename(columns={'Book-Rating': 'num_ratings'}, inplace=True)

avg_rating_df = ratings_with_books.groupby('Book-Title')['Book-Rating'].mean().reset_index()
avg_rating_df.rename(columns={'Book-Rating': 'avg_rating'}, inplace=True)

popularity_df = num_rating_df.merge(avg_rating_df, on='Book-Title')

popular_df = popularity_df[popularity_df['num_ratings'] >= 250] \
    .sort_values(by='avg_rating', ascending=False) \
    .head(50)

popular_df = popular_df.merge(books, on='Book-Title') \
    .drop_duplicates('Book-Title')[
        ['Book-Title', 'Book-Author', 'Image-URL-M', 'num_ratings', 'avg_rating']
    ]

# Collaborative filtering
x = ratings_with_books.groupby('User-ID').count()['Book-Rating'] > 200
knowledge_users = x[x].index

filtered_rating = ratings_with_books[ratings_with_books['User-ID'].isin(knowledge_users)]

y = filtered_rating.groupby('Book-Title').count()['Book-Rating'] >= 50
famous_books = y[y].index

final_ratings = filtered_rating[filtered_rating['Book-Title'].isin(famous_books)]

pt = final_ratings.pivot_table(
    index='Book-Title',
    columns='User-ID',
    values='Book-Rating'
)
pt.fillna(0, inplace=True)

similarity_scores = cosine_similarity(pt)

# -----------------------------
# Recommendation function
# -----------------------------
def recommend(book_name):
    index = np.where(pt.index == book_name)[0][0]
    similar_items = sorted(
        list(enumerate(similarity_scores[index])),
        key=lambda x: x[1],
        reverse=True
    )[1:6]

    data = []
    for i in similar_items:
        book = books[books['Book-Title'] == pt.index[i[0]]].drop_duplicates('Book-Title')
        data.append({
            "title": book['Book-Title'].values[0],
            "author": book['Book-Author'].values[0],
            "image": book['Image-URL-M'].values[0]
        })
    return data

# -----------------------------
# Streamlit UI
# -----------------------------
st.title("📚 Book Recommendation System")

selected_book = st.selectbox(
    "Select a book you like",
    pt.index
)

if st.button("Recommend"):
    recommendations = recommend(selected_book)

    st.subheader("You may also like:")
    cols = st.columns(5)

    for col, rec in zip(cols, recommendations):
        with col:
            st.image(rec["image"])
            st.text(rec["title"])
            st.caption(rec["author"])
