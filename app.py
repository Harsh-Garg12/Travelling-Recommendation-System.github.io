import pickle
import pandas as pd
import numpy as np
import streamlit as st
from serpapi import GoogleSearch
import gzip
import pickletools


st.title("Travelling Recommendation System")

# Extract data from pickle file
pickle_off = pd.read_pickle(open("travel.pkl", "rb"))
cosine_similarity1 = pd.read_pickle(open("cosine_similarity1.pkl", "rb"))
cosine_similarity2 = pd.read_pickle(open("cosine_similarity2.pkl", "rb"))
cosine_similarity3 = pd.read_pickle(open("cosine_similarity3.pkl", "rb"))


# Recommendation function
def recommend(City, Place):
    index = pickle_off[pickle_off['City'] == City][pickle_off['Place'] == Place].index[0]
    if(index<5000):
        distances = sorted(list(enumerate(cosine_similarity1[index])), reverse=True, key=lambda x:x[1])
    elif(index<10000):
        distances = sorted(list(enumerate(cosine_similarity2[5000-index])), reverse=True, key=lambda x: x[1])
    else:
        distances = sorted(list(enumerate(cosine_similarity3[10000-index])), reverse=True, key=lambda x: x[1])
    recommend_places = []
    for i in distances[1:7]:
        recommend_places.append(((pickle_off.iloc[i[0]].City, pickle_off.iloc[i[0]].Place), (pickle_off.iloc[i[0]].Rating,
                                 pickle_off.iloc[i[0]].Count)))
    return recommend_places


if __name__ == "__main__":
    # adding "select" as the first and default choice
    City = st.selectbox('Select City', options=sorted(pickle_off['City'].unique()))
    # display selectbox 2 if manufacturer is not "select"
    if City != 'select':
        Place = st.selectbox('Select Place', options=sorted(pickle_off[pickle_off['City']==City]['Place']))
    if st.button('Recommend'):
        recommend_places = recommend(City, Place)
        # st.write('City' + 'Place' + 'Rating')
        recommend_info = []
        for i in recommend_places:
            dict = {}
            params = {
                "engine": "google",
                "tbm": "isch",
                "q": "https://www.google.com/search?q=" + i[0][1],
                "api_key": "e73b3ffcc8ccb7e628fabd87c3e4709402aae8d682d67f55d5321436cb0b86f4"
            }
            search = GoogleSearch(params)
            results = search.get_dict()
            images_results = results['images_results'][0]['thumbnail']
            # st.write(images_results)
            dict['image'] = images_results
            dict['city'] = i[0][0]
            dict['place'] = i[0][1]
            dict['rating'] = i[1][0]
            dict['count'] = i[1][1]
            # st.image(images_results)
            # st.write(i[0] + ', ' + i[1],  round(i[2],  2))
            recommend_info.append(dict)

        with st.container():
            col1, col2, col3 = st.columns(3)
            with col1:
                st.subheader(recommend_info[0]['city'] + ', ' + recommend_info[0]['place'])
                st.write(round(recommend_info[0]['rating'], 2), ' average based on ', recommend_info[0]['count'], ' reviews')
                st.image(recommend_info[0]['image'])

            with col2:
                st.subheader(recommend_info[1]['city'] + ', ' + recommend_info[1]['place'])
                st.write(round(recommend_info[1]['rating'], 2), ' average based on ', recommend_info[1]['count'], ' reviews')
                st.image(recommend_info[1]['image'])

            with col3:
                st.subheader(recommend_info[2]['city'] + ', ' + recommend_info[2]['place'])
                st.write(round(recommend_info[2]['rating'],2), ' average based on ', recommend_info[2]['count'], ' reviews')
                st.image(recommend_info[2]['image'])

        with st.container():
            col1, col2, col3 = st.columns(3)
            with col1:
                st.subheader(recommend_info[3]['city'] + ', ' + recommend_info[3]['place'])
                st.write(round(recommend_info[3]['rating'], 2), ' average based on ', recommend_info[3]['count'], ' reviews')
                st.image(recommend_info[3]['image'])
        
            with col2:
                st.subheader(recommend_info[4]['city'] + ', ' + recommend_info[4]['place'])
                st.write(round(recommend_info[4]['rating'], 2), ' average based on ', recommend_info[4]['count'], ' reviews')
                st.image(recommend_info[4]['image'])
        
            with col3:
                st.subheader(recommend_info[5]['city'] + ', ' + recommend_info[5]['place'])
                st.write(round(recommend_info[5]['rating'],2), ' average based on ', recommend_info[5]['count'], ' reviews')
                st.image(recommend_info[5]['image'])


