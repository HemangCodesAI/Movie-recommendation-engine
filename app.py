import streamlit as st
import pickle
import pandas as pd
import requests

st.title("Movie Recomender system")
similarity = pickle.load(open("similarity.pkl", 'rb'))


def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)

    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path


def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    movielist = []
    posterlist = []
    distances = similarity[index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        movielist.append(movies.iloc[i[0]].title)
        posterlist.append(fetch_poster(movie_id))
    return movielist, posterlist


movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
option = st.selectbox("Select the movie of your choice", movies['title'].values)

if st.button("Search similar movies"):
    names, posters = recommend(option)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])
