import streamlit as st
import pandas as pd 
import preprocessor 
df = preprocessor.preprocess()
st.sidebar.radio(
    'Select an option',
    ('Medal Tally ','Overall Analysis','Country-Wise Analysis','Athlete-Wise Analysis')
) 
st.dataframe(df)

