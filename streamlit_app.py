import streamlit as st 
from Home import face_rec
from streamlit_webrtc import webrtc_streamer
import av
import time

st.set_page_config(
    page_title='HEART FAILURE-EDA',
    layout = 'wide',
    initial_sidebar_state='expanded'
)
st.title("Hello World")
