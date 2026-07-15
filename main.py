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
