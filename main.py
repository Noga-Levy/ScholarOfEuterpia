import streamlit as st
from welcome_page import welcome

if 'count' not in st.session_state:
    st.session_state.count = 0


def increment_sess_state():
    st.session_state.count += 1


button = st.button("Let's go!", on_click=increment_sess_state())

if st.session_state.count == 1:
    welcome()
