"""
Entry page to the game
"""

import streamlit as st

def welcome():
    st.markdown("<h1 style='text-align: center;'>Welcome, Scholar!</h1>", unsafe_allow_html=True)

    st.markdown("<h2 style='text-align: center;'>The world of Euterpia has been plunged into darkness--can you "
                "save it?</h2>", unsafe_allow_html=True)

    st.markdown("<h4 style='text-align: center;'>A long, long time ago, Euterpia was a blissful land of song and "
                "dance... but that was before the darkness arrived</h4>", unsafe_allow_html=True)

    st.markdown("<h4 style='text-align: center;'>It destroyed the musician's notes</h4>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: center;'>It destroyed the composer's theory</h4>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: center;'>And worst of all, it destroyed Euterpia's music</h4>",
                unsafe_allow_html=True)

    st.markdown("<h4 style='text-align: center;'>Luckily, a brave group of people stood up against this force, "
                "and defeated it. They called themselves the Scholars.</h4>", unsafe_allow_html=True)

    st.markdown("<h4 style='text-align: center;'>And, a millennium later, Euterpia has been restored to its former"
                "glory</h4>", unsafe_allow_html=True)

    st.markdown("<h4 style='text-align: center;'> </h4>", unsafe_allow_html=True)

    st.markdown("<h4 style='text-align: center;'>... well, almost.</h4>", unsafe_allow_html=True)

    st.markdown("<h2 style='text-align: center;'>There's still one missing piece that's keeping the land from"
                " achieving true harmony. The Scholars have sent their best--that's you!--to go retrieve it.</h2>",
                unsafe_allow_html=True)

    st.markdown("<h2 style='text-align: center;'>Are you ready for an adventure?</h2>", unsafe_allow_html=True)
