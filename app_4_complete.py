import streamlit as st

# TODO: Insert the import statement for `run_flow_from_json` from langflow to enable JSON-based flow execution.
# This function is crucial for loading flow configurations dynamically.
# Example:
# from langflow.load import run_flow_from_json
from langflow.load import run_flow_from_json

# TODO: Insert the tweaks structure for configuring your langflow flow.
# This structure is used to customize various components of the flow,
# such as API keys and response formats. Modify the dictionary below
# as needed to fit your specific requirements.
#
# Example:
# TWEAKS = {
#   "Prompt-svuPA": {
#       "template": """Answer the user as if you were a funny generative AI geek.
#       User: {user_input}
#
#       Answer: """
#   },
#   "OpenAIModel-RhxsO": {
#       "openai_api_key": st.secrets['OPENAI_API_KEY']
#   },
#   "ChatOutput-wHG84": {},
#   "ChatInput-jLIhU": {}
# }
TWEAKS = {
    "Prompt-svuPA": {"template": """Answer the user as if you were a funny generative AI geek. 
  User: {user_input}

  Answer: """},
    "OpenAIModel-RhxsO": {"openai_api_key": st.secrets['OPENAI_API_KEY']},
    "ChatOutput-wHG84": {},
    "ChatInput-jLIhU": {}
}

# Start with empty messages, stored in session state
if 'messages' not in st.session_state:
    st.session_state.messages = []

# Draw a title and some markdown
st.title("Your personal Efficiency Booster")
st.markdown("""Generative AI is considered to bring the next Industrial Revolution.  
Why? Studies show a **37% efficiency boost** in day to day work activities!""")

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
    output = run_flow_from_json(flow="BasicPrompting.json",
                                input_value=question,
                                tweaks=TWEAKS)

    answer = output[0].outputs[0].results

    # Store the bot's answer in a session object for redrawing next time
    st.session_state.messages.append({"role": "ai", "content": answer})

    # Draw the bot's answer
    with st.chat_message('assistant'):
        st.markdown(answer)