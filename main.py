import streamlit as st
import pandas as pd
from streamlit_gsheets import GSheetsConnection


#あとはconnectionオブジェクトを作成してread()メソッド使うだけでpandsのdfになる
conn = st.connection("gsheets", type=GSheetsConnection)
df = conn.read()
# Display the data in a table
edited_df = st.data_editor(df) #編集可能形式での表の表示。ただしそのまま保存はできない(当たり前)
#st.write(df)

if st.button('Save as data.csv'):
    conn.write(df)
