import streamlit as st

def add_text_area():
    st.session_state.btn = str(st.session_state.btn)+" Hello World!\n"
    return

st.text_area('test')
st.text_area('btn1', key='btn',height=3, label_visibility="hidden")
st.button('click here', on_click=add_text_area)
