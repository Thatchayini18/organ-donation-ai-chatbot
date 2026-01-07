import streamlit as st
from chatbot import chatbot_response

st.set_page_config(page_title="Organ Donation AI Assistant")

st.title("🫀 Organ Donation AI Assistant")

if "messages" not in st.session_state:
    st.session_state.messages = []

if "state" not in st.session_state:
    st.session_state.state = {}

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

user_input = st.chat_input("Type here...")

if user_input:
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    with st.chat_message("user"):
        st.markdown(user_input)

    response = chatbot_response(user_input, st.session_state.state)

    st.session_state.messages.append(
        {"role": "assistant", "content": response}
    )

    with st.chat_message("assistant"):
        st.markdown(response)

if st.button("🔄 Reset Chat"):
    st.session_state.messages = []
    st.session_state.state = {}
    st.experimental_rerun()
