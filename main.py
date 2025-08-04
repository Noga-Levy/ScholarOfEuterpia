import streamlit as st
from welcome_page import welcome
from level1 import level_1
from level2 import level_2

if 'count' not in st.session_state:
    st.session_state.count = 0


def increment_sess_state():
    st.session_state.count += 1


def reset_level_state():
    keys_to_clear = ["messages", "pending_save", "full_question", "question_counter", "num_correct", "q_number",
                     "question_displayed", "st.session_state.questionV2", "st.session_state.answerV2"]
    for key in keys_to_clear:
        if key in st.session_state:
            del st.session_state[key]


def centered_button(text: str):
    st.markdown("----", unsafe_allow_html=True)
    columns = st.columns((2, 1, 2))
    button = columns[1].button(text)
    st.markdown("----", unsafe_allow_html=True)

    if button:
        reset_level_state()
        increment_sess_state()
        st.rerun()


if st.session_state.count == 0:
    welcome()
    centered_button("Let's go!")

if st.session_state.count == 1:
    successful_lvl1 = level_1()
    if successful_lvl1:
        centered_button("Level 2 ~ Sea Shanty")

if st.session_state.count == 2:
    successful_lvl2 = level_2()
    if successful_lvl2:
        centered_button("Level 3 ~ The Goblin")
