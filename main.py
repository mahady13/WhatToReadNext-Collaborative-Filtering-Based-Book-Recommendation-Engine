import streamlit as st
import pandas as pd
import numpy as np
import joblib

@st.cache_resource
def load_assets():
    books_with_ratings=joblib.load("preprocessed_list")
    books=pd.read_csv("Books.csv")
    pt=joblib.load("pivot_table.pkl")
    similarity=joblib.load("similarity.pkl")
    return books_with_ratings,books,pt,similarity
books_with_ratings,books,pt,similarity=load_assets()


def recommend_books(book):
    indexs = np.where(pt.index == book)[0][0]
    similar_books = sorted(list(enumerate(similarity[indexs])), key=lambda x: x[1], reverse=True)[1:6]
    data = []

    for i in similar_books:
        item = []
        temp_df = books_with_ratings[books_with_ratings['Book-Title'] == pt.index[i[0]]]
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')["Book-Author"].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')["Image-URL-L"].values))
        data.append(item)
    return data

st.sidebar.title("About This Project")
st.sidebar.info("""
    **WhatToReadNext** is a Book Recommendation Engine built using:
    - **Collaborative Filtering** algorithm
    - **Cosine Similarity** to calculate distance between books
    - Dataset: 270,000+ books from Book-Crossing Dataset
    """)
st.sidebar.write("---")
st.sidebar.markdown("Developed by **Mohiuddin Mahady**")
st.sidebar.link_button(url="https://linkedin.com/in/mohiuddin-mahady",label="LinkedIn",use_container_width=True)
st.sidebar.link_button(label="Github",url="https://github.com/mahady13",use_container_width=True)

st.title("WhatToReadNext")
st.info("""**WhatToReadNext** recommends books based on collaborative filtering algorithm, analyzing ratings from thousands of top readers.""")
input_book=st.selectbox("Enter a book title you read:",books_with_ratings['Book-Title'].sort_values().unique())
