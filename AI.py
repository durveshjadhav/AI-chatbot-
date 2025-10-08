import streamlit as st
import openai

# -------------------
# Set up OpenAI API Key
# -------------------
openai.api_key = "YOUR_OPENAI_API_KEY"

# -------------------
# Streamlit UI
# -------------------
st.set_page_config(page_title="AI Chatbot", page_icon="🤖")
st.title("🤖 AI Chatbot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages
for message in st.session_state.messages:
    if message["role"] == "user":
        st.markdown(f"**You:** {message['content']}")
    else:
        st.markdown(f"**AI:** {message['content']}")

# User input
user_input = st.text_input("Type your message:", key="input")

if st.button("Send") and user_input:
    # Append user message
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Call OpenAI API
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # or "gpt-4" if you have access
        messages=st.session_state.messages
    )

    # Get AI reply
    ai_message = response['choices'][0]['message']['content']

    # Append AI message to chat history
    st.session_state.messages.append({"role": "assistant", "content": ai_message})

    # Clear input box
    st.session_state.input = ""
    
    # Rerun to display updated chat
    st.experimental_rerun()
