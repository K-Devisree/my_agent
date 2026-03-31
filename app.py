import streamlit as st
from agent import ask_agent

st.set_page_config(page_title="My AI Agent", layout="centered")
st.title("🤖 My AI Agent")
st.write("Ask questions, fetch weather, jokes, or news!")

query = st.text_input("Enter your question:")

if st.button("Ask"):
    if query:
        answer = ask_agent(query)
        st.success(answer)