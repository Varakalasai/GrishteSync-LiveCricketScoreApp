# Created with GrishteSync
# https://suryasticsai.github.io/GrishteSync
# Suryasticsai | suryasticsai@gmail.com
import streamlit as st
import requests
import json
from PIL import Image
from streamlit import caching
import time

st.title("Live Cricket Score App")

image = Image.open("https://i.ibb.co/RGmb4FKk/1781072041102.png")
st.image(image)

def get_live_scores():
    try:
        response = requests.get('https://cricapi.com/api/cricketScore?apikey=YOUR_API_KEY')
        data = json.loads(response.text)
        return data
    except Exception as e:
        st.error("Error fetching data: " + str(e))

if st.button('Refresh'):
    caching.clear_cache()
    data = get_live_scores()
    if data:
        st.write(data)

st.markdown("<br><br>", unsafe_allow_html=True)

st.markdown("Made with GrishteSync | Suryasticsai | suryasticsai@gmail.com", unsafe_allow_html=True)