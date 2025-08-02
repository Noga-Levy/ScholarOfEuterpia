"""
LEVEL 1

The Taxi
"""

import streamlit as st
from type_writer_func import type_writer

st.markdown("<h1 style='text-align: center;'>Level 1</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center;'>The C A B</h2>", unsafe_allow_html=True)


cutscene1 = [
    {"content": "To the docks, please", "role": "You", "avatar": "the_Scholar.png"},

    {"content": "Sure", "role": "Taxi Man", "avatar": "taxi_man.png"},

    {"content": ".    ", "role": "Taxi Man", "avatar": "taxi_man.png"},
    {"content": ".    ", "role": "Taxi Man", "avatar": "taxi_man.png"},
    {"content": ".    ", "role": "Taxi Man", "avatar": "taxi_man.png"},

    {"content": "Wait a minute... are YOU the Scholar everyone's been makin' a fuss about?", "role": "Taxi Man",
     "avatar": "taxi_man.png"},

    {"content": "Er... Probably? I'm on a quest to retrieve the final piece the darkness destroyed",
     "role": "You", "avatar": "the_Scholar.png"},

    {"content": "Huh. I'll be honest, I'm not impressed. You don't LOOK like a butt-kickin' Scholar.",
     "role": "Taxi Man", "avatar": "taxi_man.png"},

    {"content": "Well... we have a while till we arrive. How about this: ask me some questions about music theory and "
                "let's see how many I get right.", "role": "You", "avatar": "the_Scholar.png"},

    {"content": "Hmf. You've got your self a deal!", "role": "Taxi Man", "avatar": "taxi_man.png"},

    {"content": "*Question 1:*", "role": "Taxi Man", "avatar": "taxi_man.png"}
]


# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []
    for i in range(len(cutscene1)):
        type_writer(cutscene1[i]["content"], cutscene1[i]["role"], cutscene1[i]["avatar"])
        st.session_state.messages.append({"content": cutscene1[i]["content"],
                                          "role": cutscene1[i]["role"],
                                          "avatar": cutscene1[i]["avatar"]})

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"], avatar=message["avatar"]):
        st.markdown(message["content"])


response = st.chat_input("The answer is....")
if response:
    with st.chat_message("You", avatar="the_Scholar.png"):
        st.write(f"{response}")
        st.session_state.messages.append({"content": response, "role": "You", "avatar": "the_Scholar.png"})
