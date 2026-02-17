import streamlit as st
# from MotionAPI_UserClass import User
# from Buttons import *
import pandas as pd

#from math import ceil

#st.write("Helooooo")

# @st.cache_data
# def load_data(path):
#     df = pd.read_csv(path)
#     return df


mpg_df = pd.read_csv("./Data/mpg.csv")
#mpg_df_raw = load_data("./data/mpg.csv")
#mpg_df = deepcopy

st.title("Streamlit App")

st.dataframe(mpg_df)
#st.table(data = mpg_df)


