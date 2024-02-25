import streamlit as st
import pandas as pd
import pickle

new_df = pd.read_json('new_df.json')

with open('similarity.pkl', 'rb') as f:
    similarity = pickle.load(f)

def recommend(movie):
    movie_index = new_df[new_df['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(enumerate(distances), reverse=True, key=lambda x: x[1])[1:6]
    movie_names = []
    for i in movies_list:
        movie_names.append(new_df.iloc[i[0]]['title'])
    return movie_names

st.title('Movie Recommendation System')

movie_input = st.text_input("Enter movie name")
if movie_input:
    recommended_movies = recommend(movie_input)
    if recommended_movies:
        st.subheader("Recommended Movies:")
        for movie in recommended_movies:
            st.write(f"- {movie}")
    else:
        st.write("No recommendations found.")
