import streamlit as st
import time
import random

# This file is for the frontend application
st.title("Main Title - Betting Agent")
st.header("Helps you win the bets")
st.subheader("Tell me about the match and I will help you win the bet")

if st.button("Close!"):
    st.write("Closing...")
    st.stop()

# Initialize the chat history (Self-determined object - messages)
if "messages" not in st.session_state:
    st.session_state.messages = []

# Define response generator
def response_generator(prompt):
    # 这里应该调用实际的 LLM API | Should call actual LLM API here
    responses = [
        f"这是对 '{prompt}' 的回答。Here's a response to '{prompt}'.",
        f"我理解你在问关于 '{prompt}'。I understand you're asking about '{prompt}'.",
        f"让我思考关于 '{prompt}' 的问题。Let me think about '{prompt}'."
    ]
    response = random.choice(responses)
    
    # Simulate typing effect
    for word in response.split():
        yield word + " "
        time.sleep(0.05)

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Using walrus operator (:=) to get input value and check if it exists in one line
if prompt := st.chat_input("输入您的问题... | Type your question..."):
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Display user's message in the chat
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display AI message in the chat
    with st.chat_message("ai"):
        st.write_stream(response_generator(prompt))
    
    st.session_state.messages.append({"role": "ai", "content": "This is response from AI"})
