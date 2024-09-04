import streamlit as st
import pickle
import pandas as pd

def recommend(name):
    scores = movies_list[name]
    scores = scores.sort_values(ascending=False)
    # print(scores[1:11]['title'])
    print(scores)
    return scores[1:11]


movies_list = pickle.load(open("movies.pkl","rb"))
movie_names = movies_list.columns

st.title("Movie Recommender System")

selected_movie_name = st.selectbox(
    "Select an option",
    movie_names
)

if st.button('Recommend'):
    recommendations = recommend(selected_movie_name)
    st.write(recommendations)