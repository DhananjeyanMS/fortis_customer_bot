import os
import time
import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv, set_key

# Load environment variables from .env file
load_dotenv()

# Initialize OpenAI client
openai_api_key = os.getenv('OPENAI_API_KEY')
client = OpenAI(api_key=openai_api_key)


assistant_id = os.getenv("ASSISTANT_ID")

# Streamlit App Configuration
st.set_page_config(page_title="Fortis", layout="wide")

# Session State Initialization
if 'thread_id' not in st.session_state:
    st.session_state['thread_id'] = None
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []
if 'waiting_for_response' not in st.session_state:
    st.session_state['waiting_for_response'] = False

# Function to handle user input
def handle_user_message(user_message):
    if not user_message:
        st.warning("Please enter a message.")
        return

    # Append user message to chat history
    st.session_state['chat_history'].append(("User", user_message))
    st.session_state['waiting_for_response'] = True  # Set flag to wait for assistant response
    st.rerun()  # Update UI immediately

# Function to fetch assistant's response
def fetch_assistant_response():
    # Ensure thread exists
    if st.session_state['thread_id'] is None:
        thread = client.beta.threads.create()
        st.session_state['thread_id'] = thread.id

    thread_id = st.session_state['thread_id']

    # Fetch assistant response
    client.beta.threads.messages.create(
        thread_id=thread_id,
        role='user',
        content=st.session_state['chat_history'][-1][1]  # Last user message
    )
    run = client.beta.threads.runs.create(
        thread_id=thread_id,
        assistant_id=assistant_id
    )

    while run.status in ['queued', 'in_progress']:
        time.sleep(0.5)
        run = client.beta.threads.runs.retrieve(
            thread_id=thread_id,
            run_id=run.id
        )

    all_messages = client.beta.threads.messages.list(thread_id=thread_id)
    assistant_messages = [
        msg for msg in all_messages.data if msg.role == 'assistant'
    ]

    if assistant_messages:
        latest_response = assistant_messages[0].content
        assistant_response = ''.join(
            block.text.value for block in latest_response if block.type == 'text'
        )
    else:
        assistant_response = "No response from assistant."

    # Append assistant response to chat history
    st.session_state['chat_history'].append(("Assistant", assistant_response))
    st.session_state['waiting_for_response'] = False  # Clear the waiting flag
    st.rerun()  # Update UI after assistant response

# Sidebar
with st.sidebar:
    st.image("chatbot_image.png", use_container_width=True)  # Replace with your chatbot image
    st.title("Fortis")
    st.write(
        """
        - **Marketing**. **Business**. **Creation**.
        - We help our clients achieve their business goals by implementing comprehensive and effective marketing solutions.
        """
    )
    # Clear Chat Button


# Main Layout
st.title("Fortis - Marketing Agency")
st.write("Welcome! It's AI Kasia from Fortis")
if st.button("Clear Chat"):
    st.session_state['thread_id'] = None
    st.session_state['chat_history'] = []
    st.session_state['waiting_for_response'] = False

# Display chat history
for role, message in st.session_state['chat_history']:
    if role == "User":
        st.chat_message("user").markdown(message)
    else:
        st.chat_message("assistant").markdown(message)

# Input Box
user_input = st.chat_input("Type a message...")
if user_input:
    handle_user_message(user_input)  # Handle user input

# Check if waiting for response
if st.session_state['waiting_for_response']:
    fetch_assistant_response()  # Fetch assistant response if the flag is set

