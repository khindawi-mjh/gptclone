import openai
import streamlit as st

# App Title
st.set_page_config(page_title="Khalid's ChatGPT Clone", layout="wide")
st.title("Khalid's ChatGPT Clone")

# Sidebar Configuration
# st.sidebar.header("🔧 Settings")
openai.api_key = st.secrets["OPENAI_API_KEY"]

# Select Model in Sidebar
if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-4o"

selected_model = st.sidebar.selectbox(
    "Choose a model:",
    ["gpt-3.5-turbo", "gpt-3.5-turbo-16k", "gpt-4o"],
    index=0,
    help="Choose the OpenAI model to use for responses."
)
st.session_state["openai_model"] = selected_model

# Chat History Initialization
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display Chat History
# st.markdown("### Chat History")
for message in st.session_state.messages:
    with st.container():
        if message["role"] == "user":
            st.markdown(f"**👤 You:** {message['content']}")
        else:
            st.markdown(f"**🤖 Assistant:** {message['content']}")

# Chat Input Section
# st.markdown("### Ask a Question")
prompt = st.chat_input("How can I assist you Mr. Khalo Abdullah?")

if prompt:
    # Append User Message
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.container():
        st.markdown(f"**👤 You:** {prompt}")

    # Generate Assistant Response
    with st.spinner("🤖 Thinking..."):
        try:
            response = openai.ChatCompletion.create(
                model=st.session_state["openai_model"],
                messages=[
                    {"role": m["role"], "content": m["content"]}
                    for m in st.session_state.messages
                ]
            )
            full_response = response["choices"][0]["message"]["content"]
        except Exception as e:
            full_response = f"An error occurred: {e}"

    # Display Assistant Response
    with st.container():
        st.markdown(f"**🤖 Assistant:** {full_response}")

    # Append Assistant Response
    st.session_state.messages.append({"role": "assistant", "content": full_response})