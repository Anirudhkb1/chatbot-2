import streamlit as st
import ollama

# Configure page settings
st.set_page_config(
    page_title="AI Teacher Chatbot",
    page_icon="🎓",
    layout="centered"
)

st.title("🎓 Friendly AI Teacher")
st.caption("Ask any technical concept and learn in simple, beginner-friendly terms!")

# Default system prompt
SYSTEM_PROMPT = """You are a friendly AI teacher.

Explain technical concepts to complete beginners.
Use simple English.
Give practical examples.
Avoid unnecessary technical jargon."""

# Sidebar for controls
with st.sidebar:
    st.header("⚙️ Settings")
    model_name = st.text_input("Ollama Model", value="tinyllama:latest")
    
    if st.button("🗑️ Clear Chat History", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

# Initialize session state for messages
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("Ask a question (e.g., What is a neural network?)"):
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Prepare message payload for Ollama including system instruction
    messages_payload = [{"role": "system", "content": SYSTEM_PROMPT}] + [
        {"role": m["role"], "content": m["content"]}
        for m in st.session_state.messages
    ]

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        try:
            # Stream response from Ollama
            response_stream = ollama.chat(
                model=model_name,
                messages=messages_payload,
                stream=True
            )

            # Generator for streaming tokens into Streamlit
            def stream_response():
                for chunk in response_stream:
                    yield chunk["message"]["content"]

            full_response = st.write_stream(stream_response)

            # Add assistant response to history
            st.session_state.messages.append({"role": "assistant", "content": full_response})

        except Exception as e:
            st.error(f"Error communicating with Ollama: {e}")
