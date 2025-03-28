import streamlit as st
import time
from graph import Workflow
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import threading
from init import get_initial_graph_state, system_init, setup_scheduled_updates

# This file is for the frontend application
st.title("Main Title - Betting Agent")
st.header("Helps you win the bets")
st.subheader("Tell me about the match and I will help you win the bet")

# Initialize LLM and Workflow once (only on first run)
if "workflow" not in st.session_state:
    load_dotenv()
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)  # Adjust based on your actual LLM setup
    st.session_state.workflow = Workflow(llm)

# System Initialization
if "is_initialized" not in st.session_state:
    system_init(llm)
    setup_scheduled_updates(**st.session_state)
    st.session_state.is_initialized = True

if st.button("Close!"):
    st.write("Closing...")
    st.stop()

# Initialize the chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Using walrus operator (:=) to get input value and check if it exists in one line
if prompt := st.chat_input("Type your question..."):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Display user's message in the chat
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Process the query using workflow
    # Create initial state with user query
    initial_state = get_initial_graph_state()
    initial_state["user_query"] = prompt
    
    # Create a placeholder for the AI response
    with st.chat_message("ai"):
        message_placeholder = st.empty()
        
        # Start API call in a separate thread to not block the UI
        result_container = {"response": None, "done": False}
        
        # Start the background thread with the external function
        thread = threading.Thread(
            target=Workflow.fetch_response,
            args=(st.session_state.workflow, initial_state, result_container)
        )
        thread.start()
        
        # Show animated thinking indicator while waiting for response
        thinking_dots = [".", "..", "..."]
        dot_index = 0
        
        # Keep animating until we get a response
        while not result_container["done"]:
            message_placeholder.markdown(f"*Thinking{thinking_dots[dot_index]}*")
            dot_index = (dot_index + 1) % len(thinking_dots)
            time.sleep(0.3)
        
        # Get the response once it's ready
        response = result_container["response"]
        
        # Process markdown response with typing effect
        if st.session_state.get("enable_typing_effect", True):
            # Split by paragraphs to better preserve markdown structure
            paragraphs = response.split('\n')
            current_text = ""
            
            for i, paragraph in enumerate(paragraphs):
                # Add paragraph to current text
                if i > 0:
                    current_text += '\n'
                current_text += paragraph
                
                # Update display with markdown formatting
                message_placeholder.markdown(current_text)
                time.sleep(0.1)
        else:
            # Just display the full response with markdown
            message_placeholder.markdown(response)
    
    # Add AI response to chat history
    st.session_state.messages.append({"role": "ai", "content": response})
