import streamlit as st
import pandas as pd
from utils.ai_chat import query_data_chat

st.title("💬 Conversational Data Agent")

uploaded_file = st.file_uploader("Upload a CSV file to query", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    dataframe_head = df.head(3).to_string()

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if user_input := st.chat_input("Ask a question about this dataset..."):
        st.session_state.messages.append({"role": "user", "content": user_input})
        with st.chat_message("user"):
            st.markdown(user_input)

        with st.chat_message("assistant"):
            response = query_data_chat(dataframe_head, st.session_state.messages, user_input)
            st.markdown(response)

        st.session_state.messages.append({"role": "assistant", "content": response})