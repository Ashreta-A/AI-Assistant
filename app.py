import streamlit as st
import requests

# Your Hugging Face model & token
API_URL = "https://hf.co/chat/assistant/6845433d9425568f1ee8185e"
HF_TOKEN = "hf_dUYbEHQXxlWSbAabaqXaTAYlmCsFRcDOnBE"

headers = {"Authorization": f"Bearer {HF_TOKEN}"}

# Function to query Hugging Face model
def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

# Streamlit UI
st.set_page_config(page_title="HuggingFace Chatbot", layout="centered")
st.title("🤖 HuggingFace Chatbot in Streamlit")

# Keep chat history in session
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input
prompt = st.chat_input("Ask me anything...")

if prompt:
    # Add user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Query model
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = query({"inputs": prompt})
            try:
                reply = response[0]["generated_text"]
            except:
                reply = "Sorry, I couldn't generate a response."

            st.markdown(reply)
            st.session_state.messages.append({"role": "assistant", "content": reply})
