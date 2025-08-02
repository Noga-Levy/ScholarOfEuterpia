from google import genai
from google.genai import types
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv(dotenv_path=".env")

# Get API key from environment variable
apiKey = os.getenv("GEMINI_API_KEY")

# Initialize Gemini client
client = genai.Client()


def easy_question():
    question = client.models.generate_content(
        model="gemini-1.5-flash",
        contents="Create an easy multiple choice trivia question based on the fundamentals from music theory. It should"
                 " be in the format of [Question] (a) Option (b) Option (c) Option (d) Option  {Answer: Ans}",
        config=types.GenerateContentConfig(thinking_config=types.ThinkingConfig(thinking_budget=0))  # Disables thinking
    )

    return question.text


def interval_question():
    question = client.models.generate_content(
        model="gemini-1.5-flash",
        contents="Create an intermediate multiple choice trivia question based on semi-difficult subjects from music "
                 "theory. It should be in the format of [Question] (a) Option  (b) Option (c) Option (d)Option {Answer:"
                 " Ans}",
        config=types.GenerateContentConfig(thinking_config=types.ThinkingConfig(thinking_budget=0))  # Disables thinking
    )

    return question.text


def hard_question():
    question = client.models.generate_content(
        model="gemini-1.5-flash",
        contents="Create an painfully hard multiple choice trivia question based on anything from music theory. "
                 "It should be in the format of [Question] (a) Option  (b) Option  (c) Option  (d)Option "
                 " {Answer: Ans}",
        config=types.GenerateContentConfig(thinking_config=types.ThinkingConfig(thinking_budget=0))  # Disables thinking
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