import streamlit as st
import pandas as pd
import numpy as np

new_df = pd.read_json('new_df.json')

data = np.load('similarity_matrix123.npz')

# Extract the similarity matrix
similarity = data['similarity']

def recommend(movie):
    movie_index = new_df[new_df['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(enumerate(distances), reverse=True, key=lambda x: x[1])[1:6]
    movie_names = []
    for i in movies_list:
        movie_names.append(new_df.iloc[i[0]]['title'])
    return movie_names


st.markdown("<h1 style='margin-top:-50px;'>Movie Recommendation System</h1>", unsafe_allow_html=True)


movie_input = st.selectbox("Select a movie", new_df['title'])

if movie_input:
    recommended_movies = recommend(movie_input)
    if recommended_movies:
        st.subheader("Recommended Movies:")
        for movie in recommended_movies:
            st.write(f"- {movie}")
    else:
        st.write("No recommendations found.")
