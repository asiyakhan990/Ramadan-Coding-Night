import streamlit as st
import random 
import time 

st.title("📝 Quiz Application")

questions = [
    {
        "question": "What is the capital of Pakistan?",
        "options": ["Lahore", "Karachi", "Islamabad", "Peshawar"],
        "answer": "Islamabad",
    },
    {
        "question": "Who is the founder of Pakistan?",
        "options": [
            "Allama Iqbal",
            "Liaquat Ali Khan",
            "Muhammad Ali Jinnah",
            "Benazir Bhutto",
        ],
        "answer": "Muhammad Ali Jinnah",
    },
    {
        "question": "Which is the national language of Pakistan?",
        "options": ["Punjabi", "Urdu", "Sindhi", "Pashto"],
        "answer": "Urdu",
    },
    {
        "question": "What is the currency of Pakistan?",
        "options": ["Rupee", "Dollar", "Taka", "Riyal"],
        "answer": "Rupee",
    },
    {
        "question": "Which city is known as the City of Lights in Pakistan?",
        "options": ["Lahore", "Islamabad", "Faisalabad", "Karachi"],
        "answer": "Karachi",
    },
    {
        "question": "When did Pakistan gain independence?",
        "options": ["14th August 1947", "23rd March 1940", "15th August 1947", " 14th August 1950"],
        "answer": "14th August 1947",
    },
    {
        "question": "Who was the first Prime Minister of Pakistan?",
        "options": ["Liaquat Ali Khan", "Zulfikar Ali Bhutto", "Muhammad Ali Jinnah", "Ayub Khan"],
        "answer": "Liaquat Ali Khan",
    },
    {
        "question": "What is the name of Pakistan’s national poet?",
        "options": ["Mirza Ghalib", "Allama Iqbal", "Faiz Ahmed Faiz", "Ahmed Faraz"],
        "answer": "Allama Iqbal",
    },
    {
        "question": "What is the highest peak in Pakistan?",
        "options": ["K2", "Nanga Parbat", "Rakaposhi", "Tirich Mir"],
    },
]

if "current_question" not in st.session_state:
    st.session_state.current_question = random.choice(questions)

question = st.session_state.current_question

st.subheader(question["question"])

selected_option = st.radio("Choose your answer", question["options"], key="answer")

if st.button("Submit Answer"):
    if selected_option == question["answer"]:
        st.success("✅ Correct!")
    else:
        st.error("❌ Incorrect! the correct answer is " + question["answer"])

    time.sleep(5)

    st.session_state.current_question = random.choice(questions)
    
    st.rerun()