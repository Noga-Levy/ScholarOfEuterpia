"""
LEVEL 3

The Goblin
"""
import random

import streamlit as st
from type_writer_func import type_writer
from type_writer_func import narator
from gemini_question_generator import intermediate_question
import time


def level_3():
    # Title
    st.markdown("<h1 style='text-align: center;'>Level 3</h1>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center;'>The Goblin</h2>", unsafe_allow_html=True)

    if "full_question" not in st.session_state:
        st.session_state.full_question = [intermediate_question() for i in range(3)]
        st.session_state.question_counter = 0
        st.session_state.num_correct = 0
        st.session_state.q_number = 0
        st.session_state.question_displayed = False

    def question_and_answer(i: int):
        st.session_state.questionV2, st.session_state.answerV2 = (
            st.session_state.full_question[i][:-1].split("{"))
        st.session_state.answerV2 = st.session_state.answerV2[:-1]

    cutscene2 = [
        {"content": "Oh my god. *Pant pant* I'm almost there, thank god!", "role": "You", "avatar": "the_Scholar.png"},

        {"content": "Halt!", "role": "Goblin", "avatar": "👺"},

        {"content": "Don't need to tell me twice!", "role": "You", "avatar": "the_Scholar.png"},

        {"content": "What?", "role": "Goblin", "avatar": "👺"},

        {"content": "I'm *tired*! I haven't touched this much grass in YEARS!", "role": "You",
         "avatar": "the_Scholar.png"},

        {"content": "... What is wrong with you", "role": "Goblin", "avatar": "👺"},

        {"content": "A lot. But, I assume you have a script, right?", "role": "You", "avatar": "the_Scholar.png"},

        {"content": "Uh, yeah. I do", "role": "Goblin", "avatar": "👺"},

        {"content": "Alright then, you can continue on with it", "role": "You", "avatar": "the_Scholar.png"},

        {"content": "Aw, thanks, man! EHM HEH HEM--Welcome to my bridge, tired one! If passing is the wish of thee,"
                    " answer my riddles three! Succeed, and get your magic needs, but fail and the world will "
                    "hear a tragic tale", "role": "Goblin", "avatar": "👺"},

        {"content": "Ooh sounds fun!", "role": "You", "avatar": "the_Scholar.png"},

        {"content": "RIDDLE 1: What runs but never walks--", "role": "Goblin", "avatar": "👺"},

        {"content": "Oo, sorry to interrupt! Could the riddles be music theory based instead?", "role": "You",
         "avatar": "the_Scholar.png"},

        {"content": "Uhh. Sure, I guess. I think I have some... Aha! Here they are!",
         "role": "Goblin", "avatar": "👺"},

        {"content": "Alright, let's do this!", "role": "You", "avatar": "the_Scholar.png"},
    ]

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []
        narator("*After a week of jolly travelling with your pirate matey, you arrived at the outermost island of "
                "Euterpia and bid your friends goodbye. With your map in hand, nothing could stop you!*")
        narator("*Well, ... maybe one thing. Or somebody. Somecreature? Argh. I'm not paid enough for this job...*")
        for i in range(len(cutscene2)):
            type_writer(cutscene2[i]["content"], cutscene2[i]["role"], cutscene2[i]["avatar"])
            st.session_state.messages.append({"content": cutscene2[i]["content"],
                                              "role": cutscene2[i]["role"],
                                              "avatar": cutscene2[i]["avatar"]})

    else:
        # Display chat messages from history on app rerun
        for message in st.session_state.messages:
            with st.chat_message(message["role"], avatar=message["avatar"]):
                st.markdown(message["content"])

    if "pending_save" not in st.session_state:
        st.session_state.pending_save = []

    def responding_to_q(i):
        if not st.session_state.question_displayed:
            question_and_answer(i)
            type_writer(f"*RIDDLE {i + 1}:* {st.session_state.questionV2}", "Goblin", "👺")
            st.session_state.question_displayed = True

            st.session_state.messages.append({"content": f"*Question {i + 1}:* {st.session_state.questionV2}",
                                              "role": "Goblin", "avatar": "👺"})

        response = st.chat_input("Answer in the form of \"Answer: x\" (for example, \"Answer: b\" is valid)",
                                 key=f"level2-{st.session_state.q_number}")

        if response:
            with st.chat_message("You", avatar="the_Scholar.png"):
                st.write(f"Success: {response}")
            st.session_state.messages.append({"content": response, "role": "You", "avatar": "the_Scholar.png"})

            correct_response = ["Correct-amundo! NEXT!",
                                "Impressive! NEXT!",
                                "You... actually got it correct?! Wow, ok. NEXT!",
                                "Yep! You're pretty good! NEXT!"]

            incorrect_response = ["Nope, ehehehe! NEXT!",
                                  "Not it! NEXT!",
                                  "Don't cry. But's that incorrect. NEXT!",
                                  "ERR! Incorrect! NEXT!"]

            time.sleep(random.uniform(0.05, 0.30))

            if response.lower() == st.session_state.answerV2.lower():
                answer_response = random.choice(correct_response)
                st.session_state.num_correct += 1
            else:
                answer_response = random.choice(incorrect_response)

            st.session_state.pending_save.append({"content": answer_response, "role": "Goblin",
                                                  "avatar": "👺"})

            type_writer(answer_response, "Goblin", "👺")

            if len(st.session_state.pending_save) > 0:
                for i in st.session_state.pending_save:
                    st.session_state.messages.append({"content": i["content"],
                                                      "role": i["role"],
                                                      "avatar": i["avatar"]})
                st.session_state.pending_save = []

            st.session_state.question_displayed = False
            st.session_state.q_number += 1
            st.rerun()

    if st.session_state.q_number < 3:
        responding_to_q(st.session_state.q_number)

    elif (st.session_state.num_correct/3) < 1:
        type_writer(f"EHEHEH! YOU ONLY ANSWERED {st.session_state.num_correct} CORRECTLY! BEGONE!",
                    "Goblin", "👺")

        st.session_state.messages.append({"content": f"EHEHEH! YOU ONLY ANSWERED {st.session_state.num_correct} "
                                                     f"CORRECTLY! BEGONE!",
                                          "role": "Goblin",
                                          "avatar": "👺"})

        st.markdown("<h3 style='text-align: center;'>~ENDING 3~</h3>", unsafe_allow_html=True)
        st.markdown("<h3 style='text-align: center;'>===> TRAGIC TALE <====</h3>", unsafe_allow_html=True)
        st.markdown("<h5 style='text-align: center;'>Better luck next time... What are you still doing here? "
                    "BEGONE! </h5>", unsafe_allow_html=True)

        return False

    else:
        type_writer("No... no... no!! You got all of them right! Never in a thousand years has anybody managed to"
                    " do that! Oh, my parents are going to be so disappointed, but... you may pass.",
                    "Goblin", "👺")

        st.session_state.messages.append({"content": "No... no... no!! You got all of them right! Never in a thousand "
                                                     "years has anybody managed to"
                                                     " do that! Oh, my parents are going to be so disappointed, but... "
                                                     "you may pass.",
                                          "role": "Goblin",
                                          "avatar": "👺"})

        return True
