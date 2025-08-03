"""
LEVEL 1

The Taxi
"""
import random

import streamlit as st
from type_writer_func import type_writer
from gemini_question_generator import easy_question
import time


def level_1():
    # Title
    st.markdown("<h1 style='text-align: center;'>Level 1</h1>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center;'>The C A B</h2>", unsafe_allow_html=True)

    if "full_question" not in st.session_state:
        st.session_state.full_question = [easy_question() for i in range(4)]
        st.session_state.question_counter = 0
        st.session_state.num_correct = 0
        st.session_state.q_number = 0
        st.session_state.question_displayed = False

    def question_and_answer(i: int):
        st.session_state.questionV2, st.session_state.answerV2 = (
            st.session_state.full_question[i][:-1].split("{"))
        st.session_state.answerV2 = st.session_state.answerV2[:-1]

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

        {"content": "Hmf. You've got your self a deal!", "role": "Taxi Man", "avatar": "taxi_man.png"}
    ]


    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []
        for i in range(len(cutscene1)):
            type_writer(cutscene1[i]["content"], cutscene1[i]["role"], cutscene1[i]["avatar"])
            st.session_state.messages.append({"content": cutscene1[i]["content"],
                                              "role": cutscene1[i]["role"],
                                              "avatar": cutscene1[i]["avatar"]})

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
            type_writer(f"*Question {i + 1}:* {st.session_state.questionV2}", "Taxi Man", "taxi_man.png")
            st.session_state.question_displayed = True

            st.session_state.messages.append({"content": f"*Question {i + 1}:* {st.session_state.questionV2}",
                                              "role": "Taxi Man", "avatar": "taxi_man.png"})

        response = st.chat_input("Answer in the form of \"Answer: x\" (for example, \"Answer: b\" is valid)",
                                 key=f"question-{st.session_state.q_number}")

        if response:
            with st.chat_message("You", avatar="the_Scholar.png"):
                st.write(f"Success: {response}")
            st.session_state.messages.append({"content": response, "role": "You", "avatar": "the_Scholar.png"})

            correct_response = ["*checks notes* Well, you're smarter than you look. That's num_correct!",
                                "Oh. Well done, Mr. Scholar--you got it right.",
                                "**OI! YOU, IN THE GREEN SHIRT! DID HE GET IT RIGHT?! YES?** Good job.",
                                "Correct! Maybe your brains will make up for your lacking brawn."]

            incorrect_response = ["Humph. That's incorrect, Mr. Scholar. You'd think that a Scholar would know his "
                                  "stuff...",
                                  "You may want to work on your brawn, since your brain don't seem to be working. That "
                                  "isn't the num_correct answer.",
                                  "All those fancy institutes couldn't teach... *sigh*. I guess we all have off days, "
                                  "Mr. Scholar. You got it wrong.",
                                  "Maybe review your notebooks, 'cause that ain't the right answer."]

            time.sleep(random.uniform(0.05, 0.30))

            if response.lower() == st.session_state.answerV2.lower():
                answer_response = random.choice(correct_response)
                st.session_state.num_correct += 1
            else:
                answer_response = random.choice(incorrect_response)

            st.session_state.pending_save.append({"content": answer_response, "role": "Taxi Man",
                                                  "avatar": "taxi_man.png"})

            type_writer(answer_response, "Taxi Man", "taxi_man.png")

            if len(st.session_state.pending_save) > 0:
                for i in st.session_state.pending_save:
                    st.session_state.messages.append({"content": i["content"],
                                                      "role": i["role"],
                                                      "avatar": i["avatar"]})
                st.session_state.pending_save = []

            st.session_state.question_displayed = False
            st.session_state.q_number += 1
            st.rerun()

    if st.session_state.q_number < 4:
        responding_to_q(st.session_state.q_number)

    elif (st.session_state.num_correct/4) <= 0.5:
        type_writer("Well, Mr. Scholar, we're here. But, I don't think you're that hot-shot everybody's talking about.",
                    "Taxi Man", "taxi_man.png")
        type_writer("I THINK YOU'RE AN IMPOSTER!!", "Taxi Man", "taxi_man.png")

        st.session_state.messages.append({"content": "Well, Mr. Scholar, we're here. But, I don't think you're that "
                                                     "hot-shot everybody's talking about.",
                                          "role": "Taxi Man",
                                          "avatar": "taxi_man.png"})
        st.session_state.messages.append({"content": "I THINK YOU'RE AN IMPOSTER!!",
                                          "role": "Taxi Man",
                                          "avatar": "taxi_man.png"})

        st.markdown("<h3 style='text-align: center;'>~ENDING 1~</h3>", unsafe_allow_html=True)
        st.markdown("<h3 style='text-align: center;'>===> Imposter<====</h3>", unsafe_allow_html=True)
        st.markdown("<h5 style='text-align: center;'>Better luck next time...</h5>", unsafe_allow_html=True)

        return False

    else:
        type_writer("Well, you proved me wrong, Mr. Scholar--you got some big brains in there. Now get on out, and"
                    " restore Euterpia!", "Taxi Man", "taxi_man.png")

        st.session_state.messages.append({"content": "Well, you proved me wrong, Mr. Scholar--you got some big brains"
                                                     " in there. Now get on out, and restore Euterpia!",
                                          "role": "Taxi Man",
                                          "avatar": "taxi_man.png"})

        return True
