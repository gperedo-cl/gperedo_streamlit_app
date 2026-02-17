import streamlit as st
# from MotionAPI_UserClass import User
# from Buttons import *
import pandas as pd

#from math import ceil

#st.write("Helooooo")

mpg_df = pd.read_csv("./data/mpg.csv")

st.title("Streamlit App")

st.table(data = mpg_df)


