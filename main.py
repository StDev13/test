import streamlit as st
import pandas as pd
from streamlit_gsheets import GSheetsConnection


#あとはconnectionオブジェクトを作成してread()メソッド使うだけでpandsのdfになる
conn = st.connection("gsheets", type=GSheetsConnection)
df = conn.read()
# Display the data in a table
edited_df = st.data_editor(df) #編集可能形式での表の表示。ただしそのまま保存はできない(当たり前)
#st.write(df)

# click button to update worksheet
# This is behind a button to avoid exceeding Google API Quota
if st.button("Update worksheet"):
    df = conn.update(
        worksheet="sheet1",
        data=edited_df,
    )
    st.cache_data.clear()
    st.experimental_rerun()
