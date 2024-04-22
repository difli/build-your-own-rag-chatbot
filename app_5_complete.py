import streamlit as st
import os
import tempfile

# TODO #1:
# 1. Copy and paste the necessary code from the langflow Python API tab for the Flow: "Chat_app_5".
#    Exclude the last two lines of the provided code; these will be used elsewhere.
# 2. Ensure the 'TWEAKS' dictionary is fully configured with all required customizations
#    specific to your flow needs.
# Example:
import requests
from typing import Optional

BASE_API_URL = "http://127.0.0.1:7861/api/v1/run"
FLOW_ID = "589cb5ee-ace6-440d-a885-bc0e9ef41636"
# You can tweak the flow by adding a tweaks dictionary
# e.g {"OpenAI-XXXXX": {"model_name": "gpt-4"}}

TWEAKS = {
  "ChatInput-Ed0w6": {},
  "TextOutput-vVPoH": {},
  "OpenAIEmbeddings-kl45J": {"openai_api_key": st.secrets['OPENAI_API_KEY']},
  "OpenAIModel-4A6FX": {"openai_api_key": st.secrets['OPENAI_API_KEY']},
  "Prompt-t8lIV": {"template": """You're a helpful AI assistent tasked to answer the user's questions.
You're friendly and you answer extensively with multiple sentences. You prefer to use bulletpoints to summarize.

CONTEXT:
{context}

QUESTION:
{question}

YOUR ANSWER:"""},
  "ChatOutput-5ifqe": {},
  "AstraDBSearch-7tbUz": {"api_endpoint": st.secrets['ASTRA_API_ENDPOINT'], "token": st.secrets['ASTRA_TOKEN']}
}

def run_flow(message: str,
  flow_id: str,
  output_type: str = "chat",
  input_type: str = "chat",
  tweaks: Optional[dict] = None,
  api_key: Optional[str] = None) -> dict:
    """
    Run a flow with a given message and optional tweaks.

    :param message: The message to send to the flow
    :param flow_id: The ID of the flow to run
    :param tweaks: Optional tweaks to customize the flow
    :return: The JSON response from the flow
    """
    api_url = f"{BASE_API_URL}/{flow_id}"

    payload = {
        "input_value": message,
        "output_type": output_type,
        "input_type": input_type,
    }
    headers = None
    if tweaks:
        payload["tweaks"] = tweaks
    if api_key:
        headers = {"x-api-key": api_key}
    response = requests.post(api_url, json=payload, headers=headers)
    return response.json()

# TODO #3:
# 1. Copy and paste the necessary code from the langflow "Python Code" tab for the Flow: "Vectorize_app_5".
#    Ensure to exclude the last two line of the provided code; these will be placed in a different section.
# 2. Rename 'TWEAKS' to 'VECTORIZE_TWEAKS' dictionary with all required customizations specific to your flow needs.
#    Ensure that API keys and endpoints in 'VECTORIZE_TWEAKS' are updated according to your environment.
# Example:
from langflow.load import run_flow_from_json
VECTORIZE_TWEAKS = {
  "File-hx9qW": {},
  "RecursiveCharacterTextSplitter-JNwYQ": {},
  "AstraDB-2HgLU": {"api_endpoint": st.secrets['ASTRA_API_ENDPOINT'], "token": st.secrets['ASTRA_TOKEN']},
  "OpenAIEmbeddings-qgFd2": {"openai_api_key": st.secrets['OPENAI_API_KEY']}
}

# Start with empty messages, stored in session state
if 'messages' not in st.session_state:
    st.session_state.messages = []

# Draw a title and some markdown
st.title("Your personal Efficiency Booster")
st.markdown("""Generative AI is considered to bring the next Industrial Revolution.  
Why? Studies show a **37% efficiency boost** in day to day work activities!""")

# Include the upload form for new data to be Vectorized
with st.sidebar:
    with st.form('upload'):
        uploaded_file = st.file_uploader('Upload a document for additional context', type=['pdf', 'txt', 'md', 'mdx', 'csv', 'json', 'yaml', 'yml', 'xml', 'html', 'htm', 'pdf', 'docx', 'py', 'sh', 'sql', 'js', 'ts', 'tsx'])
        submitted = st.form_submit_button('Save to Astra DB')
        if submitted:
            print(uploaded_file)
            # Write to temporary file
            temp_dir = tempfile.TemporaryDirectory()
            file = uploaded_file
            temp_filepath = os.path.join(temp_dir.name, file.name)
            with open(temp_filepath, 'wb') as f:
                f.write(file.getvalue())

            # TODO #4:
            # 1. Verify that the 'File-hx9qW' key exists in the 'VECTORIZE_TWEAKS' dictionary.
            # 2. Copy and paste the necessary code from the langflow "Python Code" tab for the Flow: "Vectorize_app_5".
            # Example:
            VECTORIZE_TWEAKS["File-hx9qW"]["path"] = temp_filepath
            output = run_flow_from_json(flow="Vectorize_app_5.json",
                                        input_value="message",
                                        tweaks=VECTORIZE_TWEAKS)

# Draw all messages, both user and bot so far (every time the app reruns)
for message in st.session_state.messages:
    st.chat_message(message['role']).markdown(message['content'])

# Draw the chat input box
if question := st.chat_input("What's up?"):
    # Store the user's question in a session object for redrawing next time
    st.session_state.messages.append({"role": "human", "content": question})

    # Draw the user's question
    with st.chat_message('human'):
        st.markdown(question)

    # TODO #2:
    # 1. Invoke the run_flow function using the provided question, flow_id, and tweaks.
    # 2. Capture and process the output to extract the desired result.
    # Example:
    output = run_flow(message=question, flow_id=FLOW_ID, tweaks=TWEAKS)
    answer = output['outputs'][0]['outputs'][0]['results']['result']

    # Store the bot's answer in a session object for redrawing next time
    st.session_state.messages.append({"role": "ai", "content": answer})

    # Draw the bot's answer
    with st.chat_message('assistant'):
        st.markdown(answer)