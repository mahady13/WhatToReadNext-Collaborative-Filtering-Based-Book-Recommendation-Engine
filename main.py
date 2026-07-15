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