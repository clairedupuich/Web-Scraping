import streamlit as st
import pandas as pd
import sys  

st.write("""
# Web Scraping App
""")

movie_db = pd.read_csv('moviedb.csv')
# st.line_chart(movie_db)