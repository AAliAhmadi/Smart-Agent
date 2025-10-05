import streamlit as st
from langchain_community.chat_message_histories import StreamlitChatMessageHistory
from .agent_logic import run_agent

# --------------------------
# Streamlit App Setup
# --------------------------
st.set_page_config(page_title="Smart AI Agent", page_icon="🤖")
st.title("🤖 Smart AI Agent (Gemma3 + Web Tools)")
st.caption("Uses web tools when online; falls back to Gemma3:4b when offline.")

# --------------------------
# Chat Memory
# --------------------------
if "history" not in st.session_state:
    st.session_state["history"] = StreamlitChatMessageHistory()

chat_history = st.session_state["history"]

# --------------------------
# UI Controls
# --------------------------
if st.button("🗑️ Clear Chat History"):
    st.session_state["history"].clear()
    st.experimental_rerun()

# Display past messages
for msg in chat_history.messages:
    if msg.type == "human":
        st.chat_message("user").write(msg.content)
    else:
        st.chat_message("assistant").write(msg.content)

# --------------------------
# User Input and Response
# --------------------------
if user_input := st.chat_input("Ask me anything..."):
    st.chat_message("user").write(user_input)
    output, online = run_agent(user_input, chat_history)

    if online:
        st.info("🌐 Internet detected — using Wikipedia + DuckDuckGo search tools.")
    else:
        st.warning("⚠️ No internet — switching to offline mode. Some info may be outdated.")

    st.chat_message("assistant").write(output)
