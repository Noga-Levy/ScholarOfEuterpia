import streamlit as st
from welcome_page import welcome
from level1 import level_1
from level2 import level_2
from level3 import level_3
from type_writer_func import type_writer

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

if st.session_state.count == 3:
    successful_lvl3 = level_3()
    if successful_lvl3:
        centered_button("The missing piece")

if st.session_state.count == 4:
    type_writer("It's the final piece! It's... it's--", "You", "the_scholar.png")
    st.markdown("<h1 style='text-align: center;'>CONGRATULATIONS</h1>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center;'>You've completed the game, and Euterpia will be restored!</h1>",
                unsafe_allow_html=True)

    st.markdown("<h3 style='text-align: center;'>~ENDING 4~</h3>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'>===> WINNER WINNER, MUSIC DINNER <===</h3>", unsafe_allow_html=True)
    st.markdown("<h5 style='text-align: center;'>Share this game with your friends!</h5>", unsafe_allow_html=True)
