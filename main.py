import streamlit as st
import pandas as pd

# Load data from data.csv
df = pd.read_csv('data.csv')

# Display the data in a table
edited_df = st.data_editor(df) #編集可能形式での表の表示
#st.write(df)

if st.button('Save as data.csv'):
    df.to_csv('data.csv', index=False)
