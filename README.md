# AI Teacher Chatbot (Streamlit + Ollama)

A friendly AI Teacher chatbot application built using Streamlit and Ollama (`tinyllama:latest`).

## Features
- Interactive chat UI with `st.chat_input` and `st.chat_message`.
- Real-time token streaming (`stream=True`) for fast, responsive responses.
- Persistent conversation history within session state.
- System prompt configuring the AI as a beginner-friendly teacher.
- Clear chat history button.

## How to Run

1. Make sure Ollama is running:
   ```bash
   ollama serve
   ```
2. Pull the model (if not already downloaded):
   ```bash
   ollama pull tinyllama:latest
   ```
3. Run the Streamlit application:
   ```bash
   streamlit run app.py
   ```
