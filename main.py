import streamlit as st
import pandas as pd

# Load data from data.csv
data = pd.read_csv('data.csv')

# Display the data in a table
st.write(data)
