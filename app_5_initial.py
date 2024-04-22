import streamlit as st
import os
import tempfile

# TODO #1:
# 1. Copy and paste the necessary code from the langflow Python API tab for the Flow: "Chat_app_5".
#    Exclude the last two lines of the provided code; these will be used elsewhere.
# 2. Ensure the 'TWEAKS' dictionary is fully configured with all required customizations
#    specific to your flow needs.
# Example:
# TODO #1:
# 1. Copy and paste the necessary code from the langflow Python Code tab for the Flow: "Chat_app_5".
#    Exclude the last line of the provided code; this will be used elsewhere.
# 2. Ensure the 'TWEAKS' dictionary is fully configured with all required customizations
#    specific to your flow needs.
# Example:
# from langflow.load import run_flow_from_json
#
# TWEAKS = {
#   "ChatInput-Ed0w6": {},
#   "TextOutput-vVPoH": {},
#   "OpenAIEmbeddings-kl45J": {"openai_api_key": st.secrets['OPENAI_API_KEY']},
#   "OpenAIModel-4A6FX": {"openai_api_key": st.secrets['OPENAI_API_KEY']},
#   "Prompt-t8lIV": {"template": """You're a helpful AI assistent tasked to answer the user's questions.
# You're friendly and you answer extensively with multiple sentences. You prefer to use bulletpoints to summarize.
#
# CONTEXT:
# {context}
#
# QUESTION:
# {question}
#
# YOUR ANSWER:"""},
#   "ChatOutput-5ifqe": {},
#   "AstraDBSearch-7tbUz": {"api_endpoint": st.secrets['ASTRA_API_ENDPOINT'], "token": st.secrets['ASTRA_TOKEN']}
# }

# TODO #3:
# 1. Copy and paste the necessary code from the langflow "Python Code" tab for the Flow: "Vectorize_app_5".
#    Ensure to exclude the last two line of the provided code; these will be placed in a different section.
# 2. Rename 'TWEAKS' to 'VECTORIZE_TWEAKS' dictionary with all required customizations specific to your flow needs.
#    Ensure that API keys and endpoints in 'VECTORIZE_TWEAKS' are updated according to your environment.
# Example:
# from langflow.load import run_flow_from_json
# VECTORIZE_TWEAKS = {
#   "File-hx9qW": {},
#   "RecursiveCharacterTextSplitter-JNwYQ": {},
#   "AstraDB-2HgLU": {"api_endpoint": st.secrets['ASTRA_API_ENDPOINT'], "token": st.secrets['ASTRA_TOKEN']},
#   "OpenAIEmbeddings-qgFd2": {"openai_api_key": st.secrets['OPENAI_API_KEY']}
# }

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
            # VECTORIZE_TWEAKS["File-hx9qW"]["path"] = temp_filepath
            # output = run_flow_from_json(flow="Vectorize_app_5.json",
            #                             input_value="message",
            #                             tweaks=VECTORIZE_TWEAKS)

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
    # output = run_flow_from_json(flow="Chat_app_5.json", input_value=question, tweaks=TWEAKS)
    # answer = output[0].outputs[0].results

    # Store the bot's answer in a session object for redrawing next time
    st.session_state.messages.append({"role": "ai", "content": answer})

    # Draw the bot's answer
    with st.chat_message('assistant'):
        st.markdown(answer)