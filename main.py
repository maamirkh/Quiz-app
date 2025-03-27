import streamlit as st
import random
import time
st.title("Quiz Application")

questions = [
    {
        "question": "what is the capital of Pakistan",
        "options": ["Karachi", "Islamabad", "Lahore", "Quetta"],
        "answer": "Islamabad"
    },
    {
        "question": "Who is the founder of Pakistan",
        "options": [
            "Benazir Bhutto",
            "Allama Iqbal",
            "Liaquat Ali Khan",
            "Muhammad Ali Jinnah"
        ],
        "answer": "Muhammad Ali Jinnah"
    },
    {
        "question": "What is the largest city in Pakistan",
        "options": ["Islamabad", "Lahore", "Karachi", "Peshawar"],
        "answer": "Karachi"
    },
    {
        "question": "What is the National language of Pakistan",
        "options": ["Sindhi", "English", "Punjabi", "Urdu"],
        "answer": "Urdu"
    },
    {
        "question": "What is the currency of Pakistan",
        "options": ["Dollar", "Rupee", "Pound", "Euro"],
        "answer": "Rupee"
    },
    {
        "question": "Who is the first Prime Minister of Pakistan",
        "options": ["Muhammad Ali Jinnah", "Liaquat Ali Khan", "Ayub Khan", "Zulfikar Ali Bhutto"],
        "answer": "Liaquat Ali Khan"
    }
]

# Initialize a random question if none in the session state
if "current_question" not in st.session_state:
    st.session_state.current_question = random.choice(questions)

# Get the current question from session state
question = st.session_state.current_question

# Display the question
st.subheader(question["question"])

# Create radio button for the option
selected_option = st.radio("Choose your answer", question["options"], key = "answer")

# submit button to check the answer
if st.button("Submit Answer"):
    # Check if the answer is correct
    if selected_option == question["answer"]:
        st.success("Correct Answer!")
    else:
            st.error("Incorrect Answer! the correct answer is " + question["answer"])

    # wait for 3 seconds before showing the next question
    time.sleep(3)

    # Select a new random question
    st.session_state.current_question = random.choice(questions)

    # rerun the app to display next question
    st.rerun()