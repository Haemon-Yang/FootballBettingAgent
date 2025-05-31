import streamlit as st
import time
from graph import Workflow
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import Dict
import asyncio
import threading
from init import get_initial_graph_state, system_init, setup_scheduled_updates

async def process_query(workflow: Workflow, initial_state: dict, result_container: dict):
    await Workflow.fetch_response(workflow, initial_state, result_container)

def run_async_task_in_thread(workflow, initial_state, result_container):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(process_query(workflow, initial_state, result_container))


# Set page configuration
st.set_page_config(
    page_title="Smart Betting Assistant",
    page_icon="🎯",
    layout="wide"
)

# Custom CSS for better styling
st.markdown("""
    <style>
    .main-header {
        color: #1E88E5;
        font-family: 'Helvetica Neue', sans-serif;
    }
    .sub-header {
        color: #424242;
        font-family: 'Helvetica Neue', sans-serif;
    }
    .stButton>button {
        background-color: #1E88E5;
        color: white;
        border-radius: 10px;
        padding: 10px 25px;
        font-weight: bold;
    }
    .stTextInput>div>div>input {
        border-radius: 10px;
    }
    .chat-message {
        padding: 15px;
        border-radius: 10px;
        margin: 5px 0;
    }
    </style>
    """, unsafe_allow_html=True)

# Main layout with columns
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    # Title section with enhanced styling
    st.markdown("<h1 class='main-header'>🎯 Smart Betting Assistant</h1>", unsafe_allow_html=True)
    st.markdown("<h3 class='sub-header'>Your AI-Powered Betting Strategy Partner</h3>", unsafe_allow_html=True)
    
    # Add a subtle divider
    st.markdown("---")

    # Information container
    with st.container():
        st.info("💡 Tell me about the match and I'll help you make informed betting decisions.")

# Initialize LLM and Workflow once (only on first run)
if "workflow" not in st.session_state:
    load_dotenv()
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)  # Adjust based on your actual LLM setup
    st.session_state.workflow = Workflow(llm)
    st.session_state.LLM = llm

# System Initialization
if "is_initialized" not in st.session_state:
    #system_init(llm)
    #setup_scheduled_updates(**st.session_state)
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
    with st.chat_message("ai", avatar="🤖"):
        message_placeholder = st.empty()
        
        # Start API call in a separate thread to not block the UI
        result_container = {"response": None, "done": False}
        
        # In your Streamlit code:
        result_container = {"response": None, "done": False}
        thread = threading.Thread(target=run_async_task_in_thread, args=(st.session_state.workflow, initial_state, result_container))
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

        # Process markdown response with typing effect - 2
        # ===============================================
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
            
            message_placeholder.markdown(response)
        else:
            # Just display the full response with markdown
            message_placeholder.markdown(response)
            
    # Add AI response to chat history
    st.session_state.messages.append({"role": "ai", "content": response})
