import streamlit as st
import time


def type_writer(msg: str, character: str, avtr):
    def delayed_stream(text):
        for char in text:
            yield char
            time.sleep(0.05)

    person = st.chat_message(character, avatar=avtr)

    return person.write_stream(delayed_stream(msg))
