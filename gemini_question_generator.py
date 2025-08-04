import google.generativeai
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv(dotenv_path=".env")

# Get API key from environment variable
apiKey = os.getenv("GEMINI_API_KEY")

# Configure the genai library with your API key
google.generativeai.configure(api_key=apiKey)


def easy_question():
    model = google.generativeai.GenerativeModel(model_name="gemini-1.5-flash")

    question = model.generate_content(
        contents="You are an easy trivia question generator. Your task is to create a music theory question and format"
                 "it strictly as follows: [Question] (a) Option (b) Option (c) Option (d) None of the options "
                 "{Answer: Ans}. Here are a few examples:"
                 "1. [What is a triad?] (a) Three-note chord (b) A type of rhythm (c) A musical scale "
                 "(d) None of the options {Answer: a}"
                 "2. [What does a sharp symbol (#) do to a note?] (a) Lowers it by a half step "
                 "(b) Raises it by a whole step (c) Raises it by a half step (d) None of the options {Answer: c}"
                 "3. [Which note is the dominant in the key of C Major?] (a) C (b) G (c) F (d) None of the options "
                 "{Answer: b}."
                 "Generate a new question based on a topic not covered in the examples above,"
                 " and not about stacking, intervals between C, whole notes, dotted half notes, or 2 beats.",
    )

    return question.text


def intermediate_question():
    model = google.generativeai.GenerativeModel(model_name="gemini-1.5-flash")
    question = model.generate_content(
        contents="You are an trivia question generator that makes hard questions. Your task is to create a music theory"
                 " question and format it strictly as follows: "
                 "[Question] (a) Option (b) Option (c) Option (d) None of the options {Answer: Ans}."
                 "Here are a few examples:"
                 "1. [What is a triad?] (a) Three-note chord (b) A type of rhythm (c) A musical scale "
                 "(d) None of the options {Answer: a}"
                 "2. [What does a sharp symbol (#) do to a note?] (a) Lowers it by a half step "
                 "(b) Raises it by a whole step (c) Raises it by a half step (d) None of the options {Answer: c}"
                 "3. [Which note is the dominant in the key of C Major?] (a) C (b) G (c) F (d) None of the options "
                 "{Answer: b}."
                 "Generate a new question based on a topic not covered in the examples above, and make sure the answer "
                 "is correct",
    )

    return question.text


def hard_question():
    model = google.generativeai.GenerativeModel(model_name="gemini-1.5-flash")
    question = model.generate_content(
        contents="You are an painfully hard multiple choice trivia question generator. Your task is to create a music "
                 "theory questions and format it strictly as follows: "
                 "[Question] (a) Option (b) Option (c) Option (d) None of the options {Answer: Ans}."
                 "Here are a few examples:"
                 "1. [What is a triad?] (a) Three-note chord (b) A type of rhythm (c) A musical scale "
                 "(d) None of the options {Answer: a}"
                 "2. [What does a sharp symbol (#) do to a note?] (a) Lowers it by a half step "
                 "(b) Raises it by a whole step (c) Raises it by a half step (d) None of the options {Answer: c}"
                 "3. [Which note is the dominant in the key of C Major?] (a) C (b) G (c) F (d) None of the options "
                 "{Answer: b}."
                 "Generate a new insanely hard question based on a topic not covered in the examples above.",
    )

    return question.text


"""st.title("Gent-mini")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if "question" not in st.session_state:
    st.session_state.question = generate_question()

with st.chat_message("AI"):
    questionAI = st.session_state.question
    st.write(questionAI)
    st.session_state.messages.append({"role": "AI", "content": questionAI})

response = st.chat_input("The answer is....")
if response:
    st.session_state.messages.append({"content": response, "role": "You", "avatar": "the_Scholar.png"})

    with st.chat_message("You", avatar="the_Scholar.png"):
        st.write(f"{response}")
"""