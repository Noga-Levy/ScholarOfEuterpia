"""
LEVEL 2

Sea Shanty
"""
import random

import streamlit as st
from type_writer_func import type_writer
from type_writer_func import narator
from gemini_question_generator import intermediate_question
import time


def level_2():
    # Title
    st.markdown("<h1 style='text-align: center;'>Level 2</h1>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center;'>Sea Shanty</h2>", unsafe_allow_html=True)

    if "full_question" not in st.session_state:
        st.session_state.full_question = [intermediate_question() for i in range(4)]
        st.session_state.question_counter = 0
        st.session_state.num_correct = 0
        st.session_state.q_number = 0
        st.session_state.question_displayed = False

    def question_and_answer(i: int):
        st.session_state.questionV2, st.session_state.answerV2 = (
            st.session_state.full_question[i][:-1].split("{"))
        st.session_state.answerV2 = st.session_state.answerV2[:-1]

    cutscene2 = [
        {"content": "Hmm? Oh, don't let me bother you--continue to music!", "role": "You", "avatar": "the_Scholar.png"},

        {"content": "*schwing*", "role": "Pirate", "avatar": "pirate.png"},

        {"content": "... I went aboard a pirate ship again, didn't I?", "role": "You", "avatar": "the_Scholar.png"},

        {"content": "This is the fourth time, land lubber.", "role": "Pirate", "avatar": "pirate.png"},

        {"content": "Damn it. And I thought I got the right boat number...", "role": "You",
         "avatar": "the_Scholar.png"},

        {"content": "Ye were mistaken. And now, ye be dissected--the other scholars won't pay ye ransom again. Always "
                    " be ruining our fun, yer little committee", "role": "Pirate", "avatar": "pirate.png"},

        {"content": "Yeah, they can be penny-pinchers sometimes", "role": "You", "avatar": "the_Scholar.png"},

        {"content": "EXACTLY! Why can't they--uh, I mean, enough talk! Yer be coming with us.", "role": "Pirate",
         "avatar": "pirate.png"},

        {"content": "Ah! Wait!", "role": "You", "avatar": "the_Scholar.png"},

        {"content": "What?", "role": "Pirate", "avatar": "pirate.png"},

        {"content": "You guys wouldn't be here if you couldn't bribe all the boat guards, meaning you got a large chest"
                    " recently--", "role": "You", "avatar": "the_Scholar.png"},

        {"content": "--Me brother is the leader of the guard, no need for bribes. But, go on, land lubber--we did get "
                    " some booty.", "role": "Pirate", "avatar": "pirate.png"},

        {"content": "... Huh. Er, alright... where was I? Ah yes, you probably need help opening the chest, right? "
                    "Since they can only be answered by answering some music theory questions?",
         "role": "You", "avatar": "the_Scholar.png"},

        {"content": "Only when ye arrr around, me matey. But yes. I forgot about that. Fine, help us, and we'll take "
                    "ye where ye need to go.",
         "role": "Pirate", "avatar": "pirate.png"},

        {"content": "How do I know you will keep your word?", "role": "You", "avatar": "the_Scholar.png"},

        {"content": "*Me hearty.* I thought we were bros!", "role": "Pirate", "avatar": "pirate.png"},

        {"content": "I'm just kidding--of course we're bros. Now, tell me the questions!",
         "role": "You", "avatar": "the_Scholar.png"}
    ]

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []
        narator("*Exiting the carriage with a skip in your step, you waltz over your boat, writing a 5-star review"
                " of the ride on fantasy Uber. Eventually, you set aboard a boat that's playing a sea shanty in the "
                "wrong key. Except, the music stops once you get on...*")
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
            type_writer(f"*Question {i + 1}:* {st.session_state.questionV2}", "Pirate", "pirate.png")
            st.session_state.question_displayed = True

            st.session_state.messages.append({"content": f"*Question {i + 1}:* {st.session_state.questionV2}",
                                              "role": "Pirate", "avatar": "pirate.png"})

        response = st.chat_input("Answer in the form of \"Answer: x\" (for example, \"Answer: b\" is valid)",
                                 key=f"level2-{st.session_state.q_number}")

        if response:
            with st.chat_message("You", avatar="the_Scholar.png"):
                st.write(f"Success: {response}")
            st.session_state.messages.append({"content": response, "role": "You", "avatar": "the_Scholar.png"})

            correct_response = ["Ye gots it, land lubber!",
                                "*click click click* Me booty accepts! Correct!",
                                "Yarr! If me crew could plunder as well as ye can answer, we'd have enough booty to"
                                " hire ye!",
                                "YESYESYES--uh, I mean, good work, land lubber, ye be correct!"]

            incorrect_response = ["Narrr! Ye aren't correct!",
                                  "ARGGG! Nar, me hearty! Nar!",
                                  "The booty says ye be incorrect! Keep this up, and ye be getting the barnacle "
                                  "treatment.",
                                  "*click click click* Nar?! Me hearty, ye used to pillage these questions with ease"
                                  "--what happned?!"]

            time.sleep(random.uniform(0.05, 0.30))

            if response.lower() == st.session_state.answerV2.lower():
                answer_response = random.choice(correct_response)
                st.session_state.num_correct += 1
            else:
                answer_response = random.choice(incorrect_response)

            st.session_state.pending_save.append({"content": answer_response, "role": "Pirate",
                                                  "avatar": "pirate.png"})

            type_writer(answer_response, "Pirate", "pirate.png")

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

    elif (st.session_state.num_correct/4) < 0.75:
        type_writer("Arggg... the chest still be stuck. Me hearty, although ye will always be me best bro, I have"
                    "an appearance to uphold. I'm sorry, land lubber...",
                    "Pirate", "pirate.png")
        type_writer("CREW!! THROW THIS BOOTY-HATING MAN OVERBOARD!", "Pirate", "pirate.png")

        st.session_state.messages.append({"content": "Arggg... the chest still be stuck. Me hearty, although ye will "
                                                     "always be me best bro, I have an appearance to uphold. I'm sorry,"
                                                     " land lubber...",
                                          "role": "Pirate",
                                          "avatar": "pirate.png"})
        st.session_state.messages.append({"content": "CREW!! THROW THIS BOOTY-HATING MAN OVERBOARD!",
                                          "role": "Pirate",
                                          "avatar": "pirate.png"})

        st.markdown("<h3 style='text-align: center;'>~ENDING 2~</h3>", unsafe_allow_html=True)
        st.markdown("<h3 style='text-align: center;'>===> CANON BAAALL! <====</h3>", unsafe_allow_html=True)
        st.markdown("<h5 style='text-align: center;'>Better luck next time...</h5>", unsafe_allow_html=True)

        return False

    else:
        type_writer("Ah, me hearty--me BRO. I knew I could count on ye!", "Pirate", "pirate.png")
        type_writer("Crew, let's help this booty-lubber on his quest!", "Pirate", "pirate.png")

        st.session_state.messages.append({"content": "Ah, me hearty--me BRO. I knew I could count on ye!",
                                          "role": "Pirate",
                                          "avatar": "pirate.png"})
        st.session_state.messages.append({"content": "Crew, let's help this booty-lubber on his quest!",
                                          "role": "Pirate",
                                          "avatar": "pirate.png"})

        return True
