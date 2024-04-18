import streamlit as st
import os

# TODO: Insert the import statement for `run_flow_from_json` from langflow to enable JSON-based flow execution.
# This function is crucial for loading flow configurations dynamically.
# Example:
# from langflow.load import run_flow_from_json
from langflow.load import run_flow_from_json

myfile= os.path.join(os.getcwd(), "essay.pdf")
print(myfile)

# TODO: Insert the tweaks structure for configuring your langflow flow.
# This structure is used to customize various components of the flow,
# such as API keys and response formats. Modify the dictionary below
# as needed to fit your specific requirements.
#
# Example:
# TWEAKS = {
#   "ChatInput-QH9Vn": {},
#   "TextOutput-rOdzu": {},
#   "OpenAIEmbeddings-oyXOD": {"openai_api_key": st.secrets['OPENAI_API_KEY']},
#   "OpenAIModel-1gPW2": {"openai_api_key": st.secrets['OPENAI_API_KEY']},
#   "Prompt-6uVLA": {"template": """You're a helpful AI assistent tasked to answer the user's questions.
# You're friendly and you answer extensively with multiple sentences. You prefer to use bulletpoints to summarize.
#
# CONTEXT:
# {context}
#
# QUESTION:
# {question}
#
# YOUR ANSWER:"""},
#   "ChatOutput-OT9zk": {},
#   "File-icQdf": {},
#   "RecursiveCharacterTextSplitter-AbAFw": {},
#   "AstraDBSearch-urw0f": {"api_endpoint": st.secrets['ASTRA_API_ENDPOINT'], "token": st.secrets['ASTRA_TOKEN']},
#   "AstraDB-SpIGI": {"api_endpoint": st.secrets['ASTRA_API_ENDPOINT'], "token": st.secrets['ASTRA_TOKEN']},
#   "OpenAIEmbeddings-wTu3X": {"openai_api_key": st.secrets['OPENAI_API_KEY']}
# }
TWEAKS = {
  "ChatInput-QH9Vn": {},
  "TextOutput-rOdzu": {},
  "OpenAIEmbeddings-oyXOD": {"openai_api_key": st.secrets['OPENAI_API_KEY']},
  "OpenAIModel-1gPW2": {"openai_api_key": st.secrets['OPENAI_API_KEY']},
  "Prompt-6uVLA": {"template": """You're a helpful AI assistent tasked to answer the user's questions.
You're friendly and you answer extensively with multiple sentences. You prefer to use bulletpoints to summarize.

CONTEXT:
{context}

QUESTION:
{question}

YOUR ANSWER:"""},
  "ChatOutput-OT9zk": {},
  "File-icQdf": {"path": myfile},
  "RecursiveCharacterTextSplitter-AbAFw": {},
  "AstraDBSearch-urw0f": {"api_endpoint": st.secrets['ASTRA_API_ENDPOINT'], "token": st.secrets['ASTRA_TOKEN']},
  "AstraDB-SpIGI": {"api_endpoint": st.secrets['ASTRA_API_ENDPOINT'], "token": st.secrets['ASTRA_TOKEN']},
  "OpenAIEmbeddings-wTu3X": {"openai_api_key": st.secrets['OPENAI_API_KEY']}
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
            myfile= uploaded_file
            print(myfile)

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

# TODO: Ensure the 'run_flow_from_json' function is correctly imported from the langflow package.
# Ensure that the 'BasicPrompting.json' file exists and is properly formatted according to langflow requirements.
# Verify that 'TWEAKS' dictionary is defined with all necessary customizations for this flow.
# Example:
# from langflow.load import run_flow_from_json
# Ensure 'question' variable is initialized with the user input that will be passed to the flow.
#
# Example of usage:
# output = run_flow_from_json(flow="BasicPrompting.json",
#                             input_value=question,
#                             tweaks=TWEAKS)
    output = run_flow_from_json(flow="Vector Store RAG BYORCB.json",
                                input_value=question,
                                tweaks=TWEAKS)

    answer = output[0].outputs[0].results

    # Store the bot's answer in a session object for redrawing next time
    st.session_state.messages.append({"role": "ai", "content": answer})

    # Draw the bot's answer
    with st.chat_message('assistant'):
        st.markdown(answer)