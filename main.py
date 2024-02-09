import streamlit as st
import pandas as pd

# st.session_state初期化
default_session_state_values = {
    'pushed_num': 0,
    'input_sequence': "",
    'input_sequence_len': 4,
    'done_status': "",
    'result_prompt': ""
}
for key, value in default_session_state_values.items():
    if key not in st.session_state:
        st.session_state[key] = value

# ローカルcsv読み込み。
df = pd.read_csv('data.csv', encoding="shift-jis")

# タイトルを追加
#st.title("暗証番号チェックアプリ")

col1, col2, col3, col4, col5 = st.columns(5)
input_nums = col3.text_input("", value=st.session_state.input_sequence, key="input_nums")

col1, col2, col3 = st.columns([1, 3, 1])
if st.session_state.input_sequence_len != 4:
    col2.error("4桁の番号以外は検証できません")
    st.session_state.input_sequence_len = 4
    st.session_state.input_sequence = ""
    st.session_state.done_status = ""
elif st.session_state.input_sequence_len == 4:
    if st.session_state.done_status == "d":
        #col2.write(f"入力された暗証番号は {st.session_state.input_sequence} です。")
        col2.error(f"{st.session_state.result_prompt}")
        st.session_state.done_status = ""
        st.session_state.input_sequence = ""
    elif st.session_state.done_status == "":
        col2.info(f"4桁の暗証番号を入力してください")

    
# ボタンが押された場合のロジック
def handle_button_press(button_value):
    if isinstance(button_value, int):
        st.session_state.input_sequence += str(button_value)
        st.experimental_rerun()
    elif button_value == "c":
        st.session_state.input_sequence = ""
        st.experimental_rerun()
    elif button_value == "d":
        check_prompt()
        st.session_state.done_status = "d"
        st.experimental_rerun()

# 入力された暗証番号とdata.csvのnum列を比較して、一致する場合はpromptを表示
def check_prompt():
    if st.session_state.input_sequence:
        st.session_state.input_sequence_len = len(str(st.session_state.input_sequence))
        input_num = int(st.session_state.input_sequence)
        matching_row = df[df['num'] == input_num]
        if not matching_row.empty:
            st.session_state.result_prompt = matching_row.iloc[0]['prompt']
        else:
            st.session_state.result_prompt = "一致する行が見つかりませんでした。"

# レイアウトの設定
col1, col2, col3, col4, col5 = st.columns(5)

# ボタンの配置と処理
if col2.button("1", use_container_width=True):
    handle_button_press(1)
if col3.button("2", use_container_width=True):
    handle_button_press(2)
if col4.button("3", use_container_width=True):
    handle_button_press(3)
if col2.button("4", use_container_width=True):
    handle_button_press(4)
if col3.button("5", use_container_width=True):
    handle_button_press(5)
if col4.button("6", use_container_width=True):
    handle_button_press(6)
if col2.button("7", use_container_width=True):
    handle_button_press(7)
if col3.button("8", use_container_width=True):
    handle_button_press(8)
if col4.button("9", use_container_width=True):
    handle_button_press(9)
if col2.button("クリア", use_container_width=True):
    handle_button_press("c")
if col3.button("0", use_container_width=True):
    handle_button_press(0)
if col4.button("実行", use_container_width=True):
    handle_button_press("d")

#st.write(df)