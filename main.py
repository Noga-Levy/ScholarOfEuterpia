import streamlit as st
from welcome_page import welcome
from level1 import level_1

if 'count' not in st.session_state:
    st.session_state.count = 0


def increment_sess_state():
    st.session_state.count += 1


def centered_button(text: str):
    st.markdown("----", unsafe_allow_html=True)
    columns = st.columns((2, 1, 2))
    button = columns[1].button(text)
    st.markdown("----", unsafe_allow_html=True)

    if button:
        increment_sess_state()
        st.rerun()


if st.session_state.count == 0:
    welcome()
    centered_button("Let's go!")

if st.session_state.count == 1:
    done = level_1()
    if done:
        centered_button("Level 2 ~ The docks")
