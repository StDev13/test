import streamlit as st
import pandas as pd

# Load data from data.csv
df = pd.read_csv('data.csv')

# Display the data in a table
edited_df = st.data_editor(df)
st.write(df)
